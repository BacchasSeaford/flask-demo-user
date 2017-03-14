create table user_profile(id serial,username text,firstname text,lastname text,age int,gender text,biography text,file text,date_created date,primary key (username));
Grant All privileges on table user_profile to public;
grant usage, select on sequence user_profile_id_seq to project1;