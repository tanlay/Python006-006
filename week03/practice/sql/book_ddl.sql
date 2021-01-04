create table book (
    book_id int(11) not null auto_increment,
    type_id int(11) not null,
    book_name varchar(255) character set utf8 collate utf8_general_ci not null,
    primary key(book_id) using btree,
    engine = InnoDB character set = utf8 collate = utf8_general_ci;
)