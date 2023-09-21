// import createFormLinks from './updateFormLinks';

class linkListe{

    constructor(){
        this.LinkInBioLinksListView = document.querySelector('#LinkInBioLinksListView');
        this.cardContainer = document.querySelector('#card-container');
        this.loaderImage = document.querySelector('.loader-image');
        
        this.linklistview();
    }

    events(){}

    renderCard(link) {
        return `
            <div class="card border-0 shadow-sm mb-3 sortable-grabel">
                <div class="card-body">
                    <div class="row" id="linkInBioCardForm${link.id}">
                        <div class="col-1">
                            <div class="d-flex mb-3 linkin-bio-hover align-items-center h-100">
                                <i class="fa-solid fa-grip-vertical"></i>
                            </div>
                        </div>
                        <div class="col-11">
                            <div class="d-flex align-items-center justify-content-between">
                                <h5 class="mb-0">${link.button_label}</h5>
                                <button type="button" class="btn btn-primary btn-sm linkinbio-editcard" data-linkinbio-editcard="${link.id}"><i class="fa-solid fa-pen"></i></button>
                            </div>
                            <div class="d-flex mt-3">
                                <a class="linkinbio" href="${link.url_destination}" target="_blank">${link.url_destination}</a>
                            </div>
                            <div class="d-flex justify-content-between align-items-center mt-3">
                                <div class="d-flex align-items-center">
                                    <i class="fa-solid fa-chart-line linkinbio-icon"></i>
                                    <small class="mx-2 textsmall">1</small>
                                </div>
                                <div class="form-check form-switch">
                                    <input class="form-check-input linkinbio-switch" data-linkinbio-switch="${link.id}" type="checkbox" role="switch" id="flexSwitchCheckDefault">
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="row d-none" id="linkInBioCardAddForm${link.id}">
                        <div class="col-12">
                            <div class="mb-3">
                                <label for="cratedhortcode" class="form-label">Button Label</label>
                                <input type="text" class="form-control mb-3" id="button_label" placeholder="Button label">
                                <div class="bg-linkinbio-edit-field d-flex justify-content-start align-items-baseline rounded">
                                    <a class="btn btn-light form-place" data-form-place="${link.id}" href="javascript:void(0);">Replace link</a>
                                </div>

                                <!--Neuer Link Form-->
                                <div class="linkinbio-form-place${link.id}"></div>
                                <!-- /. Neuer Link Form-->
                                
                                <button type="submit" id="cancel${link.id}" class="btn btn-secondary btn-sm mt-3 cencleButton">Abbrechen</button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        `;
    }

    // ListViewLinks
    linklistview(){
        if(this.LinkInBioLinksListView){
            $.ajax({
                url: this.LinkInBioLinksListView.value,
                type: 'GET',
                dataType: 'json',
                success: (data) => {
    
                // empty list
                $(this.cardContainer).empty();
                this.loaderImage.classList.remove('d-none');
    
                    // Date
                    setTimeout(() => {
                        for (var i = 0; i < data.links.length; i++) {
                            var link = data.links[i];
                            var card = this.renderCard(link);
                            $(this.cardContainer).append($(card));
                            // this.createformlinks.insiteFormular(); 
                        }
                        $(this.loaderImage.classList.add('d-none'));
                    }, 1000);
    
                },
                error: (xhr, textStatus, errorThrown) => {
                console.error('Fehler:', errorThrown);
                }
            });
        }

    }

}

export default linkListe
