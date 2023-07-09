<script setup>
/* eslint-disable */
import {computed} from "vue";
import {isDateTime} from "@/utils/datetime";

const props = defineProps({
  columns: {
    type: Object,
    required: true
  },
  rows:{
    type: Array,
    required:true,
    default: ()=>([])
  },
  pagination: {
    type: Object,
    default: ()=>({
      page: 1,
      pageSize: 10,
      maxPage: null,
    })
  },
})
const emit = defineEmits(['sort', 'paginate'])

const sortColumn = (col)=>{
  if (!col.sort) return
  const desc = !(col.sort.desc === undefined || col.sort.desc === true)
  emit('sort', col, desc)
}

const formatCellValue = (cellValue)=>{
  if (isDateTime(cellValue)){
    return new Date(cellValue).toLocaleString()
  } else if (typeof cellValue === 'boolean'){
    return `<i class="bi bi${cellValue?'-check':''}-circle"></i>`
  }
  return cellValue
}
const sortClass = (col)=>{
  if (!col.sort) return ''
  if (col.sort.active && col.sort.desc){
    return 'order-desc'
  } else if (col.sort.active && col.sort.desc === false){
    return 'order-asc'
  } else {
    return 'opacity-25'
  }
}

const paginate = (pageNumber)=>{
  if (pageNumber<1){
    pageNumber = 1
  } else if (pageNumber > props.pagination.maxPage){
    pageNumber = props.pagination.maxPage
  }
  emit('paginate', pageNumber)
}
const currentThreePages = computed(()=>{
  if (props.pagination.page > 2 && (props.pagination.page+1 < props.pagination.maxPage)){
    return [props.pagination.page -1, props.pagination.page, props.pagination.page +1]
  } else if (props.pagination.page > 2 && (props.pagination.page+1 === props.pagination.maxPage)){
    return [props.pagination.page-2, props.pagination.page-1, props.pagination.page]
  } else {
    return [1,2,3]
  }
})

const displayColumns = computed(()=>props.columns.filter(c=>c.key !== 'id' && c.selected))
</script>
<template>
<div class="w-100 h-100">
  <div class="table-wrap w-100 h-100 overflow-x-scroll">
  <table class="position-relative">
    <thead class="position-sticky">
    <tr>
      <th><input type="checkbox" disabled></th>
      <th @click="sortColumn(col)" v-for="col in displayColumns">
        <div class="d-flex justify-content-between">
          <div>{{ col.name }}</div>
          <div v-if="col.sort" class="ms-3 flex-shrink-0">
            <img height="8" width="8" :class="sortClass(col)" :src="require('@/assets/triangle.svg')">
          </div>
        </div>
    </th></tr>
    </thead>
    <tbody class="overflow-y-scroll">
      <tr v-for="row in rows">
        <td><input type="checkbox"></td>
        <td
          v-for="col in displayColumns"
          v-html="formatCellValue(row[col.key])"
          class="cell text-nowrap"
        ></td>
      </tr>
    </tbody>
  </table>
  </div>
  <div class="mt-2">
    <div class="mx-auto d-flex justify-content-between pagination-bar">
      <div><i @click="paginate(pagination.page-1)" class="bi bi-chevron-left fs-14 fw-bold"></i></div>
      <div class="d-flex" v-if="pagination.maxPage && pagination.maxPage<5">
        <div
          class="page mx-1 text-center"
          @click="paginate(i)"
          v-for="i in Array.from({length:pagination.maxPage}, (v, k) => k+1)"
          :class="{'active': i===pagination.page}"
        ><span>{{ i }}</span></div>
      </div>
      <div class="d-flex" v-if="pagination.maxPage && pagination.maxPage>=5">
        <div v-if="currentThreePages[0] > 1" @click="paginate(1)" class="page mx-1 text-center" :class="{'active': 1===pagination.page}"><span>1</span></div>
        <span v-if="currentThreePages[0] > 2">...</span>
        <div @click="paginate(i)" class="page mx-1 text-center" :class="{'active': i===pagination.page}" v-for="i in currentThreePages"><span>{{ i }}</span></div>
        <span v-if="currentThreePages[currentThreePages.length-1]+1 < pagination.maxPage">...</span>
        <div @click="paginate(pagination.maxPage)" :class="{'active': pagination.maxPage===pagination.page}" class="page mx-1 text-center"><span>{{ pagination.maxPage }}</span></div>
      </div>
      <div><i @click="paginate(pagination.page+1)" class="bi bi-chevron-right fs-14 fw-bold"></i></div>
    </div>
  </div>
</div>
</template>

<style scoped>
.table-wrap{
  background-color: white;
  border-radius: var(--border-radius);
  border: 1px rgb(243,	243, 243) solid;
  /*box-shadow: 0 0 2px black;*/
  max-height: inherit;
}
table{
  font-size: 14px;
  padding: 0 5px 5px 0;
}
thead tr{
  padding-bottom: 1px;
  background-color: rgb(243,	243, 243);
  border-bottom: 1px lightgrey;
}
th{
  font-weight: 400;
  color: rgb(86, 85, 85);
  min-width: fit-content;
}
td, th{
  max-width: 200px;
  white-space: nowrap;
  text-overflow: ellipsis;
  padding: 0.75rem 1.25rem;
}
td{
  overflow: hidden;
}
tr{
  border: none;
}
.order-desc{
  transform: rotate(180deg);
}
.pagination-bar{
  width: max-content;
}
.pagination-bar .page{
  min-width: 30px;
  border: #dadada 1px solid;
  border-radius: 3px;
}
.page.active {
  background-color: rgb(243,	243, 243);
}
.page:hover, .pagination-bar .bi:hover{
  box-shadow: 0 0 3px grey;
}
::-webkit-scrollbar {
  -webkit-appearance: none;
    background-color: rgb(218,218,218);
    border-radius: 6px;
}
::-webkit-scrollbar:horizontal{
    height: 6px;
}
::-webkit-scrollbar:vertical{
    width: 6px;
}
::-webkit-scrollbar-thumb {
  border-radius: 4px;
  background-color: rgba(0, 0, 0, 0.85);
}
::-webkit-scrollbar-corner{
    opacity: 0;
}
</style>