<script setup>
/* eslint-disable */
import {nextTick, onBeforeMount, onMounted, ref, watchEffect} from "vue";
import vClickout from 'vue3-clickout';

const props = defineProps({
  fields: {
    type: Array,
  }
})
const emit = defineEmits(['select'])

const show = ref(false)

</script>

<template>
<div v-clickout="()=>show=false" class="position-relative">
  <div  @click="show=!show" class="selectBtn fs-14"><i class="bi bi-funnel"></i>
  </div>
  <div class="selectPopup" v-if="show">
    <div class="my-2" v-for="field in fields.filter(c=>c.key !== 'id')">
      <label class="ms-2">
      <input
          type="checkbox"
          :checked="field.selected"
          @input="emit('select', field.key, $event.target.checked)"
      >
      {{ field.name }}
      </label>
    </div>
  </div>

</div>
</template>


<style scoped>
.selectBtn{
  border-radius: var(--border-radius);
  border: 1px lightgrey solid;
  padding: 0.5rem 1rem;
  position: relative;
  height: 32px;
}
.selectPopup{
  position: absolute;
  z-index: 10;
  background-color: white;
  border-radius: var(--border-radius);
  border: 1px lightgrey solid;
  top: 45px;
  right: 0;
  /*width: 250px;*/
  width: max-content;
  padding: 0.5rem;
}

</style>