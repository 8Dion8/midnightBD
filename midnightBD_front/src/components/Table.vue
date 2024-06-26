<template>
  <div class="card maintable">
    <DataTable
      :value="data_rows"
      scrollable
      scroll-height="flex"
      v-model:selection="selected_row"
      selectionMode="single"
      v-model:editingRows="editingRows"
      editMode="row"
      @row-edit-save="onRowEditSave"
      :size="'small'"
      :rows="10"
      :rowsPerPageOptions="[5, 10, 20, 50]"
      :rowStyle="rowHeight"
      v-if="data_columns_loaded"
    >
      <template v-for="(col, i) in data_columns">
        <Column
          :field="col.field"
          :header="col.header"
          class="text-sm"
          :headerStyle="{ height: '4rem' }"
        >
          <template #body="slotProps">
            <component
              :is="getComponentType(col.display_type)"
              :display_value="slotProps.data[col.field]"
            ></component>
          </template>
          <template #editor="{ data, field }">
            <component
              :is="getComponentEditorType(col.display_type)"
              :data="data"
              :field="field"
              :table="sql_table"
              :column_index="i"
              class="w-min"
            ></component>
          </template>
        </Column>
      </template>
      <Column :rowEditor="true"></Column>
    </DataTable>
    <div v-else>
      <Skeleton class="w-full my-6" height="4rem" />
      <Skeleton class="w-full my-6" height="2rem" />
      <Skeleton class="w-full my-6" height="2rem" />
      <Skeleton class="w-full my-6" height="2rem" />
      <Skeleton class="w-full my-6" height="2rem" />
      <Skeleton class="w-full my-6" height="2rem" />
      <Skeleton class="w-full my-6" height="2rem" />
      <Skeleton class="w-full my-6" height="2rem" />
      <Skeleton class="w-full my-6" height="2rem" />
      <Skeleton class="w-full my-6" height="2rem" />
      <Skeleton class="w-full my-6" height="2rem" />
      <Skeleton class="w-full my-6" height="2rem" />
      <Skeleton class="w-full my-6" height="2rem" />
      <Skeleton class="w-full my-6" height="2rem" />
      <Skeleton class="w-full my-6" height="2rem" />
      <Skeleton class="w-full my-6" height="2rem" />
      <Skeleton class="w-full my-6" height="2rem" />
      <Skeleton class="w-full my-6" height="2rem" />
    </div>
  </div>
</template>

<script>
import DataTable from "primevue/datatable";
import Column from "primevue/column";
import ColumnGroup from "primevue/columngroup";
import Row from "primevue/row";
import Skeleton from "primevue/skeleton";
import InputText from "primevue/inputtext";

import TagCell from "./tableCellComponents/TagCell.vue";
import DefaultCell from "./tableCellComponents/DefaultCell.vue";
import CurrencyCell from "./tableCellComponents/CurrencyCell.vue";
import CPUCell from "./tableCellComponents/CPUCell.vue";
import GPUCell from "./tableCellComponents/GPUCell.vue";

import DefaultEditor from "./tableCellEditors/DefaultEditor.vue";
import TagEditor from "./tableCellEditors/TagEditor.vue";

export default {
  name: "Table",
  data() {
    return {
      data_columns: [],
      data_columns_loaded: false,
      data_rows: [],
      data_rows_loaded: false,
      selected_row: null,
      editingRows: [],
    };
  },
  props: {
    sql_table: {
      type: String,
    },
    selected_row_id: {
      type: Number,
    },
  },
  components: {
    DataTable,
    Column,
    ColumnGroup,
    Row,
    Skeleton,
    InputText,
    TagCell,
    DefaultCell,
    CurrencyCell,
    CPUCell,
    GPUCell,
    DefaultEditor,
    TagEditor,
  },

  mounted() {
    this.fetchColumns();
    this.fetchRows();
  },

  methods: {
    fetchColumns() {
      this.data_columns_loaded = false;
      fetch(`http://127.0.0.1:7900/tables/${this.sql_table}/columns`)
        .then((response) => response.json())
        .then((columnData) => {
          console.log(columnData.data);
          this.data_columns = columnData.data;
          this.data_columns_loaded = true;
        })
        .catch((error) => {
          console.error("Error fetching column data:", error);
        });
    },
    fetchRows() {
      this.data_rows_loaded = false;
      fetch(`http://127.0.0.1:7900/tables/${this.sql_table}/rows`)
        .then((response) => response.json())
        .then((rowData) => {
          console.log(rowData.data);
          this.data_rows = rowData.data;
          this.data_rows_loaded = true;
        })
        .catch((error) => {
          console.error("Error fetching row data:", error);
        });
    },

    getComponentType(type) {
      const typeToComponentMap = {
        tag: "TagCell",
        currency: "CurrencyCell",
        cpu: "CPUCell",
        gpu: "GPUCell",
      };
      return typeToComponentMap[type] || "DefaultCell";
    },

    getComponentEditorType(type) {
      const typeToEditorMap = {
        tag: "TagEditor",
      };
      return typeToEditorMap[type] || "DefaultEditor";
    },

    switchRowID(id) {
      this.$emit("switchRowID", id);
    },

    onRowEditSave(event) {
      let { newData, index } = event;
      console.log(newData);
      fetch(`http://127.0.0.1:7900/tables/${this.sql_table}/rows`, {
        method: "PATCH",
        headers: {
          "Content-type": "application/json",
        },
        body: JSON.stringify({
          data: newData,
        }),
      })
        .then((response) => response.json())
        .then((json) => console.log(json))
        .then(() => window.location.reload());
    },
    rowHeight() {
      return { height: "3rem", "max-height": "3rem" };
    },
  },

  watch: {
    sql_table(newTable, oldTable) {
      console.log("watcher", oldTable, newTable);
      this.fetchColumns();
      this.fetchRows();
    },
    selected_row(newRow, oldRow) {
      if (newRow != null) {
        console.log(newRow.id);
        this.switchRowID(newRow.id);
      }
    },
  },
};
</script>

<style>
.p-icon-field {
  margin: 1rem;
}
</style>
