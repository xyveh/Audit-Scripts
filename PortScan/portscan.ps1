param (
    [Parameter(Mandatory=$true)]
    [string]$ip,
    [Parameter(Mandatory=$true)]
    $p
)

function Ip2Int(){
    param($ip)

    $addressBytes = ([IPAddress] $ip).GetAddressBytes()
    [Array]::Reverse($addressBytes)
    return [uint32] ([IPAddress] $addressBytes).Address
}

function Int2Ip {
    param ($intIP)

    $addressBytes =  ([IPAddress] $intIP).GetAddressBytes()
    [Array]::Reverse($addressBytes)
    return  [IPAddress] $addressBytes
}

if ($ip -match '-'){
    $temp = $ip.Split("-")

    $startIPInt = Ip2Int($temp[0])
    $endIPInt = Ip2Int($temp[1])

    [uint32[]] $IPIntArray = ([uint32]$startIPInt) .. ([uint32]$endIPInt) 
}elseif ($ip -match "/") {
    $temp = $ip.Split("/")
    
    $startIPInt = Ip2Int($temp[0])
    
    $cidr = [int32] $temp[1]
    $NumberOfIPs = ([System.Math]::Pow(2, 32-$cidr)) -1
    
    $endIPInt = $startIPInt + $NumberOfIPs

    $IPIntArray = $startIPInt .. $endIPInt
}else{
    $startIPInt = Ip2Int($ip)
    $IPIntArray = @($startIPInt)
}

if ($p -match '-'){
    [int32[]] $temp = $p.Split("-")

    $ports = $temp[0] .. $temp[1]   
}
else{
    $ports = $p 
}
foreach($ipInt in $IPIntArray){
    $ip = Int2Ip($ipInt)
    
    if( test-connection $ip -count 1 -Quiet ){
        write-host "Host $ip is up"
        foreach($port in $ports){   
            try{
                $socket = new-object System.Net.Sockets.TcpClient($ipAddresses, $port)
                $socket.Close()

                write-host "$port is open"
                
            } Catch [System.Net.Sockets.SocketException]{
                
            }
        }
    }
}