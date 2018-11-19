files_api = ["FindNextFile","FindFirstFile","FindFirstFileEx","SetFilePointer","SetFilePointerEx", "GetFileSize","GetFileSizeEx",
			"SetFileAttributes", "GetFileType","CopyFileEx","CopyFile","DeleteFile","EncryptFile","NtReadFile","NtWriteFile",
			 "GetFileAttributes","GetFileAttributesEx"]
crypt_api = ["CryptDeriveKey", "CryptDecodeObject", "CryptGenKey", "CryptImportPublicKeyInfo", "CryptAcquireContext","CryptAcquireContextW"]
register_api = ["RegCloseKey","RegCreateKeyExW","RegDeleteKeyW","RegQueryValueExW","RegSetValueExW",
				"RegEnumKeyExA","RegOpenKeyExW","NtQueryValueKey","NtOpenKey"]
internet_api = ["socket", "InternetOpen","shutdown","sendto","connect","bind","listen","accept","recv","send",
				"InternetOpenUrl","InternetReadFile","InternetWriteFile"]