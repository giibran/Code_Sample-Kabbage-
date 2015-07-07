(function(){
	angular.module('kabbageController', ['kabbageService', 'ngSanitize'])
		.controller('wikipediaController', ['$scope', 'WikipediaService', '$sce', function($scope, WikipediaService, $sce){
			WikipediaService.getWikipediaItems()
				.then(function(response){
					$scope.wikipediaFound = response.data;
				});
		}])
		.controller('twitterController', ['$scope', 'TwitterService', function($scope, TwitterService){
			TwitterService.getTwitterItems()
				.then(function(response){
					$scope.twitterFound = response.data;
				});
		}])
})();
