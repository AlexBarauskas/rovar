$(document).ready(function(){
		      $('[name="action-all"]').attr('checked',null);
		      $('[name="action"]').attr('checked',null);

		      $('[name="action-all"]').change(function(){
							  if($('[name="action-all"]:checked').length)
							      $('[name="action"]').attr('checked','');
							  else
							      $('[name="action"]').attr('checked',null);
						      });
		      $('#btn-delete-seleted').click(function(){
							 var ids=$('[name="action"]:checked').map(function(){return parseInt($(this).val());}).get();
							 ids=JSON.stringify(ids);
							 window.open($('#btn-delete').attr('href')+'?ids='+ids,'this');
						     });
		  });
