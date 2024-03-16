<template>
  <div class="grid max-w-screen-xl px-4 py-8 mx-auto lg:gap-8 xl:gap-0 lg:py-16 lg:grid-cols-12">
    <div class="lg:col-span-6">
      <h1>SAC PRICE Simulator</h1>
      <form @submit.prevent="submitForm" class="max-w-sm mt-52">
        <div class="mb-5">
          <label for="loan" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Loan:</label>
          <input type="number" id="loan" v-model="loan"
            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
            required>
        </div>
        <div class="mb-5">
          <label for="installments_number"
            class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Installments Number:</label>
          <input type="number" id="installments_number" v-model="installments_number"
            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
            required>
        </div>
        <div class="mb-5">
          <label for="interest" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Interest:</label>
          <input type="number" step="0.01" id="interest" v-model="interest"
            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
            required>
        </div>
        <div class="mb-5">
          <button type="submit"
            class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Simulate</button>
        </div>
      </form>
    </div>
    <div class="lg:mt-52 lg:col-span-6 lg:flex">
      <canvas id="amortizationChart"></canvas>
    </div>
    <div v-if="data" class="lg:col-span-12 flex gap-24 mt-16">
      <div>
        <h1>Sac Table</h1>
        <table class="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400">
          <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
            <tr>
              <th scope="col" class="px-6 py-3">Installments Number</th>
              <th scope="col" class="px-6 py-3">Installment</th>
              <th scope="col" class="px-6 py-3">Interest</th>
              <th scope="col" class="px-6 py-3">Amortization</th>
              <th scope="col" class="px-6 py-3">Balance Due</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="item in data.sac" :key="item.installments_number"
              class="bg-white border-b dark:bg-gray-800 dark:border-gray-700">
              <td scope="row" class="px-6 py-4">{{ item.installments_number }}</td>
              <td scope="row" class="px-6 py-4">{{ item.installment }}</td>
              <td scope="row" class="px-6 py-4">{{ item.interest }}</td>
              <td scope="row" class="px-6 py-4">{{ item.amortization }}</td>
              <td scope="row" class="px-6 py-4">{{ item.balance_due }}</td>
            </tr>
          </tbody>
        </table>
      </div>
      <div>
        <h1>Price Table</h1>
        <table class="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400">
          <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
            <tr>
              <th scope="col" class="px-6 py-3">Installments Number</th>
              <th scope="col" class="px-6 py-3">Installment</th>
              <th scope="col" class="px-6 py-3">Interest</th>
              <th scope="col" class="px-6 py-3">Amortization</th>
              <th scope="col" class="px-6 py-3">Balance Due</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="item in data.price" :key="item.installments_number"
              class="bg-white border-b dark:bg-gray-800 dark:border-gray-700">
              <td scope="row" class="px-6 py-4">{{ item.installments_number }}</td>
              <td scope="row" class="px-6 py-4">{{ item.installment }}</td>
              <td scope="row" class="px-6 py-4">{{ item.interest }}</td>
              <td scope="row" class="px-6 py-4">{{ item.amortization }}</td>
              <td scope="row" class="px-6 py-4">{{ item.balance_due }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import Chart from 'chart.js/auto';
import axios from 'axios';

export default {
  data() {
    return {
      loan: null,
      installments_number: null,
      interest: null,
      data: null,
      chart: null
    };
  },
  methods: {
    submitForm() {
      axios.post('http://localhost:8000/api/sacprice/', {
        loan: this.loan,
        installments_number: this.installments_number,
        interest: this.interest
      }).then((response) => {
        this.data = response.data;
        this.displayChart(this.data);
      }).catch((error) => {
        console.log(error);
      });
    },
    displayChart(data) {
      if (!this.chart) {
        console.log(data);
        const ctx = document.getElementById('amortizationChart').getContext('2d');
        this.chart = new Chart(ctx, {
          type: 'line',
          data: {
            labels: data.sac.map(item => item.installments_number),
            datasets: [{
              label: 'SAC',
              data: data.sac.map(item => item.amortization),
              borderColor: 'rgb(75, 192, 192)',
              tension: 0.1,
            },
            {
              label: 'PRICE',
              data: data.price.map(item => item.amortization),
              borderColor: 'rgb(75, 192, 55)',
              tension: 0.1,
            }
            ]
          },
          options: {
            scales: {
              x: {
                title: {
                  display: true,
                  text: 'Month'
                }
              },
              y: {
                title: {
                  display: true,
                  text: 'Amortization'
                }
              }
            }
          }
        });
      }
    }

  }
};
</script>