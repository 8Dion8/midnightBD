<template>
    <div class="card maintable">
        <DataTable 
        :value="data_rows"
        showGridLines
        scrollable
        v-model:selection="selected_row"
        selectionMode="single"
        :size="small"
        :rows="10"
        :rowsPerPageOptions="[5, 10, 20, 50]"
        v-if="data_columns_loaded">
        <template v-for="(col, index) in data_columns">
            <Column :field="col.field" :header="col.header">
                <template #body="slotProps">
                    <component 
                    :is="getComponentType(col.display_type)" 
                    :display_value="slotProps.data[col.field]"/>
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
import CurrencyCell from './tableCellComponents/CurrencyCell.vue'


export default {
    name: "Table",
    data() {
        return {
            data_columns: [],
            data_columns_loaded: false,
            data_rows: [],
            data_rows_loaded: false,
            selected_row: null
        };
    },
    props: {
        sql_table: {
            type: String
        },
        selected_row_id: {
            type: Number
        }
    },
    components: {
        DataTable,
        Column,
        ColumnGroup,
        Row,
        Skeleton,
        TagCell,
        DefaultCell,
        CurrencyCell,
    },

    mounted() {
        this.fetchColumns()
        this.fetchRows()
    },

    methods: {
        fetchColumns() {
            fetch(`http://127.0.0.1:7900/${this.sql_table}/columns`)
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
            fetch(`http://127.0.0.1:7900/${this.sql_table}/rows`)
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
                tag: 'TagCell',
                currency: 'CurrencyCell'

            };
            return typeToComponentMap[type] || 'DefaultCell';
        },

        switchRowID(id) {
            this.$emit("switchRowID", id)
        }

    },

    watch: {
        sql_table(newTable, oldTable) {
            console.log("watcher", oldTable, newTable)
            this.fetchColumns()
            this.fetchRows()
        },
        selected_row(newRow, oldRow) {
            if (newRow != null) {
                console.log(newRow.id)
                this.switchRowID(newRow.id)
            }
        }
    }

    
};
</script>

<style>
.p-icon-field {
    margin: 1rem;
}

</style>
