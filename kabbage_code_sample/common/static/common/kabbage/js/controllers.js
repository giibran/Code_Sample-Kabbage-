(function(){
	angular.module('kabbageController', ['kabbageService'])
		.controller('wikipediaController', ['$scope', 'WikipediaService', function($scope, WikipediaService){
			WikipediaService.getWikipediaItems()
				.then(function(response){
					$scope.wikipediaFound = response.data;
				});
		}]);
})();
