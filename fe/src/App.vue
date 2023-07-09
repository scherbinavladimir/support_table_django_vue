<script setup>

import TableVue from "@/components/Table/TableVue.vue";
import {nextTick, onMounted, ref, watchEffect} from "vue";
import {api} from "@/api";
import StatusFilter from "@/components/Table/StatusFilter.vue";
import SearchInput from "@/components/Table/SearchInput.vue";
import FieldSelector from "@/components/Table/FieldSelector.vue";
import ContactMe from "@/components/ContactMe.vue";


const supportRequests = ref({
  count: 0,
  results: []
})

const pagination = ref({
  page: 1,
  pageSize: 20,
})

let loadParams = {
  page: pagination.value.page,
  page_size: pagination.value.pageSize
}

let loadingData = false
const loadData = async ()=>{
  if (loadingData) return
  loadingData = true
  supportRequests.value = await api.getSupportRequests(loadParams)
  pagination.value.maxPage = Math.round(supportRequests.value.count / pagination.value.pageSize)
  pagination.value.page = loadParams.page
  loadingData = false
}

let supportRequestsFields = []
const columns = ref([])
const loadFields = async ()=>{
  supportRequestsFields = await api.getSupportRequestFields()
  columns.value = Object.keys(supportRequestsFields).map(fieldName=>{
    return {
      key: fieldName,
      name: supportRequestsFields[fieldName].name,
      sort: supportRequestsFields[fieldName].ordering ? {active: false} : null,
      selected: true
    }
  })
}
const selectColumns = (key, checked)=>{
  columns.value.filter(col=>col.key===key)[0].selected = checked
  nextTick(()=>localStorage.setItem('selectedColumns', JSON.stringify(columns.value)))

}

onMounted(()=>{
  loadData()
  loadFields().then(()=>{
    const selected = JSON.parse(localStorage.getItem('selectedColumns', null))
    if (selected){
      selected.forEach(col=>{
        selectColumns(col.key, col.selected)
      })
    }
  })

})

const sort = (col, desc)=>{
  columns.value.forEach(cl=>{
    if (cl===col){
      cl.sort.active = true
      cl.sort.desc = desc
    } else if (cl.sort) {
      delete cl.sort.desc
      cl.sort.active = false
    }
  })
  loadParams.ordering = `${desc?'-':''}${col.key}`
  loadData()
}

const paginate = (pageNumber)=>{
  if (loadParams.page !== pageNumber){
    loadParams.page = pageNumber
    loadData()
  }
}

const statusFilters = ref([
  {value: 'new', title: 'Открытые'},
  {value: 'proc', title: 'Ожидают подтверждения'},
  {value: 'rjct', title: 'Неоценённые'},
  {value: 'clsd', title: 'Закрытые'},
  {value: undefined, title: 'Все', active: true},
])

const filterData = (selectedValue)=>{
  statusFilters.value.forEach(status=>(delete status.active))
  statusFilters.value.filter(s=>s.value===selectedValue)[0].active = true
  loadParams.status = selectedValue
  loadData()
}

const searchValue = ref('')
watchEffect(()=>{
  if (searchValue.value){
    loadParams.search = searchValue.value
  } else {
    loadParams.search = undefined
  }
  loadData()
})
</script>
<template>
  <div class="container mt-4">
    <h3 > Список обращений</h3>
    <div class="d-lg-flex justify-content-between mb-3">
      <status-filter
        :statuses="statusFilters"
        @filter="filterData"
      />
      <div class="d-flex align-items-center mt-2 mt-lg-0">
        <search-input v-model="searchValue">Глобальный поиск</search-input>
        <field-selector
            :fields="columns"
            @select="selectColumns"
            class="ms-2"
        />
      </div>
    </div>
    <table-vue
      :columns="columns"
      :rows="supportRequests.results"
      :pagination="pagination"
      class="tableMaxHeight"
      @sort="sort"
      @paginate="paginate"
    />
  <contact-me/>
  </div>
</template>


<style>
.statusFilter{

}
.tableMaxHeight{
  max-height: calc(100vh - 200px);
}
</style>
