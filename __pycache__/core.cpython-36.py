3
ฌGw^  ใ               @   s`  d Z dZG dd dZedkr\edZeedjdZeefe Z	e
dd	  e
d
e d e
dd	  x๊edkrZe
dd	  e
d e
d e
d e
d e
d e
d eedZedkrึe	j  qredkr่e	j  qredkredZedZe	jee qredkr.edZe	je qredkrBe	j  qredkrPP qre
d qrW dS )a'  
create a library class
	method display books
	lend book - (who owns the book if not present) take name
	add book
	return book

HarryLibrary = Library(listofbooks, library name)

dictiionary books - nameofperson
create a main function and run an infinite while loop asking users for their input
้   c               @   sb   e Zd ZddddddgZddd	gZi Zd
d Zdd Zdd Zdd Z	dd Z
dd Zdd ZdS )ฺlibraryzPython ProrammingzJava ProgrammingzWeb designingzEnglish CommunicationZPolityzHistory of modern indiaZTejasZAnujZSandipc             G   s,   || _ t| x|D ]}| jj| qW d S )N)ฺlibrary_nameฺlistฺbooksฺappend)ฺselfr   Zlist_of_booksฺiฉ r	   ๚/root/Desktop/Project/core.pyฺ__init__   s    
zlibrary.__init__c             C   sd   t dd  t d t dd  t| j}x4ttd|d | jD ]\}}t | d|  qBW d S )N๚-้F   z+Displaying the books present in library....r   z. )ฺprintฺlenr   ฺzipฺrange)r   Znum_of_booksr   ฺbookr	   r	   r
   ฺdisplay_books   s    
 zlibrary.display_booksc             C   sd   t dd  t d t dd  t| j}x4ttd|d | jD ]\}}t | d|  qBW d S )Nr   r   z#Displaying the users of library....r   z. )r   r   ฺusersr   r   )r   Znum_of_usersr   ฺuserr	   r	   r
   ฺdisplay_users#   s    
 zlibrary.display_usersc             C   s   | j j| td d S )Nz The book donated succesfully....)r   r   r   )r   Z	book_namer	   r	   r
   ฺadd_book*   s    zlibrary.add_bookc             C   s   | j j| td d S )NzUser added successfully....)r   r   r   )r   Z	user_namer	   r	   r
   ฺadd_user-   s    zlibrary.add_userc             C   s&  d}x|dkr t d t d t d ttd}|dkrftd}|| jkrZt d n
| j| q|dkrtd	}|| jkr๘d
}| j  ttd}x6| jj D ](}| j|d  |krฆt d |d7 }P qฆW |dkr๖| j|d  | j|< t d nt d q|dkr|d7 }qt d qW d S )Nr   z1. Add userz2. lend bookz3. ExitzEnter your choice : zEnter the user's name : zThe user is already exist.....้   zEnter your user name : ้    zThis book is already owned....z%The book is borrowed successfully....zThe user is not valid...้   zInvalid choice...)	r   ฺintฺinputr   r   r   ฺdicttakeฺvaluesr   )r   ZinteZchZuser_addZ
check_userZbookingZch_bookr   r	   r	   r
   ฺ
lend_books0   s:    







zlibrary.lend_booksc             C   sz   || j krnt }x"| jj D ]\}}||kr|}qW || jkrP| j|= td qv|| jkrdtd qvtd ntd d S )Nz Returning book successfully.....zThe book is not in library....zB1. This book is not borrowed....
2. Check the name of the book....zNo such a user...)r   ฺstrr   ฺitemsr   r   )r   r   Zrt_bookZkey1ฺkeyฺvaluer	   r	   r
   ฺreturn_bookQ   s    





zlibrary.return_bookN)ฺ__name__ฺ
__module__ฺ__qualname__r   r   r   r   r   r   r   r   r    r%   r	   r	   r	   r
   r      s   
!r   ฺ__main__zEnter the name of library : z-Enter the list of books seperated by comma : z, r   r   zWelcome to z library systemz1. Display booksz2. lend booksz3. return booksz4. Donate booksz5. Display usersz6. ExitzEnter your choice : r   r   zEnter your user name : zEnter the book name : ้   ้   ้   zEnter the valid choice!!!N)ฺ__doc__Zinfir   r&   r   ฺnamer   ฺsplitZExtra_books_listฺar   r   Zchoir   r    r   r   r%   r   r   r	   r	   r	   r
   ฺ<module>   sD   M







