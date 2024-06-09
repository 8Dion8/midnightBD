<template>
  <Dropdown v-model="data[field]" :options="choices" />
</template>

<script>
import Dropdown from "primevue/dropdown";
export default {
  name: "TagEditor",
  data() {
    return {
      choices: [],
    };
  },
  mounted() {
    fetch(`http://127.0.0.1:7900/tables/${this.sql_table}/config/columns`)
      .then((response) => response.json())
      .then((data) => {
        console.log(data.data);
        this.choices = columnData.data[this.column_index]["possible_values"];
      })
      .catch((error) => {
        console.error("Error fetching config choices:", error);
      });
  },
  components: {
    Dropdown,
  },
  props: ["data", "field", "table", "column_index"],
};
</script>
