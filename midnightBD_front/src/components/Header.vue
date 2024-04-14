<template>
    <div class="card">
        <Menubar :model="items"/> 
    </div>
</template>

<script>
import Menubar from 'primevue/menubar';
import Card from 'primevue/card';

export default {
    name: "Header",
    components: {
        Menubar,
        Card
    },
    data() {
        return {
            user: "dion",
            items: [
                {
                    label: "Заказы",
                    icon: "pi pi-list-check",
                    command: () => { this.switchTable("orders_repair") }
                },
                {
                    label: "Склад",
                    icon: "pi pi-box",
                    command: () => { this.switchTable("backstock") }
                },
                {
                    label: "Клиенты",
                    icon: "pi pi-user",
                    command: () => { this.switchTable("clients") }
                }
            ]
        }
    },
    props: {
        sql_table: {
            type: String
        }
    },
    methods: {
        switchTable(table) {
            this.$emit("switchTable", table);
        }
    }
}

</script>

<style>


</style>
