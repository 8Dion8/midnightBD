<template>
    <div class="card flex">
        <DataTable 
        :value="data_rows"
        tableStyle="min-width: 50rem"
        paginator
        :rows="10"
        :rowsPerPageOptions="[5, 10, 20, 50]">

            <Column 
            v-for="col of data_columns"
            :key="col.field"
            :field="col.field" 
            :header="col.header"
            />

        </DataTable>
    </div>
</template>
 
<script>

import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import ColumnGroup from 'primevue/columngroup';
import Row from 'primevue/row';

export default {
    name: "Table",
    data() {
        return {
            data_columns: [],
            data_rows: [],
        };
    },
    components: {
        DataTable,
        Column,
        ColumnGroup,
        Row
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
                    this.data_columns = columnData.data
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
                    this.data_rows = rowData.data
                })
            .catch(error => {
                console.error("Error fetching row data:", error)
            })
        }

    }

    
};
</script>

<style>

</style>
