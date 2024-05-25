<template>
  <div class="main-container flex flex-row h-[97vh] p-1 m-4 space-x-6">
    <div class="table-container w-3/4 h-full">
      <Table
        :sql_table="sql_table"
        :selected_row_id="1"
        @switchRowID="switchRowID"
        class="h-full"
      />
    </div>

    <div class="sidepanel-container flex flex-col w-1/4">
      <div class="header-container">
        <Header :sql_table="sql_table" @switchTable="switchTable" />
      </div>

      <div class="controls-container flex justify-center w-full">
        <ControlPanel />
      </div>

      <div class="details-container h-full">
        <Details
          class="h-full"
          :selected_row_id="selected_row_id"
          :sql_table="sql_table"
        />
      </div>
    </div>
  </div>
</template>

<script>
import Header from "./Header.vue";
import Table from "./Table.vue";
import ControlPanel from "./ControlPanel.vue";
import Details from "./Details.vue";

export default {
  name: "MainUI",
  components: {
    Header,
    Table,
    ControlPanel,
    Details,
  },
  data() {
    return {
      sql_table: "clients",
      selected_row_id: 1,
    };
  },
  methods: {
    switchTable(table) {
      console.log("switching", table);
      this.sql_table = table;
    },
    switchRowID(id) {
      console.log("switching id", id);
      this.selected_row_id = id;
    },
  },
};
</script>

<style></style>
