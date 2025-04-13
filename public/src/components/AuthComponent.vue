<template>
    <div>
        <h2>Регистрация</h2>
        <form @submit.prevent="register">
            <div>
                <label for="registerName">Имя:</label>
                <input type="text" id="registerName" v-model="registerName">
            </div>
            <div>
                <label for="registerAge">Возраст:</label>
                <input type="text" id="registerAge" v-model="registerAge">
            </div>
            <button type="submit">Зарегистрироваться</button>
        </form>

        <h2>Авторизация</h2>
        <form @submit.prevent="login">
            <div>
                <label for="loginName">Имя:</label>
                <input type="text" id="loginName" v-model="loginName">
            </div>
            <button type="submit">Авторизоваться</button>
        </form>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    name: 'AuthComponent',
    data() {
        return {
            registerName: '',
            registerAge: '',
            loginName: ''
    }
},
    methods: {
        async register() {
            const response = await axios.post('/api/users/', {
                name: this.registerName,
                age: Number(this.registerAge)
        });
    
            console.log('Register success: ' + response.data);
            this.$emit('handleAuth');
    },

        async login() {

    }
}
}
</script>
