<template>
	<view>
		<view class="content">
			<!-- 搜索栏 -->
			<uni-search-bar :radius="100" @confirm="search" @input="input" />
		</view>
		<view class="kongge">

		</view>
		<view class="button-sp-area">
			<button type="primary" @click="serviceRestart('restart')">重启服务</button>
		</view>

	</view>
</template>

<script>
	import uniSearchBar from '@/components/uni-search-bar/uni-search-bar.vue'
	export default {
		data() {
			return {
				title: 'Hello',
			}
		},
		onLoad() {

		},
		//监听搜索框点击事件

		methods: {
			search(res) {
				console.log(res.value)
				uni.navigateTo({

					url: "../search-results/search-results?id=" + res.value,


				})
			},
			serviceRestart(e) {
				uni.showLoading({
					title: '加载中',
					mask: true
				});
				uni.request({
					url: 'http://test/',
					method: 'POST',
					header: {
						'content-type': 'application/x-www-form-urlencoded' //自定义请求头信息
					},
					data: {
						'command': e,
					},
					success: (res) => {
						// console.log(res.data);
						if (res.data.msg == "success") {
							setTimeout(() => {
								// 服务端响应的 message 提示
								uni.showToast({
									title: "重启成功",
									icon: "none",
									position: 'bottom'
								})
								//延时关闭  加载中的 loading框
								uni.hideLoading()
							}, 2000)
							return;
						}
					},
					fail:() =>{
						setTimeout(() => {
							// 服务端响应的 message 提示
							uni.showToast({
								title: "连接失败",
								icon: "none",
								position: 'bottom'
							})
							//延时关闭  加载中的 loading框
							uni.hideLoading()
						}, 2000)
					}
				});
			}
		},
		components: {
			uniSearchBar
		}
	}
</script>

<style>
	.content {
		display: flex;
		flex-direction: column;
		justify-content: center;
	}

	.logo {
		height: 200rpx;
		width: 200rpx;
		margin-top: 200rpx;
		margin-left: auto;
		margin-right: auto;
		margin-bottom: 50rpx;
	}

	.text-area {
		display: flex;
		justify-content: center;
	}

	.title {
		font-size: 36rpx;
		color: #8f8f94;
	}

	.button-sp-area {
		margin: 0 auto;
		width: 60%;
		/* height: 50%; */
	}

	.kongge {
		min-height: 350rpx;
	}
</style>
