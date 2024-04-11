<template>
    <div>
        <Header/>
        <Table/>
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
    }
}
</script>


