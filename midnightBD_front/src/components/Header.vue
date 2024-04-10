<template>
    <div class="ui-header__wrapper">
        <h1 class="ui-header__title">Сервисная БД</h1>    
        <strong>Logged in as </strong> {{ user }}
    </div>
</template>

<script>

export default {
    name: "Header",
    data() {
        return {
            user: "dion"
        }
    } 
}

</script>

<style>

.ui-header__wrapper {
    margin: 2em;
    height: 20vh;
}

</style>
