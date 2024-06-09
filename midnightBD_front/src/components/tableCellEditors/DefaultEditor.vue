<template>
  <InputText v-model="data[field]" />
</template>

<script>
import InputText from "primevue/inputtext";
export default {
  name: "DefaultEditor",
  components: {
    InputText,
  },
  mounted() {
    console.log(this.data, this.field);
  },
  props: ["data", "field", "table", "column_index"],
};
</script>
