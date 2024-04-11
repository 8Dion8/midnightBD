<template>
    <div class="card flex">
        <DataTable 
        :value="data_rows"
        tableStyle="min-width: 50rem"
        paginator
        :rows="10"
        :rowsPerPageOptions="[5, 10, 20, 50]"
        v-if="data_columns_loaded">
        <template v-for="(col, index) in data_columns">
            <Column :field="col.field" :header="col.header">
                <template #body="slotProps">
                    <component :is="getComponentType(col.display_type)" :rowData="slotProps.data" :rowIndexToGet="col.field"/>
                </template>
            </Column>
        </template>
            
        </DataTable>
    </div>
</template>
 
<script>

import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import ColumnGroup from 'primevue/columngroup';
import Row from 'primevue/row';
import Skeleton from 'primevue/skeleton';

import TagCell from './tableCellComponents/TagCell.vue'
import DefaultCell from './tableCellComponents/DefaultCell.vue'

export default {
    name: "Table",
    data() {
        return {
            data_columns: [],
            data_columns_loaded: false,
            data_rows: [],
            data_rows_loaded: false,
        };
    },
    components: {
        DataTable,
        Column,
        ColumnGroup,
        Row,
        Skeleton,
        TagCell,
        DefaultCell
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
                    this.data_columns = columnData.data;
                    this.data_columns_loaded = true;
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
                    this.data_rows = rowData.data;
                    this.data_rows_loaded = true;
                })
            .catch(error => {
                console.error("Error fetching row data:", error)
            })
        },

        getComponentType(type) {
            const typeToComponentMap = {
                tag: 'TagCell'

            };
            return typeToComponentMap[type] || 'DefaultCell';
        }

    }

    
};
</script>

<style>

</style>
