angular.module("yet2Download", []).controller(
			'downloadThem',
			function downloadThem($scope, $http) {
				var loc = window.location.href;
				var re = /^(.*)\/logbackup/;
				var vals = re.exec(loc);
				$http.get(vals[0] + '/getDownloadableLogs').success(
						function process(resp) {
							$scope.fileList = resp.files;
						}
				);
			}
);

