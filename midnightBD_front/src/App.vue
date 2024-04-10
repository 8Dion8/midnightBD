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
    font-family: "Rubik", sans-serif;
    font-optical-sizing: auto;
    font-weight: 300;
    font-style: normal;
    background-color: #2c3e50;
    color: #ecf0f1;
    min-height: 100vh;
}
</style>
