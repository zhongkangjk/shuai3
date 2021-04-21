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
				url: 'http://',
				method: 'POST',
				data: {
					'khsbh': '***'
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
