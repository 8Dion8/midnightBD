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
      <Column
        :field="'id'"
        :header="'ID'"
        class="text-sm"
        :headerStyle="{ height: '4rem' }"
      >
        <DefaultCell :display_value="row.id"></DefaultCell>
      </Column>
      <Column
        :field="'client'"
        :header="'Клиент'"
        class="text-sm"
        :headerStyle="{ height: '4rem' }"
      >
        <DefaultCell :display_value="row.client"></DefaultCell>
      </Column>
      <Column
        :field="'cpu'"
        :header="'CPU'"
        class="text-sm"
        :headerStyle="{ height: '4rem' }"
      >
        <template #body="slotProps">
          <CPUCell :display_value="slotProps.data.cpu"></CPUCell>
        </template>
      </Column>
      <Column
        :field="'gpu'"
        :header="'GPU'"
        class="text-sm"
        :headerStyle="{ height: '4rem' }"
      >
        <template #body="slotProps">
          <GPUCell :display_value="slotProps.data.gpu"></GPUCell>
        </template>
      </Column>
      <Column
        :field="'motherboard'"
        :header="'Материнская плата'"
        class="text-sm"
        :headerStyle="{ height: '4rem' }"
      >
        <DefaultCell :display_value="row.motherboard"></DefaultCell>
      </Column>
      <Column
        :field="'ram'"
        :header="'Оперативная Память'"
        class="text-sm"
        :headerStyle="{ height: '4rem' }"
      >
        <DefaultCell :display_value="row.ram"></DefaultCell>
      </Column>
      <Column
        :field="'psu'"
        :header="'Блок питания'"
        class="text-sm"
        :headerStyle="{ height: '4rem' }"
      >
        <DefaultCell :display_value="row.psu"></DefaultCell>
      </Column>
      <Column
        :field="'pc_case'"
        :header="'Корпус'"
        class="text-sm"
        :headerStyle="{ height: '4rem' }"
      >
        <DefaultCell :display_value="row.pc_case"></DefaultCell>
      </Column>
      <Column
        :field="'cpu_cooler'"
        :header="'Кулер'"
        class="text-sm"
        :headerStyle="{ height: '4rem' }"
      >
        <DefaultCell :display_value="row.cpu_cooler"></DefaultCell>
      </Column>
      <Column
        :field="'fans'"
        :header="'Вертушки'"
        class="text-sm"
        :headerStyle="{ height: '4rem' }"
      >
        <DefaultCell :display_value="row.fans"></DefaultCell>
      </Column>
      <Column
        :field="'date_of_entry'"
        :header="'Дата Приёма Заказа'"
        class="text-sm"
        :headerStyle="{ height: '4rem' }"
      >
        <DefaultCell :display_value="row.date_of_entry"></DefaultCell>
      </Column>
      <Column
        :field="'date_of_finish'"
        :header="'Дата Выполнения Заказа'"
        class="text-sm"
        :headerStyle="{ height: '4rem' }"
      >
        <DefaultCell :display_value="row.date_of_finish"></DefaultCell>
      </Column>
      <Column
        :field="'job_price'"
        :header="'Стоимость Заказа'"
        class="text-sm"
        :headerStyle="{ height: '4rem' }"
      >
        <CurrencyCell :display_value="row.job_price"></CurrencyCell>
      </Column>
      <Column
        :field="'status'"
        :header="'Статус Заказа'"
        class="text-sm"
        :headerStyle="{ height: '4rem' }"
      >
        <template #body="slotProps">
          <TagCell :display_value="slotProps.data.status"></TagCell>
        </template>
      </Column>

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
      fetch(`http://127.0.0.1:7900/tables/orders_build/columns`)
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
      fetch(`http://127.0.0.1:7900/tables/orders_build/rows`)
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
