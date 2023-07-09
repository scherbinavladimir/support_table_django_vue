<script setup>
/* eslint-disable */
import {nextTick, onBeforeMount, ref, watchEffect} from "vue";
import vClickout from 'vue3-clickout';

const props = defineProps({
  modelValue: {
    type: String,
  }
})
const emit = defineEmits(['update:modelValue'])

const show = ref(false)
const searchInput = ref(null)

watchEffect(()=>{
  if (show && searchInput.value){
    nextTick(()=>searchInput.value.focus())
  }
})
</script>

<template>
<div v-clickout="()=>show=false" class="position-relative">
  <div @click="show=!show" class="searchBtn text-nowrap fs-14"><span><slot></slot></span>
  </div>
  <div class="searchPopup" v-if="show">
    <input
      ref="searchInput"
      type="text"
      :value="modelValue"
      @input="emit('update:modelValue', $event.target.value)"
    >
    <div @click="show=false"><i class="bi bi-search"></i></div>
  </div>

</div>
</template>


<style scoped>
.searchBtn{
  background-color: black;
  color: white;
  border-radius: var(--border-radius);
  padding: 0.5rem 1rem;
  position: relative;
}
.searchPopup{
  position: absolute;
  z-index: 10;
  background-color: white;
  border-radius: var(--border-radius);
  border: 1px lightgrey solid;
  top: 45px;
  right: 0;
  height: 40px;
  width: 250px;
  display: flex;
}
.searchPopup input{
  flex-grow: 1;
  height: 100%;
  margin-left: 0.5rem;
}
.searchPopup > div{
  height: 100%;
  border-radius: var(--border-radius);
  padding: 0.5rem 1rem;
  background-color: black;
  color: white;
}
</style>