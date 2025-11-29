Create QueryHistory Table
```sql
USE website;
CREATE Table queryHistory(
    id int unsigned auto_increment primary key,
    inquirer_member_id int unsigned not null,
    queried_member_id int unsigned not null,
    time datetime not null default current_timestamp    
); 
```

```sql
SELECT member.name, queryhistory.inquirer_member_id, queryhistory.time FROM queryhistory JOIN member on member.id=queryhistory.inquirer_member_id WHERE queried_member_id = 12;
```