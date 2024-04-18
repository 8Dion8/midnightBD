<template>
    <div class="card">
        <Button label="Новый Клиент" @click="visible = true" />
        <OverlayCreateClient v-model:visible="visible" />
    </div>
</template>

<script>
import Button from 'primevue/button'
import OverlayCreateClient from './OverlayCreateClient.vue'

export default {
    name: "ControlPanel",
    components: {
        OverlayCreateClient,
        Button
    },
    data() {
        return {
            visible: false
        };
    }
}
</script>
