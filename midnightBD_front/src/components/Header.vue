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
                    icon: "pi pi-list-check"
                },
                {
                    label: "Склад",
                    icon: "pi pi-box"
                }
            ]
        }
    } 
}

</script>

<style>


</style>
