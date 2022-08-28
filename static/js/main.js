$(document).ready(function(){
    $('button').click(function(){
        let $sights = $('#content');
        let zone = $(this).text();
        $.ajax({
            method: 'GET',
            url: '/SightAPI?zone=' + zone,
            success: function(sights){
                $sights.html("");
                $.each(sights, function(i, sight){
                    let cardDisplay = $("<div></div>").attr("id", "card-display");

                    let card = $("<div></div>").addClass("card");
                    let header = $("<div></div>").addClass("card-header").text(sight.sightName);
                    let body = $("<div></div>").addClass("card-body");
                    let bodyContent = $("<p></p>");
                    bodyContent.append(`地區：${sight.zone}`, "<br>", `分類：${sight.category}`);
                    let address = $("<a></a>").addClass("btn btn-primary")
                                              .attr("id", "address_button")
                                              .attr("href", `https://www.google.com.tw/maps/place/${sight.address}`)
                                              .attr("target", "_blank")
                                              .text("地址");

                    let descriptionCard = $("<div></div>").addClass("card");
                    let descriptionHeader = $("<div></div>").addClass("card-header");
                    let photo = $("<img>").attr("src", sight.photoURL);
                    let descriptionTitle = $("<a></a>").addClass("btn")
                                                       .attr("data-bs-toggle", "collapse")
                                                       .attr("href", `#collapse${i}`)
                                                       .text("詳細資訊");
                    descriptionHeader.append(descriptionTitle);

                    let descriptionCollapse = $("<div></div>").addClass("collapse")
                                                              .attr("id", `collapse${i}`);
                    let descriptionBody = $("<div></div>").addClass("card-body")
                                                          .text(sight.description);
                    if(sight.photoURL != "") descriptionCollapse.append(photo, descriptionBody);
                    else descriptionCollapse.append(descriptionBody);
                    descriptionCard.append(descriptionHeader, descriptionCollapse);

                    body.append(address, bodyContent);
                    card.append(header, body);
                    cardDisplay.append(card, descriptionCard);
                    $sights.append(cardDisplay);
                });
            }
        });
    });
})