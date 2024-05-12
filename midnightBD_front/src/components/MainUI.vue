<template>
    <div>
        <Header :sql_table="sql_table" @switchTable="switchTable"/>
        <ControlPanel />
        <div class="main-container">
            <Table  :sql_table="sql_table" :selected_row_id="1" @switchRowID="switchRowID"/>
            <Details/>
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

</style>
