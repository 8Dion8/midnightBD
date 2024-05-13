<template>
    <div class="h-svh">
        <div class="header-container p-1">
            <Header :sql_table="sql_table" @switchTable="switchTable"/>
        </div>
        <div class="controls-container p-1">
            <ControlPanel />
        </div>
        <div class="main-container flex flex-row h-full p-1 space-x-6">
            <div class="table-container w-2/3 h-full">
                <Table :sql_table="sql_table" :selected_row_id="1" @switchRowID="switchRowID" class="h-full"/>
            </div>
            <div class="details-container w-1/3 h-full">
                <Details class="h-full"/>
            </div>
        </div>
    </div>
</template>

<script>

import Header from "./Header.vue"
import Table from "./Table.vue"
import ControlPanel from "./ControlPanel.vue"
import Details from "./Details.vue"

export default {
    name: "MainUI",
    components: {
        Header,
        Table,
        ControlPanel,
        Details
    },
    data() {
        return {
            sql_table: "clients",
            selected_row_id: 1
        }
    },
    methods: {
        switchTable(table) {
            console.log("switching", table)
            this.sql_table = table
        },
        switchRowID(id) {
            console.log("switching id", id)
            this.selected_row_id = id
        }
    }
}
</script>

<style>
table-container, .details-container {
    padding:
}

</style>
