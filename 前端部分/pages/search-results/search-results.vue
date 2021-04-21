<template>
	<view>
		{{res.id}}
	</view>
</template>

<script>
	export default {
		data() {
			return {
				res:''
			}
		},
		onLoad(res){
			uni.request({
				url: 'http://qdbwjf.com/bwydbg/api/work/pgd/getfwqx',
				method: 'POST',
				data: {
					'khsbh': '37021219740426251X01'
				},
				success: res => {
					console.log(res)
				},
				fail: () => {},
				complete: () => {}
			});
			// console.log(res)
			this.res = res
			
		},
		methods: {
			
		}
	}
</script>

<style>

</style>
