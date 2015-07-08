describe('Controllers tests', function(){

    describe('wikipediaController test', function(){

        var $scope,
            wikipediaController,
            WikipediaServices,
            $location;

        beforeEach(module('kabbageApp'));

        beforeEach(inject(function($rootScope, $controller){

            $scope = $rootScope.$new();
            WikipediaServices = {
                'getWikipediaItems' :function(){}
            };
            spyOn(WikipediaServices, 'getWikipediaItems');

            $location = {
                'search': function(){}
            };
            spyOn($location, 'search').and.returnValue({
                'search': 'testing value'
            });
            wikipediaController = $controller('wikipediaController', {
                '$scope': $scope,
                'WikipediaServices': WikipediaServices,
                '$location': $location
            });

        }));

        it('', function(){
            expect($location.search).toHaveBeenCalled();
        })

    });

});
