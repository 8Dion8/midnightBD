<script>
import MainUI from "./components/MainUI.vue"

export default {
    name: 'App',
    components: { MainUI }
}
</script>

<template>
    <div id="app__wrapper">
        <MainUI/>
    </div>
</template>

<style>
@import url('https://fonts.googleapis.com/css2?family=Rubik:ital,wght@0,300..900;1,300..900&display=swap');

body {
    min-height: 100vh;
}
</style>
