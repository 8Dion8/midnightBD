<template>
    <div>
        <Header :sql_table="sql_table" @switchTable="switchTable"/>
        <Table  :sql_table="sql_table"/>
    </div>
</template>

<script>

import Header from "./Header.vue"
import Table from "./Table.vue"

export default {
    name: "MainUI",
    components: {
        Header,
        Table
    },
    data() {
        return {
            sql_table: "clients"
        }
    },
    methods: {
        switchTable(table) {
            console.log("switching", table)
            this.sql_table = table
        }
    }
}
</script>


