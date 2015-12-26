import Relational from 'backbone-relational';
import MarionetteForms from 'marionette.forms';

let BaseModel = Backbone.RelationalModel.extend(MarionetteForms.FormModelMixin);

export default BaseModel;
