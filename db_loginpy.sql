use login_python;

create table if not exists users(
	username varchar(40) not null,
    password varchar(50) not null,
    firstname varchar(40) not null,
    lastname varchar(40),
    primary key (username)
);

insert into users
values("admin", "admin", "The", "Admin")


