#projects
db.projects.name.requires = IS_NOT_EMPTY(error_message='Cannot be empty!')
db.projects.image.requires = IS_EMPTY_OR(IS_IMAGE(extensions=('jpeg', 'png', 'jpg', 'gif')))
db.projects.project_type.requires = IS_EMPTY_OR(IS_IN_SET(['OpenSource', T('Enterprising'), T('Social'), T('Other')]))
db.projects.video_url.requires = IS_EMPTY_OR(IS_URL(error_message='Must be a valid URL!'))
db.projects.slideshare_url.requires = IS_EMPTY_OR(IS_URL(error_message='Must be a valid URL!'))
db.projects.project_links.requires = IS_EMPTY_OR(IS_URL(error_message='Must be a valid URL!'))
db.projects.project_mail.requires = IS_EMPTY_OR(IS_EMAIL(error_message='Invalid e-mail!'))
db.projects.phone.requires = IS_EMPTY_OR(IS_MATCH("^(.)?(\d{2})?(.)?(.)?(\d{4})(.)?(\d{4})$",
			error_message = "Phone format: (xx) xxxx-xxxx or xxxx-xxxx or xx xxxx-xxxx or xxxxxxxx"))
db.projects.created_on.requires = IS_DATE(format=T('%Y-%m-%d'), error_message='Must be YYYY-MM-DD!')
db.projects.created_on.writable = db.projects.created_on.readable = False
db.projects.project_owner.requires = IS_IN_DB(db, 'auth_user.id', '%(username)s', zero=T('Choose one'))
db.projects.project_owner.writable = db.projects.project_owner.readable = False

#team_function
db.team_function.project_id.requires = IS_IN_DB(db, 'projects.id', '%(name)s', zero=T('Define a project that already exists.'))
db.team_function.username.requires = IS_IN_DB(db, 'auth_user.username', '%(username)s', zero=T('Define a user that already exists.'))
db.team_function.project_id.readable = db.team_function.project_id.writable = False
db.team_function.username.requires = db.team_function.role.requires = IS_NOT_EMPTY(error_message='Cannot be empty!')