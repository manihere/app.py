$version=$PSVersionTable.PSVersion #to check powershell version

Write-Host $version

Get-ExecutionPolicy

#Set-ExecutionPolicy RemoteSigned

Get-ExecutionPolicy

Write-Host "Hello World"

Write-Host "No New Line" -nonewline #pointer does not move to new line after execution

#Get-Command : Prints all available commands in PS, with module name and version

Get-Help Write-Host -Full #get all help related to a command here it's write-host

#Command1 | Command 2 : To provide Command 1 output as input for Command 2. eg:

"Hello" | Out-File Hello.txt #prints Hello into hello.txt file

$FavChar = "Batman" #decalare and initialize variable

$FavChar #printVariable

$FavChar | Out-File favchar.txt

$FavChar.GetType() #will show datatype as string

$FavChar = 5 #int32 type

$FavChar.GetType() #now shows as int32

$x = 4; $y = 5; $z = $x + $y;

$z #prints 9

$newfav = "manbat"

#$x + $newfav #exception as you are adding num with string

# Cannot convert value "manbat" to type "System.Int32". Error: "Input string was not in a correct format."

$newfav.Length

$newfav | Select-Object -Property * #list all property of this var. String datatype has only one property i.e. length

Get-Member -InputObject $newfav #displays all functions that can be applied to this var eg. toUpper, toLower for string etc

#-------Arrays------------#
$listofchars = ('A','B','C','D')
$listofchars.GetType() # Array type
$listofchars[0].Length #length of a particular value in array here 1
$listofchars += 'E'; $listofchars #adds E to end of array


#-------------HASHTABLES----------#
$Fellowship = @{key1="value1";key2 = "value2"} #@ is required here to make it hashtable i.e. array of key pair 
$Fellowship
$Fellowship.Add("key3","value3") #you can only add one key-pair at a time to a hashtable
$Fellowship.Add("key4","value4") 
$Fellowship #add function may not add always in order, use [ordered]@ to declare ordered hashtable 
$NewFellowship=[ordered]@{key1="value1";key2 = "value2"}
$NewFellowship
$NewFellowship.Add('key3','value3')
$NewFellowship.Add('key4','value4')
$NewFellowship
$NewFellowship.Set_item("key3","value3.1") #to replace a particular value in hashtable
$NewFellowship
$NewFellowship["key1"] #to print value1
$NewFellowship.Remove("key4") #to remove a key-pair


#--------Read-Host--------#
$ColorFavourite = Read-Host "What is your favourite color?" #to fill a variable with user input
$ColorFavourite

Write-Output "What is your Favourite Color?"
Write-Output "1. Blue"
Write-Output "2. Green"
$ColorFavourite = Read-Host "Select 1 or 2: "
$ColorFavourite


#--------If-Else-ElseIf-------#
$num = "100"
If ($num -lt "100"){
    Write-Output "Number is less than 100"
} elseif ($num -gt "100") {
    Write-Output "Number is greater than 100"
} else{
    Write-Output "Number = 100"
}


#-------Switch-----it is like Case statement#
$fruit = "apple" #default value
$fruit = Read-Host "Enter fruit name to get price (apple/banana): " #user-input
Switch($fruit){
    "apple"{
        Write-Output "Apple at 25/KG"
    }
    "banana"{
        Write-Output "Banana at 15/KG"
    }
    default{
        Write-Output "Did not enter apple or banana"
    }
}


#-----ForEach----------#

$heroes = ('Batman','Superman','Spiderman','Wonder Woman')
ForEach ($hero in $heroes){
    Write-Output "$hero has arrived!" #$hero even when inside " will print value, otherwise it will be printed in different lines
}


#--------While----------#

$i = 0
while($i -lt 4){
    Write-Output "This is line#$i"
    $i++
}



#-------Do-While----#
$i = 0
$animal = @('Wolf','Dog','Lion')
do {
    Write-Output ($animal[$i] + " is an Animal!") # using () will concat string instead of printing in new line 
    $i++
} while ($i -lt 3)



#--------Functions-----#

function pingwebsite{
    param(
        $website = "www.google.com"
    )
    ping $website
}

pingwebsite #calling the function


#-----Function with Parameters------#
function pingwebsite{
    param( #setting default values
        $website = "www.google.com", 
        $counter = 10
    )
    Test-Connection $website -Count $counter #ping does not have -count so we are using Test-Connection
}
pingwebsite -website "www.bing.com" -counter 5 #providing params in call



#----------Exceptions------#

Throw "It's a trap" #to just print an error
Write-Error "It's an Error" -ErrorAction Stop #to stop script when this error comes


#------------Throw-Catch------#

function pingwebsite{
    param(
        [CmdletBinding()] #for advanced parameters
        $website = "www.google.com",
        [Parameter(Mandatory)]
        [int32]$counter = 5 #this is mandatory param user needs to provide
    )
    Test-Connection $website -Count $counter 
    Write-Error "Generating an error on purpose" -ErrorAction Stop #throwing an error on purpose, -ErrorAction Stop is a terminating error for running catch block
}
try{ 
    pingwebsite -count 2 #try running this code and run catch block if terminating error occurs
}catch{ #this block will execute if there is a terminating error
    Write-Error "There is an error, catch block is executing"
    Write-Output $_
}


#--------New-Item---#
New-Item -Path C:\ -ItemType Directory -Name "Scripts"
New-Item -Path C:\Scripts\ -ItemType File -Name "test.txt" -Value "Sample text"
Copy-Item C:\Scripts\test.txt -Destination C:\Scripts\test1.txt
Remove-Item C:\Scripts\test1.txt
Test-Path C:\Scripts\test1.txt #True if file exists, False if not 
Rename-Item -Path C:\Scripts\test.txt -NewName test0.txt
