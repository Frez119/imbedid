__int64 sub_140001520()
{
  float v0; // xmm1_4
  int v1; // ebx
  _QWORD *v2; // rdi
  _BYTE v4[12]; // [rsp+48h] [rbp-C0h] BYREF
  _OWORD v5[4]; // [rsp+58h] [rbp-B0h] BYREF
  __int64 v6; // [rsp+98h] [rbp-70h] BYREF
  float v7; // [rsp+A0h] [rbp-68h]
  int v8[4]; // [rsp+A8h] [rbp-60h] BYREF
  __int128 v9[4]; // [rsp+B8h] [rbp-50h] BYREF
  char v10[64]; // [rsp+F8h] [rbp-10h] BYREF
  char v11[64]; // [rsp+138h] [rbp+30h] BYREF
  char v12[64]; // [rsp+178h] [rbp+70h] BYREF
  char v13[64]; // [rsp+1B8h] [rbp+B0h] BYREF
  char v14[64]; // [rsp+1F8h] [rbp+F0h] BYREF

  (*(void (__fastcall **)(__int64, _QWORD, _QWORD, __int64, int, int, _DWORD))(*(_QWORD *)qword_140020438 + 344i64))(
    qword_140020438,
    0i64,
    0i64,
    1i64,
    -16777216,
    1065353216,
    0);
  (*(void (__fastcall **)(__int64, _QWORD, _QWORD, __int64, int, int, _DWORD))(*(_QWORD *)qword_140020438 + 344i64))(
    qword_140020438,
    0i64,
    0i64,
    2i64,
    -16777216,
    1065353216,
    0);
  (*(void (__fastcall **)(__int64))(*(_QWORD *)qword_140020438 + 328i64))(qword_140020438);
  (*(void (__fastcall **)(__int64, __int64))(*(_QWORD *)qword_140020438 + 712i64))(qword_140020438, 322i64);
  D3DXMatrixRotationYawPitchRoll(v11);
  v0 = *(float *)&dword_140020694 + *(float *)&dword_140020468;
  *(float *)&dword_140020694 = *(float *)&dword_140020694 + *(float *)&dword_140020468;
  if ( *(float *)&dword_140020694 < 300.0 )
  {
    if ( v0 <= -300.0 )
      dword_140020694 = -1013612544;
  }
  else
  {
    dword_140020694 = 1133871104;
  }
  dword_140020468 = 0;
  v6 = 0i64;
  v7 = 1.0;
  *(_QWORD *)v4 = 0i64;
  *(_DWORD *)&v4[8] = 1065353216;
  D3DXVec3TransformCoord(&v6, v4, v11);
  v8[0] = dword_140020694;
  v8[2] = dword_140020698;
  *(float *)&v6 = *(float *)&v6 + *(float *)&dword_140020694;
  v8[1] = 1095027917;
  *((float *)&v6 + 1) = *((float *)&v6 + 1) + 12.3;
  *(_DWORD *)v4 = 0;
  *(_QWORD *)&v4[4] = 1065353216i64;
  v7 = v7 + *(float *)&dword_140020698;
  D3DXMatrixLookAtLH(v12, v8, &v6, v4);
  (*(void (__fastcall **)(__int64, __int64, char *))(*(_QWORD *)qword_140020438 + 352i64))(qword_140020438, 2i64, v12);
  D3DXMatrixPerspectiveFovLH(v13);
  (*(void (__fastcall **)(__int64, __int64, char *))(*(_QWORD *)qword_140020438 + 352i64))(qword_140020438, 3i64, v13);
  D3DXMatrixScaling(v14);
  v1 = 0;
  v2 = &unk_140020470;
  do
  {
    D3DXMatrixTranslation(v10);
    D3DXMatrixMultiply(v5, v10, v14);
    v9[0] = v5[0];
    v9[1] = v5[1];
    v9[2] = v5[2];
    v9[3] = v5[3];
    (*(void (__fastcall **)(__int64, __int64, __int128 *))(*(_QWORD *)qword_140020438 + 352i64))(
      qword_140020438,
      256i64,
      v9);
    (*(void (__fastcall **)(_QWORD, _QWORD))(*(_QWORD *)*v2 + 24i64))(*v2, 0i64);
    ++v1;
    ++v2;
  }
  while ( v1 < 68 );
  (*(void (__fastcall **)(__int64, _QWORD, __int64, _QWORD, int))(*(_QWORD *)qword_140020438 + 800i64))(
    qword_140020438,
    0i64,
    qword_140020428,
    0i64,
    24);
  (*(void (__fastcall **)(__int64, _QWORD, __int64))(*(_QWORD *)qword_140020438 + 520i64))(
    qword_140020438,
    0i64,
    qword_140020458);
  D3DXMatrixTranslation(v10);
  (*(void (__fastcall **)(__int64, __int64, char *))(*(_QWORD *)qword_140020438 + 352i64))(qword_140020438, 256i64, v10);
  (*(void (__fastcall **)(__int64, __int64, _QWORD))(*(_QWORD *)qword_140020438 + 648i64))(qword_140020438, 5i64, 0i64);
  (*(void (__fastcall **)(__int64, __int64, __int64, __int64))(*(_QWORD *)qword_140020438 + 648i64))(
    qword_140020438,
    5i64,
    8i64,
    6i64);
  (*(void (__fastcall **)(__int64))(*(_QWORD *)qword_140020438 + 336i64))(qword_140020438);
  return (*(__int64 (__fastcall **)(__int64, _QWORD, _QWORD, _QWORD, _QWORD))(*(_QWORD *)qword_140020438 + 136i64))(
           qword_140020438,
           0i64,
           0i64,
           0i64,
           0i64);
}