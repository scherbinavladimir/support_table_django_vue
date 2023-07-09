<script setup>
/* eslint-disable */
const props = defineProps({
  statuses:{
    type: Array,
    required: true
  }
})

const emit = defineEmits(['filter'])
const filter = (status)=>{
  emit('filter', status.value)
}
</script>

<template>
<div class="d-flex statusFilter overflow-x-scroll">
  <div
    v-for="status in statuses"
    @click="filter(status)"
    class="text-nowrap fs-14"
    :class="{'active': status.active}"
  ><span>{{ status.title }}</span></div>
</div>
</template>

<style scoped>
.statusFilter{
  border-radius: var(--border-radius);
  background-color: rgb(241, 246, 250);
  border: 1px lightgrey solid;
  max-width: fit-content;
}
.statusFilter > div{
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 0.5rem 1rem;
}
.statusFilter .active{
  border-radius: var(--border-radius);
  background-color: black;
  color: white;
}
</style>