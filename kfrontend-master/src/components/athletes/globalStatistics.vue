<script setup>
import GlobalStatisticsForm from "@/components/athletes/partials/globalStatisticsForm.vue";
import Statistics from "@/components/athletes/partials/statistics.vue";
import { ref } from "vue";

const url = ref("competitions/results?");
const penalizationUrl = ref("penalizations?skip=0&limit=-1");
const before2024 = ref(false);

const updateUrl = async (competitions, year) => {
	let urlBuilder = "competitions/results?";
	let urlPenalizationsBuilder = "penalizations?";
	for (const competition of competitions) {
		console.log(competition.name);
		if (competition.selected) {
			urlBuilder += `competition_ids=${competition.id}&`;
			urlPenalizationsBuilder += `competition_ids=${competition.id}&`;
		}
	}
	urlPenalizationsBuilder += "skip=0&limit=-1";
	url.value = urlBuilder.slice(0, urlBuilder.length - 1);
	penalizationUrl.value = `${urlPenalizationsBuilder}skip=0&limit=-1`;
	before2024.value = year < 2024;
};
</script>

<template>
	<GlobalStatisticsForm @update-statistics="updateUrl" />
	<Statistics
		:url="url"
		:penalizationUrl="penalizationUrl"
		:showPenalizationForm="false"
		:before2024="before2024"
		:immediate="false" />
</template>
