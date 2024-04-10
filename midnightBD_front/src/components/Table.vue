<template>
    <v-grid
      theme="compact"
      :source="rows"
      :columns="columns"
      :resize="true"
      :autoSizeColumn="autoSizeColumn"
    ></v-grid>
</template>
 
<script>

import VGrid from "@revolist/vue3-datagrid";

export default {
    name: "Table",
    data() {
        return {
            columns: [],
            rows: [],
            autoSizeColumn: {
                mode: 'autoSizeOnTextOverlap'
            }
        };
    },
    components: {
        VGrid,
    },

    mounted() {
        this.fetchColumns()
        this.fetchRows()
    },

    methods: {
        fetchColumns() {
            fetch("http://127.0.0.1:7900/fetch/data_column_names?table=clients")
                .then(response => response.json())
                .then(columnData => {
                    console.log(columnData.data)
                    this.columns = columnData.data
                })
            .catch(error => {
                console.error("Error fetching column data:", error)
            })
        },
        fetchRows() {
            fetch("http://127.0.0.1:7900/fetch/data_rows?table=clients")
                .then(response => response.json())
                .then(rowData => {
                    console.log(rowData.data)
                    this.rows = rowData.data
                })
            .catch(error => {
                console.error("Error fetching row data:", error)
            })
        }

    }

    
};
</script>

<style>

revo-grid {
    height: 80vh;
    width: 100vw;
}

</style>
