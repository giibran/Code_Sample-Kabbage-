(function(){
	angular.module('kabbageController', ['kabbageService', 'ngSanitize'])
		.controller('wikipediaController', ['$scope', 'WikipediaService', '$sce', '$location', function($scope, WikipediaService, $sce, $location){
			var queryParams = $location.search();
			if (queryParams['search']) {
				WikipediaService.getWikipediaItems(queryParams['search'])
				.then(function(response){
					$scope.wikipediaFound = response.data;
				});
			};
		}])
		.controller('twitterController', ['$scope', 'TwitterService', '$location', function($scope, TwitterService, $location){
			var queryParams = $location.search();
			if (queryParams['search']) {
				TwitterService.getTwitterItems(queryParams['search'])
				.then(function(response){
					$scope.twitterFound = response.data;
				});
			}
		}])
})();
