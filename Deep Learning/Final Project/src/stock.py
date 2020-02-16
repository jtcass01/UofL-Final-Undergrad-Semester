import enum
import os

class stock():
    @staticmethod
    def generate_enums(stock_directory, output_directory):
        stock_files = [file for file in os.listdir(stock_directory) if os.path.isfile(os.path.join(stock_directory, file))]

        with open(output_directory + "stock_enums.txt", "w+") as file:
            for stock_file_enum, stock_file in enumerate(stock_files):
                file.write("STOCK_{} = {}\n".format(stock_file.split(".")[0].upper(), stock_file_enum+1))

    @staticmethod
    def generate_enum___str__(stock_directory, output_directory):
        stock_files = [file for file in os.listdir(stock_directory) if os.path.isfile(os.path.join(stock_directory, file))]

        with open(output_directory + "stock_enum___str__.txt", "w+") as file:
            file.write("def __str__(self):\n")
            file.write("    if self == stock.STOCK.STOCK_INVALID:\n")
            file.write("        return \"invalid\"\n")
            for stock_file_enum, stock_file in enumerate(stock_files):
                file.write("    elif self == stock.STOCK.STOCK_{}:\n".format(stock_file.split(".")[0].upper()))
                file.write("        return \"{}\"\n".format(stock_file.split(".")[0]))

    @staticmethod
    def load(stock_directory, stock):
        pass

"""
    class STOCK(enum.Enum):
        STOCK_INVALID = 0
        STOCK_A = 1
        STOCK_AA = 2
        STOCK_AAAP = 3
        STOCK_AABA = 4
        STOCK_AAC = 5
        STOCK_AAL = 6
        STOCK_AAMC = 7
        STOCK_AAME = 8
        STOCK_AAN = 9
        STOCK_AAOI = 10
        STOCK_AAON = 11
        STOCK_AAP = 12
        STOCK_AAPL = 13
        STOCK_AAT = 14
        STOCK_AAU = 15
        STOCK_AAV = 16
        STOCK_AAWW = 17
        STOCK_AAXN = 18
        STOCK_AB = 19
        STOCK_ABAC = 20
        STOCK_ABAX = 21
        STOCK_ABB = 22
        STOCK_ABBV = 23
        STOCK_ABC = 24
        STOCK_ABCB = 25
        STOCK_ABCD = 26
        STOCK_ABCO = 27
        STOCK_ABDC = 28
        STOCK_ABE = 29
        STOCK_ABEO = 30
        STOCK_ABEOW = 31
        STOCK_ABEV = 32
        STOCK_ABG = 33
        STOCK_ABIL = 34
        STOCK_ABIO = 35
        STOCK_ABLX = 36
        STOCK_ABM = 37
        STOCK_ABMD = 38
        STOCK_ABR = 39
        STOCK_ABRN = 40
        STOCK_ABR_A = 41
        STOCK_ABR_B = 42
        STOCK_ABR_C = 43
        STOCK_ABT = 44
        STOCK_ABTX = 45
        STOCK_ABUS = 46
        STOCK_ABX = 47
        STOCK_ABY = 48
        STOCK_AC = 49
        STOCK_ACAD = 50
        STOCK_ACBI = 51
        STOCK_ACC = 52
        STOCK_ACCO = 53
        STOCK_ACCP = 54
        STOCK_ACER = 55
        STOCK_ACERW = 56
        STOCK_ACET = 57
        STOCK_ACFC = 58
        STOCK_ACGL = 59
        STOCK_ACGLO = 60
        STOCK_ACGLP = 61
        STOCK_ACH = 62
        STOCK_ACHC = 63
        STOCK_ACHN = 64
        STOCK_ACHV = 65
        STOCK_ACIA = 66
        STOCK_ACIU = 67
        STOCK_ACIW = 68
        STOCK_ACLS = 69
        STOCK_ACM = 70
        STOCK_ACMR = 71
        STOCK_ACN = 72
        STOCK_ACNB = 73
        STOCK_ACOR = 74
        STOCK_ACP = 75
        STOCK_ACRE = 76
        STOCK_ACRS = 77
        STOCK_ACRX = 78
        STOCK_ACSF = 79
        STOCK_ACSI = 80
        STOCK_ACST = 81
        STOCK_ACTA = 82
        STOCK_ACTG = 83
        STOCK_ACU = 84
        STOCK_ACV = 85
        STOCK_ACXM = 86
        STOCK_ACY = 87
        STOCK_ADAP = 88
        STOCK_ADBE = 89
        STOCK_ADC = 90
        STOCK_ADES = 91
        STOCK_ADHD = 92
        STOCK_ADI = 93
        STOCK_ADM = 94
        STOCK_ADMA = 95
        STOCK_ADMP = 96
        STOCK_ADMS = 97
        STOCK_ADNT = 98
        STOCK_ADOM = 99
        STOCK_ADP = 100
        STOCK_ADRO = 101
        STOCK_ADS = 102
        STOCK_ADSK = 103
        STOCK_ADSW = 104
        STOCK_ADTN = 105
        STOCK_ADUS = 106
        STOCK_ADVM = 107
        STOCK_ADX = 108
        STOCK_ADXS = 109
        STOCK_ADXSW = 110
        STOCK_AE = 111
        STOCK_AEB = 112
        STOCK_AED = 113
        STOCK_AEE = 114
        STOCK_AEG = 115
        STOCK_AEGN = 116
        STOCK_AEH = 117
        STOCK_AEHR = 118
        STOCK_AEIS = 119
        STOCK_AEK = 120
        STOCK_AEL = 121
        STOCK_AEM = 122
        STOCK_AEMD = 123
        STOCK_AEO = 124
        STOCK_AEP = 125
        STOCK_AER = 126
        STOCK_AERI = 127
        STOCK_AES = 128
        STOCK_AET = 129
        STOCK_AETI = 130
        STOCK_AEUA = 131
        STOCK_AEY = 132
        STOCK_AEZS = 133
        STOCK_AFAM = 134
        STOCK_AFB = 135
        STOCK_AFC = 136
        STOCK_AFG = 137
        STOCK_AFGE = 138
        STOCK_AFGH = 139
        STOCK_AFH = 140
        STOCK_AFHBL = 141
        STOCK_AFI = 142
        STOCK_AFL = 143
        STOCK_AFMD = 144
        STOCK_AFSD = 145
        STOCK_AFSI = 146
        STOCK_AFSI_A = 147
        STOCK_AFSI_B = 148
        STOCK_AFSI_C = 149
        STOCK_AFSI_D = 150
        STOCK_AFSI_E = 151
        STOCK_AFSI_F = 152
        STOCK_AFSS = 153
        STOCK_AFST = 154
        STOCK_AFT = 155
        STOCK_AFTY = 156
        STOCK_AG = 157
        STOCK_AGC = 158
        STOCK_AGCO = 159
        STOCK_AGD = 160
        STOCK_AGEN = 161
        STOCK_AGFS = 162
        STOCK_AGFSW = 163
        STOCK_AGGE = 164
        STOCK_AGGP = 165
        STOCK_AGGY = 166
        STOCK_AGI = 167
        STOCK_AGII = 168
        STOCK_AGIIL = 169
        STOCK_AGIO = 170
        STOCK_AGLE = 171
        STOCK_AGM__A = 172
        STOCK_AGM = 173
        STOCK_AGM_A = 174
        STOCK_AGM_B = 175
        STOCK_AGM_C = 176
        STOCK_AGN = 177
        STOCK_AGNC = 178
        STOCK_AGNCB = 179
        STOCK_AGNCN = 180
        STOCK_AGN_A = 181
        STOCK_AGO = 182
        STOCK_AGO_B = 183
        STOCK_AGO_E = 184
        STOCK_AGO_F = 185
        STOCK_AGR = 186
        STOCK_AGRO = 187
        STOCK_AGRX = 188
        STOCK_AGT = 189
        STOCK_AGTC = 190
        STOCK_AGU = 191
        STOCK_AGX = 192
        STOCK_AGYS = 193
        STOCK_AHC = 194
        STOCK_AHGP = 195
        STOCK_AHH = 196
        STOCK_AHL = 197
        STOCK_AHL_C = 198
        STOCK_AHL_D = 199
        STOCK_AHP = 200
        STOCK_AHPA = 201
        STOCK_AHPAU = 202
        STOCK_AHPAW = 203
        STOCK_AHPI = 204
        STOCK_AHP_B = 205
        STOCK_AHT = 206
        STOCK_AHT_D = 207
        STOCK_AHT_F = 208
        STOCK_AHT_G = 209
        STOCK_AHT_H = 210
        STOCK_AI = 211
        STOCK_AIB__CL = 212
        STOCK_AIC = 213
        STOCK_AIEQ = 214
        STOCK_AIF = 215
        STOCK_AIG__WS = 216
        STOCK_AIG = 217
        STOCK_AIMC = 218
        STOCK_AIMT = 219
        STOCK_AIN = 220
        STOCK_AINC = 221
        STOCK_AINV = 222
        STOCK_AIR = 223
        STOCK_AIRG = 224
        STOCK_AIRI = 225
        STOCK_AIRT = 226
        STOCK_AIT = 227
        STOCK_AIV = 228
        STOCK_AIV_A = 229
        STOCK_AIW = 230
        STOCK_AIY = 231
        STOCK_AIZ = 232
        STOCK_AI_B = 233
        STOCK_AJG = 234
        STOCK_AJRD = 235
        STOCK_AJX = 236
        STOCK_AJXA = 237
        STOCK_AKAM = 238
        STOCK_AKAO = 239
        STOCK_AKBA = 240
        STOCK_AKCA = 241
        STOCK_AKER = 242
        STOCK_AKG = 243
        STOCK_AKO__A = 244
        STOCK_AKO__B = 245
        STOCK_AKP = 246
        STOCK_AKR = 247
        STOCK_AKRX = 248
        STOCK_AKS = 249
        STOCK_AKTS = 250
        STOCK_AKTX = 251
        STOCK_AL = 252
        STOCK_ALB = 253
        STOCK_ALBO = 254
        STOCK_ALCO = 255
        STOCK_ALDR = 256
        STOCK_ALDW = 257
        STOCK_ALDX = 258
        STOCK_ALE = 259
        STOCK_ALEX = 260
        STOCK_ALFI = 261
        STOCK_ALG = 262
        STOCK_ALGN = 263
        STOCK_ALGT = 264
        STOCK_ALIM = 265
        STOCK_ALJJ = 266
        STOCK_ALK = 267
        STOCK_ALKS = 268
        STOCK_ALL = 269
        STOCK_ALLE = 270
        STOCK_ALLT = 271
        STOCK_ALLY = 272
        STOCK_ALLY_A = 273
        STOCK_ALL_A = 274
        STOCK_ALL_B = 275
        STOCK_ALL_C = 276
        STOCK_ALL_D = 277
        STOCK_ALL_E = 278
        STOCK_ALL_F = 279
        STOCK_ALN = 280
        STOCK_ALNA = 281
        STOCK_ALNY = 282
        STOCK_ALO = 283
        STOCK_ALOG = 284
        STOCK_ALOT = 285
        STOCK_ALPN = 286
        STOCK_ALP_O__CL = 287
        STOCK_ALP_Q = 288
        STOCK_ALQA = 289
        STOCK_ALRM = 290
        STOCK_ALRN = 291
        STOCK_ALSK = 292
        STOCK_ALSN = 293
        STOCK_ALT = 294
        STOCK_ALTR = 295
        STOCK_ALTY = 296
        STOCK_ALV = 297
        STOCK_ALX = 298
        STOCK_ALXN = 299
        STOCK_AM = 300
        STOCK_AMAG = 301
        STOCK_AMAT = 302
        STOCK_AMBA = 303
        STOCK_AMBC = 304
        STOCK_AMBCW = 305
        STOCK_AMBR = 306
        STOCK_AMC = 307
        STOCK_AMCA = 308
        STOCK_AMCN = 309
        STOCK_AMCX = 310
        STOCK_AMD = 311
        STOCK_AMDA = 312
        STOCK_AME = 313
        STOCK_AMED = 314
        STOCK_AMFW = 315
        STOCK_AMG = 316
        STOCK_AMGN = 317
        STOCK_AMGP = 318
        STOCK_AMH = 319
        STOCK_AMH_C = 320
        STOCK_AMH_D = 321
        STOCK_AMH_E = 322
        STOCK_AMH_F = 323
        STOCK_AMH_G = 324
        STOCK_AMID = 325
        STOCK_AMKR = 326
        STOCK_AMLX = 327
        STOCK_AMMA = 328
        STOCK_AMN = 329
        STOCK_AMNB = 330
        STOCK_AMOT = 331
        STOCK_AMOV = 332
        STOCK_AMP = 333
        STOCK_AMPE = 334
        STOCK_AMPH = 335
        STOCK_AMRB = 336
        STOCK_AMRC = 337
        STOCK_AMRH = 338
        STOCK_AMRHW = 339
        STOCK_AMRK = 340
        STOCK_AMRN = 341
        STOCK_AMRS = 342
        STOCK_AMS = 343
        STOCK_AMSC = 344
        STOCK_AMSF = 345
        STOCK_AMSWA = 346
        STOCK_AMT = 347
        STOCK_AMTD = 348
        STOCK_AMTX = 349
        STOCK_AMT_B = 350
        STOCK_AMWD = 351
        STOCK_AMX = 352
        STOCK_AMZA = 353
        STOCK_AMZN = 354
        STOCK_AN = 355
        STOCK_ANAB = 356
        STOCK_ANAT = 357
        STOCK_ANCB = 358
        STOCK_ANCX = 359
        STOCK_ANDA = 360
        STOCK_ANDAR = 361
        STOCK_ANDAU = 362
        STOCK_ANDAW = 363
        STOCK_ANDE = 364
        STOCK_ANDV = 365
        STOCK_ANDX = 366
        STOCK_ANET = 367
        STOCK_ANF = 368
        STOCK_ANFI = 369
        STOCK_ANGI = 370
        STOCK_ANGO = 371
        STOCK_ANH = 372
        STOCK_ANH_A = 373
        STOCK_ANH_B = 374
        STOCK_ANH_C = 375
        STOCK_ANIK = 376
        STOCK_ANIP = 377
        STOCK_ANSS = 378
        STOCK_ANTH = 379
        STOCK_ANTM = 380
        STOCK_ANTX = 381
        STOCK_ANW = 382
        STOCK_ANY = 383
        STOCK_AOBC = 384
        STOCK_AOD = 385
        STOCK_AOI = 386
        STOCK_AON = 387
        STOCK_AOS = 388
        STOCK_AOSL = 389
        STOCK_AOXG = 390
        STOCK_AP = 391
        STOCK_APA = 392
        STOCK_APAM = 393
        STOCK_APB = 394
        STOCK_APC = 395
        STOCK_APD = 396
        STOCK_APDN = 397
        STOCK_APDNW = 398
        STOCK_APEI = 399
        STOCK_APEN = 400
        STOCK_APF = 401
        STOCK_APH = 402
        STOCK_APHB = 403
        STOCK_APLE = 404
        STOCK_APLP = 405
        STOCK_APLS = 406
        STOCK_APO = 407
        STOCK_APOG = 408
        STOCK_APOP = 409
        STOCK_APOPW = 410
        STOCK_APO_A = 411
        STOCK_APPF = 412
        STOCK_APPN = 413
        STOCK_APPS = 414
        STOCK_APRI = 415
        STOCK_APRN = 416
        STOCK_APT = 417
        STOCK_APTI = 418
        STOCK_APTO = 419
        STOCK_APTS = 420
        STOCK_APU = 421
        STOCK_APVO = 422
        STOCK_APWC = 423
        STOCK_AQ = 424
        STOCK_AQB = 425
        STOCK_AQMS = 426
        STOCK_AQN = 427
        STOCK_AQUA = 428
        STOCK_AQXP = 429
        STOCK_AR = 430
        STOCK_ARA = 431
        STOCK_ARAY = 432
        STOCK_ARC = 433
        STOCK_ARCB = 434
        STOCK_ARCC = 435
        STOCK_ARCH = 436
        STOCK_ARCI = 437
        STOCK_ARCM = 438
        STOCK_ARCO = 439
        STOCK_ARCW = 440
        STOCK_ARCX = 441
        STOCK_ARD = 442
        STOCK_ARDC = 443
        STOCK_ARDM = 444
        STOCK_ARDX = 445
        STOCK_ARE = 446
        STOCK_ARES = 447
        STOCK_ARES_A = 448
        STOCK_AREX = 449
        STOCK_ARE_D = 450
        STOCK_ARGS = 451
        STOCK_ARGX = 452
        STOCK_ARH_C = 453
        STOCK_ARI = 454
        STOCK_ARII = 455
        STOCK_ARI_C = 456
        STOCK_ARKG = 457
        STOCK_ARKK = 458
        STOCK_ARKQ = 459
        STOCK_ARKR = 460
        STOCK_ARKW = 461
        STOCK_ARL = 462
        STOCK_ARLP = 463
        STOCK_ARLZ = 464
        STOCK_ARMK = 465
        STOCK_ARNA = 466
        STOCK_ARNC = 467
        STOCK_ARNC_ = 468
        STOCK_ARNC_B = 469
        STOCK_AROC = 470
        STOCK_AROW = 471
        STOCK_ARQL = 472
        STOCK_ARR = 473
        STOCK_ARRS = 474
        STOCK_ARRY = 475
        STOCK_ARR_A = 476
        STOCK_ARR_B = 477
        STOCK_ARTNA = 478
        STOCK_ARTW = 479
        STOCK_ARTX = 480
        STOCK_ARW = 481
        STOCK_ARWR = 482
        STOCK_ASA = 483
        STOCK_ASB__WS = 484
        STOCK_ASB = 485
        STOCK_ASB_C = 486
        STOCK_ASB_D = 487
        STOCK_ASC = 488
        STOCK_ASCMA = 489
        STOCK_ASET = 490
        STOCK_ASFI = 491
        STOCK_ASG = 492
        STOCK_ASGN = 493
        STOCK_ASH = 494
        STOCK_ASHX = 495
        STOCK_ASIX = 496
        STOCK_ASM = 497
        STOCK_ASMB = 498
        STOCK_ASML = 499
        STOCK_ASNA = 500
        STOCK_ASND = 501
        STOCK_ASNS = 502
        STOCK_ASPN = 503
        STOCK_ASPS = 504
        STOCK_ASPU = 505
        STOCK_ASR = 506
        STOCK_ASRV = 507
        STOCK_ASRVP = 508
        STOCK_AST = 509
        STOCK_ASTC = 510
        STOCK_ASTE = 511
        STOCK_ASUR = 512
        STOCK_ASV = 513
        STOCK_ASX = 514
        STOCK_ASYS = 515
        STOCK_AT = 516
        STOCK_ATAC = 517
        STOCK_ATACR = 518
        STOCK_ATACU = 519
        STOCK_ATAI = 520
        STOCK_ATAX = 521
        STOCK_ATEC = 522
        STOCK_ATEN = 523
        STOCK_ATGE = 524
        STOCK_ATH = 525
        STOCK_ATHM = 526
        STOCK_ATHN = 527
        STOCK_ATHX = 528
        STOCK_ATI = 529
        STOCK_ATKR = 530
        STOCK_ATLC = 531
        STOCK_ATLO = 532
        STOCK_ATNI = 533
        STOCK_ATNM = 534
        STOCK_ATNX = 535
        STOCK_ATO = 536
        STOCK_ATOM = 537
        STOCK_ATOS = 538
        STOCK_ATR = 539
        STOCK_ATRA = 540
        STOCK_ATRC = 541
        STOCK_ATRI = 542
        STOCK_ATRO = 543
        STOCK_ATRS = 544
        STOCK_ATSG = 545
        STOCK_ATTO = 546
        STOCK_ATTU = 547
        STOCK_ATU = 548
        STOCK_ATUS = 549
        STOCK_ATV = 550
        STOCK_ATVI = 551
        STOCK_ATXI = 552
        STOCK_AU = 553
        STOCK_AUBN = 554
        STOCK_AUDC = 555
        STOCK_AUG = 556
        STOCK_AUMN = 557
        STOCK_AUO = 558
        STOCK_AUPH = 559
        STOCK_AUTO = 560
        STOCK_AUY = 561
        STOCK_AVA = 562
        STOCK_AVAL = 563
        STOCK_AVAV = 564
        STOCK_AVB = 565
        STOCK_AVD = 566
        STOCK_AVDL = 567
        STOCK_AVEO = 568
        STOCK_AVGO = 569
        STOCK_AVGR = 570
        STOCK_AVH = 571
        STOCK_AVHI = 572
        STOCK_AVID = 573
        STOCK_AVIR = 574
        STOCK_AVK = 575
        STOCK_AVNW = 576
        STOCK_AVP = 577
        STOCK_AVT = 578
        STOCK_AVX = 579
        STOCK_AVXL = 580
        STOCK_AVXS = 581
        STOCK_AVY = 582
        STOCK_AWF = 583
        STOCK_AWI = 584
        STOCK_AWK = 585
        STOCK_AWP = 586
        STOCK_AWR = 587
        STOCK_AWRE = 588
        STOCK_AWX = 589
        STOCK_AXAS = 590
        STOCK_AXDX = 591
        STOCK_AXE = 592
        STOCK_AXGN = 593
        STOCK_AXL = 594
        STOCK_AXON = 595
        STOCK_AXP = 596
        STOCK_AXR = 597
        STOCK_AXS = 598
        STOCK_AXSM = 599
        STOCK_AXS_D = 600
        STOCK_AXS_E = 601
        STOCK_AXTA = 602
        STOCK_AXTI = 603
        STOCK_AXU = 604
        STOCK_AYI = 605
        STOCK_AYR = 606
        STOCK_AYTU = 607
        STOCK_AYX = 608
        STOCK_AZN = 609
        STOCK_AZO = 610
        STOCK_AZPN = 611
        STOCK_AZRE = 612
        STOCK_AZRX = 613
        STOCK_AZUL = 614
        STOCK_AZZ = 615
        STOCK_B = 616
        STOCK_BA = 617
        STOCK_BAA = 618
        STOCK_BABA = 619
        STOCK_BABY = 620
        STOCK_BAC__WS__A = 621
        STOCK_BAC__WS__B = 622
        STOCK_BAC = 623
        STOCK_BAC_A = 624
        STOCK_BAC_C = 625
        STOCK_BAC_D = 626
        STOCK_BAC_E = 627
        STOCK_BAC_I = 628
        STOCK_BAC_L = 629
        STOCK_BAC_W = 630
        STOCK_BAC_Y = 631
        STOCK_BAF = 632
        STOCK_BAH = 633
        STOCK_BAK = 634
        STOCK_BAM = 635
        STOCK_BANC = 636
        STOCK_BANC_C = 637
        STOCK_BANC_D = 638
        STOCK_BANC_E = 639
        STOCK_BAND = 640
        STOCK_BANF = 641
        STOCK_BANFP = 642
        STOCK_BANR = 643
        STOCK_BANX = 644
        STOCK_BAP = 645
        STOCK_BAR = 646
        STOCK_BAS = 647
        STOCK_BASI = 648
        STOCK_BATRA = 649
        STOCK_BATRK = 650
        STOCK_BAX = 651
        STOCK_BB = 652
        STOCK_BBBY = 653
        STOCK_BBC = 654
        STOCK_BBD = 655
        STOCK_BBDO = 656
        STOCK_BBF = 657
        STOCK_BBG = 658
        STOCK_BBGI = 659
        STOCK_BBK = 660
        STOCK_BBL = 661
        STOCK_BBN = 662
        STOCK_BBOX = 663
        STOCK_BBRG = 664
        STOCK_BBRX = 665
        STOCK_BBSI = 666
        STOCK_BBT = 667
        STOCK_BBT_D = 668
        STOCK_BBT_E = 669
        STOCK_BBT_F = 670
        STOCK_BBT_G = 671
        STOCK_BBT_H = 672
        STOCK_BBU = 673
        STOCK_BBVA = 674
        STOCK_BBW = 675
        STOCK_BBX = 676
        STOCK_BBY = 677
        STOCK_BC = 678
        STOCK_BCAC = 679
        STOCK_BCACR = 680
        STOCK_BCACU = 681
        STOCK_BCACW = 682
        STOCK_BCBP = 683
        STOCK_BCC = 684
        STOCK_BCD = 685
        STOCK_BCE = 686
        STOCK_BCEI = 687
        STOCK_BCH = 688
        STOCK_BCI = 689
        STOCK_BCLI = 690
        STOCK_BCO = 691
        STOCK_BCOM = 692
        STOCK_BCOR = 693
        STOCK_BCOV = 694
        STOCK_BCPC = 695
        STOCK_BCR = 696
        STOCK_BCRH = 697
        STOCK_BCRX = 698
        STOCK_BCS = 699
        STOCK_BCS_D = 700
        STOCK_BCTF = 701
        STOCK_BCV = 702
        STOCK_BCV_A = 703
        STOCK_BCX = 704
        STOCK_BDC = 705
        STOCK_BDCZ = 706
        STOCK_BDC_B = 707
        STOCK_BDGE = 708
        STOCK_BDJ = 709
        STOCK_BDL = 710
        STOCK_BDN = 711
        STOCK_BDR = 712
        STOCK_BDSI = 713
        STOCK_BDX = 714
        STOCK_BDXA = 715
        STOCK_BEAT = 716
        STOCK_BEBE = 717
        STOCK_BECN = 718
        STOCK_BEDU = 719
        STOCK_BEF = 720
        STOCK_BEL = 721
        STOCK_BELFA = 722
        STOCK_BELFB = 723
        STOCK_BEMO = 724
        STOCK_BEN = 725
        STOCK_BEP = 726
        STOCK_BERN = 727
        STOCK_BERY = 728
        STOCK_BETR = 729
        STOCK_BF__A = 730
        STOCK_BF__B = 731
        STOCK_BFAM = 732
        STOCK_BFIN = 733
        STOCK_BFIT = 734
        STOCK_BFK = 735
        STOCK_BFO = 736
        STOCK_BFR = 737
        STOCK_BFS = 738
        STOCK_BFS_C = 739
        STOCK_BFY = 740
        STOCK_BFZ = 741
        STOCK_BG = 742
        STOCK_BGB = 743
        STOCK_BGC = 744
        STOCK_BGCA = 745
        STOCK_BGCP = 746
        STOCK_BGFV = 747
        STOCK_BGG = 748
        STOCK_BGH = 749
        STOCK_BGI = 750
        STOCK_BGIO = 751
        STOCK_BGNE = 752
        STOCK_BGR = 753
        STOCK_BGS = 754
        STOCK_BGSF = 755
        STOCK_BGT = 756
        STOCK_BGX = 757
        STOCK_BGY = 758
        STOCK_BH = 759
        STOCK_BHAC = 760
        STOCK_BHACR = 761
        STOCK_BHACU = 762
        STOCK_BHACW = 763
        STOCK_BHB = 764
        STOCK_BHBK = 765
        STOCK_BHE = 766
        STOCK_BHF = 767
        STOCK_BHGE = 768
        STOCK_BHK = 769
        STOCK_BHLB = 770
        STOCK_BHP = 771
        STOCK_BHV = 772
        STOCK_BHVN = 773
        STOCK_BIBL = 774
        STOCK_BID = 775
        STOCK_BIDU = 776
        STOCK_BIF = 777
        STOCK_BIG = 778
        STOCK_BIIB = 779
        STOCK_BIO__B = 780
        STOCK_BIO = 781
        STOCK_BIOA = 782
        STOCK_BIOC = 783
        STOCK_BIOL = 784
        STOCK_BIOS = 785
        STOCK_BIP = 786
        STOCK_BIT = 787
        STOCK_BITA = 788
        STOCK_BIVV = 789
        STOCK_BJRI = 790
        STOCK_BJZ = 791
        STOCK_BK = 792
        STOCK_BKCC = 793
        STOCK_BKD = 794
        STOCK_BKE = 795
        STOCK_BKEP = 796
        STOCK_BKEPP = 797
        STOCK_BKH = 798
        STOCK_BKHU = 799
        STOCK_BKI = 800
        STOCK_BKJ = 801
        STOCK_BKK = 802
        STOCK_BKMU = 803
        STOCK_BKN = 804
        STOCK_BKS = 805
        STOCK_BKSC = 806
        STOCK_BKT = 807
        STOCK_BKU = 808
        STOCK_BKYI = 809
        STOCK_BK_C = 810
        STOCK_BL = 811
        STOCK_BLBD = 812
        STOCK_BLCM = 813
        STOCK_BLD = 814
        STOCK_BLDP = 815
        STOCK_BLDR = 816
        STOCK_BLE = 817
        STOCK_BLES = 818
        STOCK_BLFS = 819
        STOCK_BLH = 820
        STOCK_BLHY = 821
        STOCK_BLIN = 822
        STOCK_BLJ = 823
        STOCK_BLK = 824
        STOCK_BLKB = 825
        STOCK_BLL = 826
        STOCK_BLMN = 827
        STOCK_BLMT = 828
        STOCK_BLPH = 829
        STOCK_BLRX = 830
        STOCK_BLUE = 831
        STOCK_BLVD = 832
        STOCK_BLVDU = 833
        STOCK_BLVDW = 834
        STOCK_BLW = 835
        STOCK_BLX = 836
        STOCK_BMA = 837
        STOCK_BMCH = 838
        STOCK_BME = 839
        STOCK_BMI = 840
        STOCK_BMLA = 841
        STOCK_BMLP = 842
        STOCK_BML_G = 843
        STOCK_BML_H = 844
        STOCK_BML_I = 845
        STOCK_BML_J = 846
        STOCK_BML_L = 847
        STOCK_BMO = 848
        STOCK_BMRA = 849
        STOCK_BMRC = 850
        STOCK_BMRN = 851
        STOCK_BMS = 852
        STOCK_BMTC = 853
        STOCK_BMY = 854
        STOCK_BNCL = 855
        STOCK_BNDC = 856
        STOCK_BNED = 857
        STOCK_BNFT = 858
        STOCK_BNJ = 859
        STOCK_BNS = 860
        STOCK_BNSO = 861
        STOCK_BNTC = 862
        STOCK_BNTCW = 863
        STOCK_BNY = 864
        STOCK_BOBE = 865
        STOCK_BOCH = 866
        STOCK_BOE = 867
        STOCK_BOFI = 868
        STOCK_BOFIL = 869
        STOCK_BOH = 870
        STOCK_BOJA = 871
        STOCK_BOKF = 872
        STOCK_BOKFL = 873
        STOCK_BOLD = 874
        STOCK_BOLT = 875
        STOCK_BOMN = 876
        STOCK_BONT = 877
        STOCK_BOOM = 878
        STOCK_BOOT = 879
        STOCK_BORN = 880
        STOCK_BOSC = 881
        STOCK_BOSS = 882
        STOCK_BOTJ = 883
        STOCK_BOTZ = 884
        STOCK_BOX = 885
        STOCK_BOXL = 886
        STOCK_BP = 887
        STOCK_BPFH = 888
        STOCK_BPFHP = 889
        STOCK_BPFHW = 890
        STOCK_BPI = 891
        STOCK_BPK = 892
        STOCK_BPL = 893
        STOCK_BPMC = 894
        STOCK_BPMP = 895
        STOCK_BPMX = 896
        STOCK_BPOP = 897
        STOCK_BPOPM = 898
        STOCK_BPOPN = 899
        STOCK_BPRN = 900
        STOCK_BPT = 901
        STOCK_BPTH = 902
        STOCK_BPY = 903
        STOCK_BQH = 904
        STOCK_BR = 905
        STOCK_BRAC = 906
        STOCK_BRACR = 907
        STOCK_BRACU = 908
        STOCK_BRACW = 909
        STOCK_BRC = 910
        STOCK_BRCD = 911
        STOCK_BREW = 912
        STOCK_BRFS = 913
        STOCK_BRG = 914
        STOCK_BRGL = 915
        STOCK_BRG_A = 916
        STOCK_BRG_C = 917
        STOCK_BRG_D = 918
        STOCK_BRID = 919
        STOCK_BRK__A = 920
        STOCK_BRK__B = 921
        STOCK_BRKL = 922
        STOCK_BRKR = 923
        STOCK_BRKS = 924
        STOCK_BRN = 925
        STOCK_BRO = 926
        STOCK_BRQS = 927
        STOCK_BRQSW = 928
        STOCK_BRS = 929
        STOCK_BRSS = 930
        STOCK_BRT = 931
        STOCK_BRX = 932
        STOCK_BSAC = 933
        STOCK_BSBR = 934
        STOCK_BSCP = 935
        STOCK_BSCQ = 936
        STOCK_BSCR = 937
        STOCK_BSD = 938
        STOCK_BSE = 939
        STOCK_BSET = 940
        STOCK_BSF = 941
        STOCK_BSFT = 942
        STOCK_BSJN = 943
        STOCK_BSJO = 944
        STOCK_BSJP = 945
        STOCK_BSL = 946
        STOCK_BSM = 947
        STOCK_BSMX = 948
        STOCK_BSPM = 949
        STOCK_BSQR = 950
        STOCK_BSRR = 951
        STOCK_BST = 952
        STOCK_BSTC = 953
        STOCK_BSTI = 954
        STOCK_BSWN = 955
        STOCK_BSX = 956
        STOCK_BT = 957
        STOCK_BTA = 958
        STOCK_BTE = 959
        STOCK_BTEC = 960
        STOCK_BTG = 961
        STOCK_BTI = 962
        STOCK_BTN = 963
        STOCK_BTO = 964
        STOCK_BTT = 965
        STOCK_BTU = 966
        STOCK_BTU_ = 967
        STOCK_BTX__WS = 968
        STOCK_BTX = 969
        STOCK_BTZ = 970
        STOCK_BUD = 971
        STOCK_BUFF = 972
        STOCK_BUI = 973
        STOCK_BUR = 974
        STOCK_BURL = 975
        STOCK_BUSE = 976
        STOCK_BUZ = 977
        STOCK_BV = 978
        STOCK_BVAL = 979
        STOCK_BVN = 980
        STOCK_BVSN = 981
        STOCK_BVX = 982
        STOCK_BVXV = 983
        STOCK_BVXVW = 984
        STOCK_BW = 985
        STOCK_BWA = 986
        STOCK_BWEN = 987
        STOCK_BWFG = 988
        STOCK_BWG = 989
        STOCK_BWINA = 990
        STOCK_BWINB = 991
        STOCK_BWL__A = 992
        STOCK_BWLD = 993
        STOCK_BWP = 994
        STOCK_BWXT = 995
        STOCK_BX = 996
        STOCK_BXC = 997
        STOCK_BXE = 998
        STOCK_BXG = 999
        STOCK_BXMT = 1000
        STOCK_BXMX = 1001
        STOCK_BXP = 1002
        STOCK_BXP_B = 1003
        STOCK_BXS = 1004
        STOCK_BY = 1005
        STOCK_BYBK = 1006
        STOCK_BYD = 1007
        STOCK_BYFC = 1008
        STOCK_BYM = 1009
        STOCK_BYSI = 1010
        STOCK_BZH = 1011
        STOCK_BZM = 1012
        STOCK_BZUN = 1013
        STOCK_C__WS__A = 1014
        STOCK_C = 1015
        STOCK_CA = 1016
        STOCK_CAA = 1017
        STOCK_CAAS = 1018
        STOCK_CABO = 1019
        STOCK_CAC = 1020
        STOCK_CACC = 1021
        STOCK_CACG = 1022
        STOCK_CACI = 1023
        STOCK_CADC = 1024
        STOCK_CADE = 1025
        STOCK_CAE = 1026
        STOCK_CAF = 1027
        STOCK_CAFD = 1028
        STOCK_CAG = 1029
        STOCK_CAH = 1030
        STOCK_CAI = 1031
        STOCK_CAJ = 1032
        STOCK_CAKE = 1033
        STOCK_CAL = 1034
        STOCK_CALA = 1035
        STOCK_CALD = 1036
        STOCK_CALF = 1037
        STOCK_CALI = 1038
        STOCK_CALL = 1039
        STOCK_CALM = 1040
        STOCK_CALX = 1041
        STOCK_CAMP = 1042
        STOCK_CAMT = 1043
        STOCK_CANF = 1044
        STOCK_CAPL = 1045
        STOCK_CAPR = 1046
        STOCK_CAR = 1047
        STOCK_CARA = 1048
        STOCK_CARB = 1049
        STOCK_CARG = 1050
        STOCK_CARO = 1051
        STOCK_CARS = 1052
        STOCK_CART = 1053
        STOCK_CARV = 1054
        STOCK_CASC = 1055
        STOCK_CASH = 1056
        STOCK_CASI = 1057
        STOCK_CASM = 1058
        STOCK_CASS = 1059
        STOCK_CASY = 1060
        STOCK_CAT = 1061
        STOCK_CATB = 1062
        STOCK_CATC = 1063
        STOCK_CATH = 1064
        STOCK_CATM = 1065
        STOCK_CATO = 1066
        STOCK_CATS = 1067
        STOCK_CATY = 1068
        STOCK_CATYW = 1069
        STOCK_CAVM = 1070
        STOCK_CAW = 1071
        STOCK_CB = 1072
        STOCK_CBA = 1073
        STOCK_CBAK = 1074
        STOCK_CBAN = 1075
        STOCK_CBAY = 1076
        STOCK_CBB = 1077
        STOCK_CBB_B = 1078
        STOCK_CBD = 1079
        STOCK_CBF = 1080
        STOCK_CBFV = 1081
        STOCK_CBG = 1082
        STOCK_CBH = 1083
        STOCK_CBI = 1084
        STOCK_CBIO = 1085
        STOCK_CBK = 1086
        STOCK_CBL = 1087
        STOCK_CBLI = 1088
        STOCK_CBL_D = 1089
        STOCK_CBL_E = 1090
        STOCK_CBM = 1091
        STOCK_CBMG = 1092
        STOCK_CBMX = 1093
        STOCK_CBMXW = 1094
        STOCK_CBO = 1095
        STOCK_CBOE = 1096
        STOCK_CBPO = 1097
        STOCK_CBPX = 1098
        STOCK_CBRL = 1099
        STOCK_CBS__A = 1100
        STOCK_CBS = 1101
        STOCK_CBSH = 1102
        STOCK_CBSHP = 1103
        STOCK_CBT = 1104
        STOCK_CBTX = 1105
        STOCK_CBU = 1106
        STOCK_CBX = 1107
        STOCK_CBZ = 1108
        STOCK_CC = 1109
        STOCK_CCA = 1110
        STOCK_CCBG = 1111
        STOCK_CCC = 1112
        STOCK_CCCL = 1113
        STOCK_CCCR = 1114
        STOCK_CCD = 1115
        STOCK_CCE = 1116
        STOCK_CCF = 1117
        STOCK_CCI = 1118
        STOCK_CCIH = 1119
        STOCK_CCI_A = 1120
        STOCK_CCJ = 1121
        STOCK_CCK = 1122
        STOCK_CCL = 1123
        STOCK_CCLP = 1124
        STOCK_CCM = 1125
        STOCK_CCMP = 1126
        STOCK_CCNE = 1127
        STOCK_CCO = 1128
        STOCK_CCOI = 1129
        STOCK_CCOR = 1130
        STOCK_CCRC = 1131
        STOCK_CCRN = 1132
        STOCK_CCS = 1133
        STOCK_CCU = 1134
        STOCK_CCUR = 1135
        STOCK_CCV__CL = 1136
        STOCK_CCV = 1137
        STOCK_CCXI = 1138
        STOCK_CCZ = 1139
        STOCK_CDC = 1140
        STOCK_CDE = 1141
        STOCK_CDEV = 1142
        STOCK_CDK = 1143
        STOCK_CDL = 1144
        STOCK_CDNA = 1145
        STOCK_CDNS = 1146
        STOCK_CDOR = 1147
        STOCK_CDR = 1148
        STOCK_CDR_B = 1149
        STOCK_CDR_C = 1150
        STOCK_CDTI = 1151
        STOCK_CDTX = 1152
        STOCK_CDW = 1153
        STOCK_CDXC = 1154
        STOCK_CDXS = 1155
        STOCK_CDZI = 1156
        STOCK_CE = 1157
        STOCK_CEA = 1158
        STOCK_CECE = 1159
        STOCK_CECO = 1160
        STOCK_CEE = 1161
        STOCK_CEF = 1162
        STOCK_CEFS = 1163
        STOCK_CEI = 1164
        STOCK_CEL = 1165
        STOCK_CELC = 1166
        STOCK_CELG = 1167
        STOCK_CELGZ = 1168
        STOCK_CELH = 1169
        STOCK_CELP = 1170
        STOCK_CEM = 1171
        STOCK_CEMB = 1172
        STOCK_CEMI = 1173
        STOCK_CEN = 1174
        STOCK_CENT = 1175
        STOCK_CENTA = 1176
        STOCK_CENX = 1177
        STOCK_CEO = 1178
        STOCK_CEQP = 1179
        STOCK_CERC = 1180
        STOCK_CERCW = 1181
        STOCK_CERN = 1182
        STOCK_CERS = 1183
        STOCK_CET = 1184
        STOCK_CETV = 1185
        STOCK_CETX = 1186
        STOCK_CETXP = 1187
        STOCK_CETXW = 1188
        STOCK_CEV = 1189
        STOCK_CEVA = 1190
        STOCK_CEY = 1191
        STOCK_CEZ = 1192
        STOCK_CF = 1193
        STOCK_CFA = 1194
        STOCK_CFBI = 1195
        STOCK_CFBK = 1196
        STOCK_CFCO = 1197
        STOCK_CFCOU = 1198
        STOCK_CFCOW = 1199
        STOCK_CFC_B = 1200
        STOCK_CFFI = 1201
        STOCK_CFFN = 1202
        STOCK_CFG = 1203
        STOCK_CFMS = 1204
        STOCK_CFNB = 1205
        STOCK_CFO = 1206
        STOCK_CFR = 1207
        STOCK_CFRX = 1208
        STOCK_CFR_A = 1209
        STOCK_CFX = 1210
        STOCK_CG = 1211
        STOCK_CGA = 1212
        STOCK_CGBD = 1213
        STOCK_CGEN = 1214
        STOCK_CGG = 1215
        STOCK_CGI = 1216
        STOCK_CGIX = 1217
        STOCK_CGNT = 1218
        STOCK_CGNX = 1219
        STOCK_CGO = 1220
        STOCK_CH = 1221
        STOCK_CHA = 1222
        STOCK_CHAD = 1223
        STOCK_CHCI = 1224
        STOCK_CHCO = 1225
        STOCK_CHCT = 1226
        STOCK_CHD = 1227
        STOCK_CHDN = 1228
        STOCK_CHE = 1229
        STOCK_CHEF = 1230
        STOCK_CHEK = 1231
        STOCK_CHEKW = 1232
        STOCK_CHFC = 1233
        STOCK_CHFN = 1234
        STOCK_CHFS = 1235
        STOCK_CHGG = 1236
        STOCK_CHGX = 1237
        STOCK_CHH = 1238
        STOCK_CHI = 1239
        STOCK_CHK = 1240
        STOCK_CHKE = 1241
        STOCK_CHKP = 1242
        STOCK_CHKR = 1243
        STOCK_CHK_D = 1244
        STOCK_CHL = 1245
        STOCK_CHMA = 1246
        STOCK_CHMG = 1247
        STOCK_CHMI = 1248
        STOCK_CHMI_A = 1249
        STOCK_CHN = 1250
        STOCK_CHNR = 1251
        STOCK_CHRS = 1252
        STOCK_CHRW = 1253
        STOCK_CHS = 1254
        STOCK_CHSCL = 1255
        STOCK_CHSCM = 1256
        STOCK_CHSCN = 1257
        STOCK_CHSCO = 1258
        STOCK_CHSCP = 1259
        STOCK_CHSP = 1260
        STOCK_CHT = 1261
        STOCK_CHTR = 1262
        STOCK_CHU = 1263
        STOCK_CHUBA = 1264
        STOCK_CHUBK = 1265
        STOCK_CHUY = 1266
        STOCK_CHW = 1267
        STOCK_CHY = 1268
        STOCK_CI = 1269
        STOCK_CIA = 1270
        STOCK_CIB = 1271
        STOCK_CIBR = 1272
        STOCK_CIC__U = 1273
        STOCK_CIC__WS = 1274
        STOCK_CIC = 1275
        STOCK_CID = 1276
        STOCK_CIDM = 1277
        STOCK_CIE = 1278
        STOCK_CIEN = 1279
        STOCK_CIF = 1280
        STOCK_CIFS = 1281
        STOCK_CIG__C = 1282
        STOCK_CIG = 1283
        STOCK_CIGI = 1284
        STOCK_CII = 1285
        STOCK_CIK = 1286
        STOCK_CIL = 1287
        STOCK_CIM = 1288
        STOCK_CIM_A = 1289
        STOCK_CIM_B = 1290
        STOCK_CINF = 1291
        STOCK_CINR = 1292
        STOCK_CIO = 1293
        STOCK_CIO_A = 1294
        STOCK_CIR = 1295
        STOCK_CISN__WS = 1296
        STOCK_CISN = 1297
        STOCK_CIT = 1298
        STOCK_CIVB = 1299
        STOCK_CIVBP = 1300
        STOCK_CIVI = 1301
        STOCK_CIX = 1302
        STOCK_CIZ = 1303
        STOCK_CIZN = 1304
        STOCK_CJ = 1305
        STOCK_CJJD = 1306
        STOCK_CKH = 1307
        STOCK_CKPT = 1308
        STOCK_CKX = 1309
        STOCK_CL = 1310
        STOCK_CLAR = 1311
        STOCK_CLB = 1312
        STOCK_CLBS = 1313
        STOCK_CLCT = 1314
        STOCK_CLD = 1315
        STOCK_CLDC = 1316
        STOCK_CLDR = 1317
        STOCK_CLDT = 1318
        STOCK_CLDX = 1319
        STOCK_CLF = 1320
        STOCK_CLFD = 1321
        STOCK_CLGX = 1322
        STOCK_CLH = 1323
        STOCK_CLI = 1324
        STOCK_CLIR = 1325
        STOCK_CLIRW = 1326
        STOCK_CLLS = 1327
        STOCK_CLM = 1328
        STOCK_CLMT = 1329
        STOCK_CLNE = 1330
        STOCK_CLNS = 1331
        STOCK_CLNS_B = 1332
        STOCK_CLNS_C__CL = 1333
        STOCK_CLNS_D = 1334
        STOCK_CLNS_E = 1335
        STOCK_CLNS_G = 1336
        STOCK_CLNS_H = 1337
        STOCK_CLNS_I = 1338
        STOCK_CLNS_J = 1339
        STOCK_CLNT = 1340
        STOCK_CLPR = 1341
        STOCK_CLR = 1342
        STOCK_CLRB = 1343
        STOCK_CLRBW = 1344
        STOCK_CLRBZ = 1345
        STOCK_CLRO = 1346
        STOCK_CLS = 1347
        STOCK_CLSD = 1348
        STOCK_CLSN = 1349
        STOCK_CLTL = 1350
        STOCK_CLUB = 1351
        STOCK_CLVS = 1352
        STOCK_CLW = 1353
        STOCK_CLWT = 1354
        STOCK_CLX = 1355
        STOCK_CLXT = 1356
        STOCK_CLYH = 1357
        STOCK_CM = 1358
        STOCK_CMA__WS = 1359
        STOCK_CMA = 1360
        STOCK_CMC = 1361
        STOCK_CMCL = 1362
        STOCK_CMCM = 1363
        STOCK_CMCO = 1364
        STOCK_CMCSA = 1365
        STOCK_CMCT = 1366
        STOCK_CMD = 1367
        STOCK_CME = 1368
        STOCK_CMFN = 1369
        STOCK_CMG = 1370
        STOCK_CMI = 1371
        STOCK_CMLS = 1372
        STOCK_CMO = 1373
        STOCK_CMO_E = 1374
        STOCK_CMP = 1375
        STOCK_CMPR = 1376
        STOCK_CMRE = 1377
        STOCK_CMRE_B = 1378
        STOCK_CMRE_C = 1379
        STOCK_CMRE_D = 1380
        STOCK_CMRX = 1381
        STOCK_CMS = 1382
        STOCK_CMSS = 1383
        STOCK_CMSSR = 1384
        STOCK_CMSSU = 1385
        STOCK_CMSSW = 1386
        STOCK_CMS_B = 1387
        STOCK_CMT = 1388
        STOCK_CMTA = 1389
        STOCK_CMTL = 1390
        STOCK_CMU = 1391
        STOCK_CNA = 1392
        STOCK_CNAC = 1393
        STOCK_CNACR = 1394
        STOCK_CNACU = 1395
        STOCK_CNACW = 1396
        STOCK_CNAT = 1397
        STOCK_CNBKA = 1398
        STOCK_CNC = 1399
        STOCK_CNCE = 1400
        STOCK_CNCR = 1401
        STOCK_CNDF = 1402
        STOCK_CNDT = 1403
        STOCK_CNET = 1404
        STOCK_CNFR = 1405
        STOCK_CNHI = 1406
        STOCK_CNHX = 1407
        STOCK_CNI = 1408
        STOCK_CNIT = 1409
        STOCK_CNK = 1410
        STOCK_CNMD = 1411
        STOCK_CNNX = 1412
        STOCK_CNO = 1413
        STOCK_CNOB = 1414
        STOCK_CNP = 1415
        STOCK_CNQ = 1416
        STOCK_CNS = 1417
        STOCK_CNSF = 1418
        STOCK_CNSL = 1419
        STOCK_CNTF = 1420
        STOCK_CNTY = 1421
        STOCK_CNX = 1422
        STOCK_CNXC = 1423
        STOCK_CNXN = 1424
        STOCK_CNXR = 1425
        STOCK_CNYA = 1426
        STOCK_CO = 1427
        STOCK_COBZ = 1428
        STOCK_CODA = 1429
        STOCK_CODI = 1430
        STOCK_CODI_A = 1431
        STOCK_CODX = 1432
        STOCK_COE = 1433
        STOCK_COF__WS = 1434
        STOCK_COF = 1435
        STOCK_COF_C = 1436
        STOCK_COF_D = 1437
        STOCK_COF_F = 1438
        STOCK_COF_G = 1439
        STOCK_COF_H = 1440
        STOCK_COF_P = 1441
        STOCK_COG = 1442
        STOCK_COGT = 1443
        STOCK_COHN = 1444
        STOCK_COHR = 1445
        STOCK_COHU = 1446
        STOCK_COKE = 1447
        STOCK_COL = 1448
        STOCK_COLB = 1449
        STOCK_COLL = 1450
        STOCK_COLM = 1451
        STOCK_COM = 1452
        STOCK_COMB = 1453
        STOCK_COMG = 1454
        STOCK_COMM = 1455
        STOCK_CONE = 1456
        STOCK_CONN = 1457
        STOCK_COO = 1458
        STOCK_COOL = 1459
        STOCK_COP = 1460
        STOCK_COR = 1461
        STOCK_CORE = 1462
        STOCK_CORI = 1463
        STOCK_CORR = 1464
        STOCK_CORR_A = 1465
        STOCK_CORT = 1466
        STOCK_COR_A__CL = 1467
        STOCK_COR_A = 1468
        STOCK_COST = 1469
        STOCK_COT = 1470
        STOCK_COTV = 1471
        STOCK_COTY = 1472
        STOCK_COUP = 1473
        STOCK_COWN = 1474
        STOCK_COWNL = 1475
        STOCK_COWZ = 1476
        STOCK_CP = 1477
        STOCK_CPA = 1478
        STOCK_CPAC = 1479
        STOCK_CPAH = 1480
        STOCK_CPB = 1481
        STOCK_CPE = 1482
        STOCK_CPE_A = 1483
        STOCK_CPF = 1484
        STOCK_CPG = 1485
        STOCK_CPHC = 1486
        STOCK_CPHI = 1487
        STOCK_CPIX = 1488
        STOCK_CPK = 1489
        STOCK_CPL = 1490
        STOCK_CPLA = 1491
        STOCK_CPLP = 1492
        STOCK_CPN = 1493
        STOCK_CPRT = 1494
        STOCK_CPRX = 1495
        STOCK_CPS = 1496
        STOCK_CPSH = 1497
        STOCK_CPSI = 1498
        STOCK_CPSS = 1499
        STOCK_CPST = 1500
        STOCK_CPT = 1501
        STOCK_CPTA = 1502
        STOCK_CPTAG = 1503
        STOCK_CPTAL = 1504
        STOCK_CQH = 1505
        STOCK_CQP = 1506
        STOCK_CR = 1507
        STOCK_CRAI = 1508
        STOCK_CRAK = 1509
        STOCK_CRAY = 1510
        STOCK_CRBP = 1511
        STOCK_CRC = 1512
        STOCK_CRCM = 1513
        STOCK_CRD__A = 1514
        STOCK_CRD__B = 1515
        STOCK_CREE = 1516
        STOCK_CREG = 1517
        STOCK_CRESY = 1518
        STOCK_CRF = 1519
        STOCK_CRH = 1520
        STOCK_CRHM = 1521
        STOCK_CRI = 1522
        STOCK_CRIS = 1523
        STOCK_CRK = 1524
        STOCK_CRL = 1525
        STOCK_CRM = 1526
        STOCK_CRMD = 1527
        STOCK_CRME = 1528
        STOCK_CRMT = 1529
        STOCK_CRNT = 1530
        STOCK_CROX = 1531
        STOCK_CRR = 1532
        STOCK_CRS = 1533
        STOCK_CRSP = 1534
        STOCK_CRT = 1535
        STOCK_CRTN = 1536
        STOCK_CRTO = 1537
        STOCK_CRUS = 1538
        STOCK_CRVL = 1539
        STOCK_CRVP = 1540
        STOCK_CRVS = 1541
        STOCK_CRWS = 1542
        STOCK_CRY = 1543
        STOCK_CRZO = 1544
        STOCK_CS = 1545
        STOCK_CSA = 1546
        STOCK_CSB = 1547
        STOCK_CSBK = 1548
        STOCK_CSBR = 1549
        STOCK_CSCO = 1550
        STOCK_CSF = 1551
        STOCK_CSFL = 1552
        STOCK_CSGP = 1553
        STOCK_CSGS = 1554
        STOCK_CSII = 1555
        STOCK_CSIQ = 1556
        STOCK_CSL = 1557
        STOCK_CSLT = 1558
        STOCK_CSML = 1559
        STOCK_CSOD = 1560
        STOCK_CSPI = 1561
        STOCK_CSQ = 1562
        STOCK_CSRA = 1563
        STOCK_CSS = 1564
        STOCK_CSSE = 1565
        STOCK_CSTE = 1566
        STOCK_CSTM = 1567
        STOCK_CSTR = 1568
        STOCK_CSU = 1569
        STOCK_CSV = 1570
        STOCK_CSWC = 1571
        STOCK_CSWI = 1572
        STOCK_CSX = 1573
        STOCK_CTAA = 1574
        STOCK_CTAS = 1575
        STOCK_CTB = 1576
        STOCK_CTBB = 1577
        STOCK_CTBI = 1578
        STOCK_CTDD = 1579
        STOCK_CTEK = 1580
        STOCK_CTG = 1581
        STOCK_CTHR = 1582
        STOCK_CTIB = 1583
        STOCK_CTIC = 1584
        STOCK_CTL = 1585
        STOCK_CTLT = 1586
        STOCK_CTMX = 1587
        STOCK_CTO = 1588
        STOCK_CTR = 1589
        STOCK_CTRE = 1590
        STOCK_CTRL = 1591
        STOCK_CTRN = 1592
        STOCK_CTRP = 1593
        STOCK_CTRV = 1594
        STOCK_CTS = 1595
        STOCK_CTSH = 1596
        STOCK_CTSO = 1597
        STOCK_CTT = 1598
        STOCK_CTU = 1599
        STOCK_CTV = 1600
        STOCK_CTW = 1601
        STOCK_CTWS = 1602
        STOCK_CTX = 1603
        STOCK_CTXR = 1604
        STOCK_CTXRW = 1605
        STOCK_CTXS = 1606
        STOCK_CTY = 1607
        STOCK_CTZ = 1608
        STOCK_CUB = 1609
        STOCK_CUBA = 1610
        STOCK_CUBE = 1611
        STOCK_CUBI = 1612
        STOCK_CUBI_C = 1613
        STOCK_CUBI_D = 1614
        STOCK_CUBI_E = 1615
        STOCK_CUBI_F = 1616
        STOCK_CUBN = 1617
        STOCK_CUBS = 1618
        STOCK_CUDA = 1619
        STOCK_CUI = 1620
        STOCK_CUK = 1621
        STOCK_CULP = 1622
        STOCK_CUMB = 1623
        STOCK_CUNB = 1624
        STOCK_CUO = 1625
        STOCK_CUR = 1626
        STOCK_CUTR = 1627
        STOCK_CUZ = 1628
        STOCK_CVA = 1629
        STOCK_CVBF = 1630
        STOCK_CVCO = 1631
        STOCK_CVCY = 1632
        STOCK_CVE = 1633
        STOCK_CVEO = 1634
        STOCK_CVG = 1635
        STOCK_CVGI = 1636
        STOCK_CVGW = 1637
        STOCK_CVI = 1638
        STOCK_CVLT = 1639
        STOCK_CVLY = 1640
        STOCK_CVM__WS = 1641
        STOCK_CVM = 1642
        STOCK_CVNA = 1643
        STOCK_CVO = 1644
        STOCK_CVR = 1645
        STOCK_CVRR = 1646
        STOCK_CVRS = 1647
        STOCK_CVS = 1648
        STOCK_CVTI = 1649
        STOCK_CVU = 1650
        STOCK_CVV = 1651
        STOCK_CVX = 1652
        STOCK_CW = 1653
        STOCK_CWAI = 1654
        STOCK_CWAY = 1655
        STOCK_CWBC = 1656
        STOCK_CWCO = 1657
        STOCK_CWEB = 1658
        STOCK_CWH = 1659
        STOCK_CWS = 1660
        STOCK_CWST = 1661
        STOCK_CWT = 1662
        STOCK_CX = 1663
        STOCK_CXDC = 1664
        STOCK_CXE = 1665
        STOCK_CXH = 1666
        STOCK_CXO = 1667
        STOCK_CXP = 1668
        STOCK_CXRX = 1669
        STOCK_CXSE = 1670
        STOCK_CXW = 1671
        STOCK_CY = 1672
        STOCK_CYAD = 1673
        STOCK_CYAN = 1674
        STOCK_CYBE = 1675
        STOCK_CYBR = 1676
        STOCK_CYCC = 1677
        STOCK_CYCCP = 1678
        STOCK_CYD = 1679
        STOCK_CYH = 1680
        STOCK_CYHHZ = 1681
        STOCK_CYOU = 1682
        STOCK_CYRN = 1683
        STOCK_CYRX = 1684
        STOCK_CYRXW = 1685
        STOCK_CYS = 1686
        STOCK_CYS_A = 1687
        STOCK_CYS_B = 1688
        STOCK_CYTK = 1689
        STOCK_CYTR = 1690
        STOCK_CYTX = 1691
        STOCK_CYTXW = 1692
        STOCK_CZFC = 1693
        STOCK_CZNC = 1694
        STOCK_CZR = 1695
        STOCK_CZWI = 1696
        STOCK_CZZ = 1697
        STOCK_C_C = 1698
        STOCK_C_J = 1699
        STOCK_C_K = 1700
        STOCK_C_L = 1701
        STOCK_C_N = 1702
        STOCK_C_P = 1703
        STOCK_C_S = 1704
        STOCK_D = 1705
        STOCK_DAC = 1706
        STOCK_DAIO = 1707
        STOCK_DAKT = 1708
        STOCK_DAL = 1709
        STOCK_DALT = 1710
        STOCK_DAN = 1711
        STOCK_DAR = 1712
        STOCK_DARE = 1713
        STOCK_DATA = 1714
        STOCK_DAVE = 1715
        STOCK_DAX = 1716
        STOCK_DB = 1717
        STOCK_DBD = 1718
        STOCK_DBES = 1719
        STOCK_DBIT = 1720
        STOCK_DBL = 1721
        STOCK_DBRT = 1722
        STOCK_DBVT = 1723
        STOCK_DCF = 1724
        STOCK_DCI = 1725
        STOCK_DCIX = 1726
        STOCK_DCM = 1727
        STOCK_DCO = 1728
        STOCK_DCOM = 1729
        STOCK_DCP = 1730
        STOCK_DCPH = 1731
        STOCK_DCT = 1732
        STOCK_DCUD = 1733
        STOCK_DD = 1734
        STOCK_DDBI = 1735
        STOCK_DDC = 1736
        STOCK_DDD = 1737
        STOCK_DDE = 1738
        STOCK_DDEZ = 1739
        STOCK_DDF = 1740
        STOCK_DDJP = 1741
        STOCK_DDLS = 1742
        STOCK_DDR = 1743
        STOCK_DDR_A = 1744
        STOCK_DDR_J = 1745
        STOCK_DDR_K = 1746
        STOCK_DDS = 1747
        STOCK_DDT = 1748
        STOCK_DDWM = 1749
        STOCK_DD_A = 1750
        STOCK_DD_B = 1751
        STOCK_DE = 1752
        STOCK_DEA = 1753
        STOCK_DECK = 1754
        STOCK_DEEF = 1755
        STOCK_DEFA = 1756
        STOCK_DEI = 1757
        STOCK_DEL = 1758
        STOCK_DELT = 1759
        STOCK_DELTW = 1760
        STOCK_DEMG = 1761
        STOCK_DEMS = 1762
        STOCK_DENN = 1763
        STOCK_DEO = 1764
        STOCK_DEPO = 1765
        STOCK_DERM = 1766
        STOCK_DESC = 1767
        STOCK_DESP = 1768
        STOCK_DEST = 1769
        STOCK_DEUS = 1770
        STOCK_DEWJ = 1771
        STOCK_DEX = 1772
        STOCK_DEZU = 1773
        STOCK_DF = 1774
        STOCK_DFBG = 1775
        STOCK_DFEN = 1776
        STOCK_DFFN = 1777
        STOCK_DFIN = 1778
        STOCK_DFND = 1779
        STOCK_DFNL = 1780
        STOCK_DFP = 1781
        STOCK_DFRG = 1782
        STOCK_DFS = 1783
        STOCK_DFS_B__CL = 1784
        STOCK_DFS_B = 1785
        STOCK_DFVL = 1786
        STOCK_DFVS = 1787
        STOCK_DG = 1788
        STOCK_DGICA = 1789
        STOCK_DGICB = 1790
        STOCK_DGII = 1791
        STOCK_DGLT = 1792
        STOCK_DGLY = 1793
        STOCK_DGSE = 1794
        STOCK_DGX = 1795
        STOCK_DHDG = 1796
        STOCK_DHF = 1797
        STOCK_DHG = 1798
        STOCK_DHI = 1799
        STOCK_DHIL = 1800
        STOCK_DHR = 1801
        STOCK_DHT = 1802
        STOCK_DHVW = 1803
        STOCK_DHX = 1804
        STOCK_DHXM = 1805
        STOCK_DHY = 1806
        STOCK_DIAL = 1807
        STOCK_DIAX = 1808
        STOCK_DIN = 1809
        STOCK_DIOD = 1810
        STOCK_DIS = 1811
        STOCK_DISCA = 1812
        STOCK_DISCB = 1813
        STOCK_DISCK = 1814
        STOCK_DISH = 1815
        STOCK_DIT = 1816
        STOCK_DIVA = 1817
        STOCK_DIVB = 1818
        STOCK_DIVO = 1819
        STOCK_DIVY = 1820
        STOCK_DJCO = 1821
        STOCK_DJD = 1822
        STOCK_DK = 1823
        STOCK_DKL = 1824
        STOCK_DKS = 1825
        STOCK_DKT = 1826
        STOCK_DL = 1827
        STOCK_DLA = 1828
        STOCK_DLB = 1829
        STOCK_DLBL = 1830
        STOCK_DLBR = 1831
        STOCK_DLBS = 1832
        STOCK_DLHC = 1833
        STOCK_DLNG = 1834
        STOCK_DLNG_A = 1835
        STOCK_DLPH = 1836
        STOCK_DLR = 1837
        STOCK_DLR_C = 1838
        STOCK_DLR_G = 1839
        STOCK_DLR_H = 1840
        STOCK_DLR_I = 1841
        STOCK_DLR_J = 1842
        STOCK_DLTH = 1843
        STOCK_DLTR = 1844
        STOCK_DLX = 1845
        STOCK_DM = 1846
        STOCK_DMB = 1847
        STOCK_DMF = 1848
        STOCK_DMLP = 1849
        STOCK_DMO = 1850
        STOCK_DMPI = 1851
        STOCK_DMRC = 1852
        STOCK_DMRI = 1853
        STOCK_DMRL = 1854
        STOCK_DMTX = 1855
        STOCK_DNB = 1856
        STOCK_DNBF = 1857
        STOCK_DNI = 1858
        STOCK_DNKN = 1859
        STOCK_DNN = 1860
        STOCK_DNOW = 1861
        STOCK_DNP = 1862
        STOCK_DNR = 1863
        STOCK_DO = 1864
        STOCK_DOC = 1865
        STOCK_DOOR = 1866
        STOCK_DORM = 1867
        STOCK_DOTA = 1868
        STOCK_DOTAR = 1869
        STOCK_DOTAU = 1870
        STOCK_DOTAW = 1871
        STOCK_DOV = 1872
        STOCK_DOVA = 1873
        STOCK_DOX = 1874
        STOCK_DPG = 1875
        STOCK_DPLO = 1876
        STOCK_DPS = 1877
        STOCK_DPST = 1878
        STOCK_DPW = 1879
        STOCK_DPZ = 1880
        STOCK_DQ = 1881
        STOCK_DRAD = 1882
        STOCK_DRD = 1883
        STOCK_DRE = 1884
        STOCK_DRH = 1885
        STOCK_DRI = 1886
        STOCK_DRIO = 1887
        STOCK_DRIOW = 1888
        STOCK_DRNA = 1889
        STOCK_DRQ = 1890
        STOCK_DRRX = 1891
        STOCK_DRUA = 1892
        STOCK_DRYS = 1893
        STOCK_DS = 1894
        STOCK_DSE = 1895
        STOCK_DSGX = 1896
        STOCK_DSKE = 1897
        STOCK_DSKEW = 1898
        STOCK_DSL = 1899
        STOCK_DSM = 1900
        STOCK_DSPG = 1901
        STOCK_DSS = 1902
        STOCK_DST = 1903
        STOCK_DSU = 1904
        STOCK_DSW = 1905
        STOCK_DSWL = 1906
        STOCK_DSX = 1907
        STOCK_DSXN = 1908
        STOCK_DSX_B = 1909
        STOCK_DS_B = 1910
        STOCK_DS_C = 1911
        STOCK_DS_D = 1912
        STOCK_DTE = 1913
        STOCK_DTEA = 1914
        STOCK_DTF = 1915
        STOCK_DTJ = 1916
        STOCK_DTK = 1917
        STOCK_DTLA_ = 1918
        STOCK_DTQ = 1919
        STOCK_DTRM = 1920
        STOCK_DTUL = 1921
        STOCK_DTUS = 1922
        STOCK_DTV = 1923
        STOCK_DTY = 1924
        STOCK_DTYL = 1925
        STOCK_DTYS = 1926
        STOCK_DUC = 1927
        STOCK_DUK = 1928
        STOCK_DUKH = 1929
        STOCK_DUSA = 1930
        STOCK_DUSL = 1931
        STOCK_DVA = 1932
        STOCK_DVAX = 1933
        STOCK_DVCR = 1934
        STOCK_DVD = 1935
        STOCK_DVEM = 1936
        STOCK_DVMT = 1937
        STOCK_DVN = 1938
        STOCK_DVP = 1939
        STOCK_DWAC = 1940
        STOCK_DWAQ = 1941
        STOCK_DWAS = 1942
        STOCK_DWAT = 1943
        STOCK_DWCH = 1944
        STOCK_DWDP = 1945
        STOCK_DWFI = 1946
        STOCK_DWIN = 1947
        STOCK_DWLD = 1948
        STOCK_DWLV = 1949
        STOCK_DWPP = 1950
        STOCK_DWSN = 1951
        STOCK_DWT = 1952
        STOCK_DWTR = 1953
        STOCK_DX = 1954
        STOCK_DXB = 1955
        STOCK_DXC = 1956
        STOCK_DXCM = 1957
        STOCK_DXLG = 1958
        STOCK_DXPE = 1959
        STOCK_DXR = 1960
        STOCK_DXTR = 1961
        STOCK_DXUS = 1962
        STOCK_DXYN = 1963
        STOCK_DX_A = 1964
        STOCK_DX_B = 1965
        STOCK_DY = 1966
        STOCK_DYB = 1967
        STOCK_DYLS = 1968
        STOCK_DYN__WS__A = 1969
        STOCK_DYN = 1970
        STOCK_DYNC = 1971
        STOCK_DYNT = 1972
        STOCK_DYN_A = 1973
        STOCK_DYSL = 1974
        STOCK_DZSI = 1975
        STOCK_E = 1976
        STOCK_EA = 1977
        STOCK_EAB = 1978
        STOCK_EACQ = 1979
        STOCK_EACQU = 1980
        STOCK_EACQW = 1981
        STOCK_EAD = 1982
        STOCK_EAE = 1983
        STOCK_EAGL = 1984
        STOCK_EAGLU = 1985
        STOCK_EAGLW = 1986
        STOCK_EAI = 1987
        STOCK_EARN = 1988
        STOCK_EARS = 1989
        STOCK_EAT = 1990
        STOCK_EBAY = 1991
        STOCK_EBAYL = 1992
        STOCK_EBF = 1993
        STOCK_EBIO = 1994
        STOCK_EBIX = 1995
        STOCK_EBMT = 1996
        STOCK_EBR__B = 1997
        STOCK_EBR = 1998
        STOCK_EBS = 1999
        STOCK_EBSB = 2000
        STOCK_EBTC = 2001
        STOCK_EC = 2002
        STOCK_ECA = 2003
        STOCK_ECC = 2004
        STOCK_ECCA = 2005
        STOCK_ECCB = 2006
        STOCK_ECCY = 2007
        STOCK_ECCZ = 2008
        STOCK_ECF = 2009
        STOCK_ECF_A = 2010
        STOCK_ECHO = 2011
        STOCK_ECL = 2012
        STOCK_ECOL = 2013
        STOCK_ECOM = 2014
        STOCK_ECPG = 2015
        STOCK_ECR = 2016
        STOCK_ECT = 2017
        STOCK_ECYT = 2018
        STOCK_ED = 2019
        STOCK_EDAP = 2020
        STOCK_EDBI = 2021
        STOCK_EDD = 2022
        STOCK_EDF = 2023
        STOCK_EDGE = 2024
        STOCK_EDGW = 2025
        STOCK_EDI = 2026
        STOCK_EDIT = 2027
        STOCK_EDN = 2028
        STOCK_EDOM = 2029
        STOCK_EDOW = 2030
        STOCK_EDR = 2031
        STOCK_EDU = 2032
        STOCK_EDUC = 2033
        STOCK_EE = 2034
        STOCK_EEA = 2035
        STOCK_EEFT = 2036
        STOCK_EEI = 2037
        STOCK_EEMO = 2038
        STOCK_EEMX = 2039
        STOCK_EEP = 2040
        STOCK_EEQ = 2041
        STOCK_EEX = 2042
        STOCK_EFAS = 2043
        STOCK_EFAX = 2044
        STOCK_EFBI = 2045
        STOCK_EFC = 2046
        STOCK_EFF = 2047
        STOCK_EFII = 2048
        STOCK_EFL = 2049
        STOCK_EFNL = 2050
        STOCK_EFOI = 2051
        STOCK_EFR = 2052
        STOCK_EFSC = 2053
        STOCK_EFT = 2054
        STOCK_EFX = 2055
        STOCK_EGAN = 2056
        STOCK_EGBN = 2057
        STOCK_EGF = 2058
        STOCK_EGHT = 2059
        STOCK_EGI = 2060
        STOCK_EGIF = 2061
        STOCK_EGL = 2062
        STOCK_EGLE = 2063
        STOCK_EGLT = 2064
        STOCK_EGN = 2065
        STOCK_EGO = 2066
        STOCK_EGOV = 2067
        STOCK_EGP = 2068
        STOCK_EGRX = 2069
        STOCK_EGY = 2070
        STOCK_EHI = 2071
        STOCK_EHIC = 2072
        STOCK_EHR = 2073
        STOCK_EHT = 2074
        STOCK_EHTH = 2075
        STOCK_EIA = 2076
        STOCK_EIG = 2077
        STOCK_EIGI = 2078
        STOCK_EIGR = 2079
        STOCK_EIM = 2080
        STOCK_EIO = 2081
        STOCK_EIP = 2082
        STOCK_EIV = 2083
        STOCK_EIX = 2084
        STOCK_EKSO = 2085
        STOCK_EL = 2086
        STOCK_ELC = 2087
        STOCK_ELEC = 2088
        STOCK_ELECU = 2089
        STOCK_ELECW = 2090
        STOCK_ELF = 2091
        STOCK_ELGX = 2092
        STOCK_ELJ = 2093
        STOCK_ELLI = 2094
        STOCK_ELLO = 2095
        STOCK_ELMD = 2096
        STOCK_ELON = 2097
        STOCK_ELP = 2098
        STOCK_ELS = 2099
        STOCK_ELSE = 2100
        STOCK_ELTK = 2101
        STOCK_ELU = 2102
        STOCK_ELVT = 2103
        STOCK_ELY = 2104
        STOCK_EMAN = 2105
        STOCK_EMBH = 2106
        STOCK_EMBU = 2107
        STOCK_EMCF = 2108
        STOCK_EMCI = 2109
        STOCK_EMD = 2110
        STOCK_EMDV = 2111
        STOCK_EME = 2112
        STOCK_EMES = 2113
        STOCK_EMF = 2114
        STOCK_EMGF = 2115
        STOCK_EMHY = 2116
        STOCK_EMI = 2117
        STOCK_EMITF = 2118
        STOCK_EMJ = 2119
        STOCK_EMKR = 2120
        STOCK_EML = 2121
        STOCK_EMMS = 2122
        STOCK_EMN = 2123
        STOCK_EMO = 2124
        STOCK_EMP = 2125
        STOCK_EMQQ = 2126
        STOCK_EMR = 2127
        STOCK_EMSD = 2128
        STOCK_EMTL = 2129
        STOCK_EMX = 2130
        STOCK_EMXC = 2131
        STOCK_ENB = 2132
        STOCK_ENBL = 2133
        STOCK_ENDP = 2134
        STOCK_ENFC = 2135
        STOCK_ENG = 2136
        STOCK_ENH_C = 2137
        STOCK_ENIA = 2138
        STOCK_ENIC = 2139
        STOCK_ENJ = 2140
        STOCK_ENLC = 2141
        STOCK_ENLK = 2142
        STOCK_ENO = 2143
        STOCK_ENOR = 2144
        STOCK_ENPH = 2145
        STOCK_ENR = 2146
        STOCK_ENRJ = 2147
        STOCK_ENS = 2148
        STOCK_ENSG = 2149
        STOCK_ENSV = 2150
        STOCK_ENT = 2151
        STOCK_ENTA = 2152
        STOCK_ENTG = 2153
        STOCK_ENTL = 2154
        STOCK_ENTR = 2155
        STOCK_ENV = 2156
        STOCK_ENVA = 2157
        STOCK_ENX = 2158
        STOCK_ENZ = 2159
        STOCK_ENZY = 2160
        STOCK_EOCC = 2161
        STOCK_EOD = 2162
        STOCK_EOG = 2163
        STOCK_EOI = 2164
        STOCK_EOS = 2165
        STOCK_EOT = 2166
        STOCK_EPAM = 2167
        STOCK_EPAY = 2168
        STOCK_EPC = 2169
        STOCK_EPD = 2170
        STOCK_EPE = 2171
        STOCK_EPIX = 2172
        STOCK_EPM = 2173
        STOCK_EPR = 2174
        STOCK_EPRF = 2175
        STOCK_EPR_C = 2176
        STOCK_EPR_E = 2177
        STOCK_EPR_F = 2178
        STOCK_EPZM = 2179
        STOCK_EP_C = 2180
        STOCK_EQBK = 2181
        STOCK_EQC = 2182
        STOCK_EQCO = 2183
        STOCK_EQC_D = 2184
        STOCK_EQFN = 2185
        STOCK_EQGP = 2186
        STOCK_EQIX = 2187
        STOCK_EQM = 2188
        STOCK_EQR = 2189
        STOCK_EQRR = 2190
        STOCK_EQS = 2191
        STOCK_EQT = 2192
        STOCK_ERA = 2193
        STOCK_ERC = 2194
        STOCK_ERF = 2195
        STOCK_ERGF = 2196
        STOCK_ERH = 2197
        STOCK_ERI = 2198
        STOCK_ERIC = 2199
        STOCK_ERIE = 2200
        STOCK_ERII = 2201
        STOCK_ERJ = 2202
        STOCK_ERM = 2203
        STOCK_ERN = 2204
        STOCK_EROS = 2205
        STOCK_ERYP = 2206
        STOCK_ES = 2207
        STOCK_ESBA = 2208
        STOCK_ESBK = 2209
        STOCK_ESCA = 2210
        STOCK_ESDI = 2211
        STOCK_ESDIW = 2212
        STOCK_ESE = 2213
        STOCK_ESEA = 2214
        STOCK_ESES = 2215
        STOCK_ESG = 2216
        STOCK_ESGD = 2217
        STOCK_ESGE = 2218
        STOCK_ESGF = 2219
        STOCK_ESGG = 2220
        STOCK_ESGL = 2221
        STOCK_ESGN = 2222
        STOCK_ESGR = 2223
        STOCK_ESGS = 2224
        STOCK_ESGU = 2225
        STOCK_ESGW = 2226
        STOCK_ESIO = 2227
        STOCK_ESL = 2228
        STOCK_ESLT = 2229
        STOCK_ESNC = 2230
        STOCK_ESND = 2231
        STOCK_ESNT = 2232
        STOCK_ESP = 2233
        STOCK_ESPR = 2234
        STOCK_ESQ = 2235
        STOCK_ESRT = 2236
        STOCK_ESRX = 2237
        STOCK_ESS = 2238
        STOCK_ESSA = 2239
        STOCK_ESTE = 2240
        STOCK_ESV = 2241
        STOCK_ESXB = 2242
        STOCK_ETB = 2243
        STOCK_ETE = 2244
        STOCK_ETFC = 2245
        STOCK_ETG = 2246
        STOCK_ETH = 2247
        STOCK_ETHO = 2248
        STOCK_ETJ = 2249
        STOCK_ETM = 2250
        STOCK_ETMW = 2251
        STOCK_ETN = 2252
        STOCK_ETO = 2253
        STOCK_ETP = 2254
        STOCK_ETR = 2255
        STOCK_ETSY = 2256
        STOCK_ETV = 2257
        STOCK_ETW = 2258
        STOCK_ETX = 2259
        STOCK_ETY = 2260
        STOCK_EUDV = 2261
        STOCK_EUFL = 2262
        STOCK_EURN = 2263
        STOCK_EURZ = 2264
        STOCK_EUXL = 2265
        STOCK_EV = 2266
        STOCK_EVA = 2267
        STOCK_EVAR = 2268
        STOCK_EVBG = 2269
        STOCK_EVBN = 2270
        STOCK_EVC = 2271
        STOCK_EVEP = 2272
        STOCK_EVF = 2273
        STOCK_EVG = 2274
        STOCK_EVGBC = 2275
        STOCK_EVGN = 2276
        STOCK_EVH = 2277
        STOCK_EVHC = 2278
        STOCK_EVI = 2279
        STOCK_EVIX = 2280
        STOCK_EVJ = 2281
        STOCK_EVK = 2282
        STOCK_EVLMC = 2283
        STOCK_EVLV = 2284
        STOCK_EVM = 2285
        STOCK_EVN = 2286
        STOCK_EVO = 2287
        STOCK_EVOK = 2288
        STOCK_EVOL = 2289
        STOCK_EVP = 2290
        STOCK_EVR = 2291
        STOCK_EVRI = 2292
        STOCK_EVSTC = 2293
        STOCK_EVT = 2294
        STOCK_EVTC = 2295
        STOCK_EVV = 2296
        STOCK_EVY = 2297
        STOCK_EW = 2298
        STOCK_EWBC = 2299
        STOCK_EWGS = 2300
        STOCK_EWMC = 2301
        STOCK_EWRE = 2302
        STOCK_EWSC = 2303
        STOCK_EWUS = 2304
        STOCK_EXA = 2305
        STOCK_EXAC = 2306
        STOCK_EXAS = 2307
        STOCK_EXC = 2308
        STOCK_EXD = 2309
        STOCK_EXEL = 2310
        STOCK_EXFO = 2311
        STOCK_EXG = 2312
        STOCK_EXIV = 2313
        STOCK_EXK = 2314
        STOCK_EXLS = 2315
        STOCK_EXP = 2316
        STOCK_EXPD = 2317
        STOCK_EXPE = 2318
        STOCK_EXPO = 2319
        STOCK_EXPR = 2320
        STOCK_EXR = 2321
        STOCK_EXTN = 2322
        STOCK_EXTR = 2323
        STOCK_EXXI = 2324
        STOCK_EYE = 2325
        STOCK_EYEG = 2326
        STOCK_EYEGW = 2327
        STOCK_EYES = 2328
        STOCK_EYESW = 2329
        STOCK_EYLD = 2330
        STOCK_EZPW = 2331
        STOCK_EZT = 2332
        STOCK_F = 2333
        STOCK_FAAR = 2334
        STOCK_FAC = 2335
        STOCK_FAF = 2336
        STOCK_FALN = 2337
        STOCK_FANG = 2338
        STOCK_FANH = 2339
        STOCK_FANZ = 2340
        STOCK_FARM = 2341
        STOCK_FARO = 2342
        STOCK_FAST = 2343
        STOCK_FAT = 2344
        STOCK_FATE = 2345
        STOCK_FAX = 2346
        STOCK_FB = 2347
        STOCK_FBC = 2348
        STOCK_FBHS = 2349
        STOCK_FBIO = 2350
        STOCK_FBIZ = 2351
        STOCK_FBK = 2352
        STOCK_FBM = 2353
        STOCK_FBMS = 2354
        STOCK_FBNC = 2355
        STOCK_FBNK = 2356
        STOCK_FBP = 2357
        STOCK_FBR = 2358
        STOCK_FBSS = 2359
        STOCK_FC = 2360
        STOCK_FCAL = 2361
        STOCK_FCAP = 2362
        STOCK_FCAU = 2363
        STOCK_FCB = 2364
        STOCK_FCBC = 2365
        STOCK_FCCO = 2366
        STOCK_FCCY = 2367
        STOCK_FCE__A = 2368
        STOCK_FCEF = 2369
        STOCK_FCEL = 2370
        STOCK_FCF = 2371
        STOCK_FCFS = 2372
        STOCK_FCN = 2373
        STOCK_FCNCA = 2374
        STOCK_FCO = 2375
        STOCK_FCPT = 2376
        STOCK_FCRE = 2377
        STOCK_FCSC = 2378
        STOCK_FCVT = 2379
        STOCK_FCX = 2380
        STOCK_FDBC = 2381
        STOCK_FDC = 2382
        STOCK_FDEF = 2383
        STOCK_FDEU = 2384
        STOCK_FDLO = 2385
        STOCK_FDMO = 2386
        STOCK_FDP = 2387
        STOCK_FDRR = 2388
        STOCK_FDS = 2389
        STOCK_FDUS = 2390
        STOCK_FDVV = 2391
        STOCK_FDX = 2392
        STOCK_FE = 2393
        STOCK_FEDU = 2394
        STOCK_FEIM = 2395
        STOCK_FELE = 2396
        STOCK_FELP = 2397
        STOCK_FEN = 2398
        STOCK_FENC = 2399
        STOCK_FENG = 2400
        STOCK_FET = 2401
        STOCK_FEYE = 2402
        STOCK_FF = 2403
        STOCK_FFBC = 2404
        STOCK_FFBCW = 2405
        STOCK_FFBW = 2406
        STOCK_FFC = 2407
        STOCK_FFG = 2408
        STOCK_FFHG = 2409
        STOCK_FFHL = 2410
        STOCK_FFIC = 2411
        STOCK_FFIN = 2412
        STOCK_FFIU = 2413
        STOCK_FFIV = 2414
        STOCK_FFKT = 2415
        STOCK_FFNW = 2416
        STOCK_FFSG = 2417
        STOCK_FFTG = 2418
        STOCK_FFTI = 2419
        STOCK_FFTY = 2420
        STOCK_FFWM = 2421
        STOCK_FGBI = 2422
        STOCK_FGEN = 2423
        STOCK_FGL = 2424
        STOCK_FGP = 2425
        STOCK_FH = 2426
        STOCK_FHB = 2427
        STOCK_FHN = 2428
        STOCK_FHN_A = 2429
        STOCK_FI = 2430
        STOCK_FIBK = 2431
        STOCK_FIBR = 2432
        STOCK_FICO = 2433
        STOCK_FIEE = 2434
        STOCK_FIG = 2435
        STOCK_FIHD = 2436
        STOCK_FII = 2437
        STOCK_FINL = 2438
        STOCK_FINX = 2439
        STOCK_FIS = 2440
        STOCK_FISI = 2441
        STOCK_FISK = 2442
        STOCK_FISV = 2443
        STOCK_FIT = 2444
        STOCK_FITB = 2445
        STOCK_FITBI = 2446
        STOCK_FIV = 2447
        STOCK_FIVE = 2448
        STOCK_FIVN = 2449
        STOCK_FIX = 2450
        STOCK_FIXD = 2451
        STOCK_FIZZ = 2452
        STOCK_FL = 2453
        STOCK_FLAT = 2454
        STOCK_FLAU = 2455
        STOCK_FLBR = 2456
        STOCK_FLC = 2457
        STOCK_FLCA = 2458
        STOCK_FLCH = 2459
        STOCK_FLCO = 2460
        STOCK_FLDM = 2461
        STOCK_FLEU = 2462
        STOCK_FLEX = 2463
        STOCK_FLGB = 2464
        STOCK_FLGR = 2465
        STOCK_FLGT = 2466
        STOCK_FLHK = 2467
        STOCK_FLIC = 2468
        STOCK_FLIO = 2469
        STOCK_FLIR = 2470
        STOCK_FLJH = 2471
        STOCK_FLJP = 2472
        STOCK_FLKR = 2473
        STOCK_FLKS = 2474
        STOCK_FLL = 2475
        STOCK_FLLV = 2476
        STOCK_FLMB = 2477
        STOCK_FLMX = 2478
        STOCK_FLO = 2479
        STOCK_FLOW = 2480
        STOCK_FLQD = 2481
        STOCK_FLQE = 2482
        STOCK_FLQG = 2483
        STOCK_FLQH = 2484
        STOCK_FLQL = 2485
        STOCK_FLQM = 2486
        STOCK_FLQS = 2487
        STOCK_FLR = 2488
        STOCK_FLS = 2489
        STOCK_FLT = 2490
        STOCK_FLWS = 2491
        STOCK_FLXN = 2492
        STOCK_FLXS = 2493
        STOCK_FLY = 2494
        STOCK_FMAO = 2495
        STOCK_FMAX = 2496
        STOCK_FMBH = 2497
        STOCK_FMBI = 2498
        STOCK_FMC = 2499
        STOCK_FMCI = 2500
        STOCK_FMCIR = 2501
        STOCK_FMCIU = 2502
        STOCK_FMCIW = 2503
        STOCK_FMDG = 2504
        STOCK_FMHI = 2505
        STOCK_FMI = 2506
        STOCK_FMN = 2507
        STOCK_FMNB = 2508
        STOCK_FMO = 2509
        STOCK_FMS = 2510
        STOCK_FMSA = 2511
        STOCK_FMX = 2512
        STOCK_FN = 2513
        STOCK_FNB = 2514
        STOCK_FNBG = 2515
        STOCK_FNB_E = 2516
        STOCK_FNCF = 2517
        STOCK_FND = 2518
        STOCK_FNF = 2519
        STOCK_FNFV = 2520
        STOCK_FNG = 2521
        STOCK_FNGN = 2522
        STOCK_FNHC = 2523
        STOCK_FNJN = 2524
        STOCK_FNKO = 2525
        STOCK_FNLC = 2526
        STOCK_FNSR = 2527
        STOCK_FNTE = 2528
        STOCK_FNTEU = 2529
        STOCK_FNTEW = 2530
        STOCK_FNV = 2531
        STOCK_FNWB = 2532
        STOCK_FOANC = 2533
        STOCK_FOE = 2534
        STOCK_FOF = 2535
        STOCK_FOGO = 2536
        STOCK_FOLD = 2537
        STOCK_FOMX = 2538
        STOCK_FONR = 2539
        STOCK_FOR = 2540
        STOCK_FORD = 2541
        STOCK_FORK = 2542
        STOCK_FORM = 2543
        STOCK_FORR = 2544
        STOCK_FORTY = 2545
        STOCK_FOSL = 2546
        STOCK_FOX = 2547
        STOCK_FOXA = 2548
        STOCK_FOXF = 2549
        STOCK_FPAY = 2550
        STOCK_FPEI = 2551
        STOCK_FPH = 2552
        STOCK_FPI = 2553
        STOCK_FPI_B = 2554
        STOCK_FPP__WS = 2555
        STOCK_FPP = 2556
        STOCK_FPRX = 2557
        STOCK_FPT = 2558
        STOCK_FQAL = 2559
        STOCK_FR = 2560
        STOCK_FRA = 2561
        STOCK_FRAC = 2562
        STOCK_FRAN = 2563
        STOCK_FRBA = 2564
        STOCK_FRBK = 2565
        STOCK_FRC = 2566
        STOCK_FRC_C = 2567
        STOCK_FRC_D = 2568
        STOCK_FRC_E = 2569
        STOCK_FRC_F = 2570
        STOCK_FRC_G = 2571
        STOCK_FRC_H = 2572
        STOCK_FRD = 2573
        STOCK_FRED = 2574
        STOCK_FRGI = 2575
        STOCK_FRME = 2576
        STOCK_FRO = 2577
        STOCK_FRPH = 2578
        STOCK_FRPT = 2579
        STOCK_FRSH = 2580
        STOCK_FRSX = 2581
        STOCK_FRT = 2582
        STOCK_FRTA = 2583
        STOCK_FRT_C = 2584
        STOCK_FSAC = 2585
        STOCK_FSACU = 2586
        STOCK_FSACW = 2587
        STOCK_FSAM = 2588
        STOCK_FSB = 2589
        STOCK_FSBC = 2590
        STOCK_FSBK = 2591
        STOCK_FSBW = 2592
        STOCK_FSCT = 2593
        STOCK_FSFG = 2594
        STOCK_FSI = 2595
        STOCK_FSIC = 2596
        STOCK_FSLR = 2597
        STOCK_FSM = 2598
        STOCK_FSNN = 2599
        STOCK_FSP = 2600
        STOCK_FSS = 2601
        STOCK_FSTR = 2602
        STOCK_FSV = 2603
        STOCK_FT = 2604
        STOCK_FTAG = 2605
        STOCK_FTAI = 2606
        STOCK_FTD = 2607
        STOCK_FTEK = 2608
        STOCK_FTEO = 2609
        STOCK_FTF = 2610
        STOCK_FTFT = 2611
        STOCK_FTI = 2612
        STOCK_FTK = 2613
        STOCK_FTNT = 2614
        STOCK_FTR = 2615
        STOCK_FTRI = 2616
        STOCK_FTRPR = 2617
        STOCK_FTS = 2618
        STOCK_FTV = 2619
        STOCK_FTVA = 2620
        STOCK_FTXD = 2621
        STOCK_FTXG = 2622
        STOCK_FTXH = 2623
        STOCK_FTXL = 2624
        STOCK_FTXN = 2625
        STOCK_FTXO = 2626
        STOCK_FTXR = 2627
        STOCK_FUL = 2628
        STOCK_FULLL = 2629
        STOCK_FULT = 2630
        STOCK_FUN = 2631
        STOCK_FUNC = 2632
        STOCK_FUND = 2633
        STOCK_FUSB = 2634
        STOCK_FUT = 2635
        STOCK_FUV = 2636
        STOCK_FVAL = 2637
        STOCK_FVC = 2638
        STOCK_FVE = 2639
        STOCK_FWONA = 2640
        STOCK_FWONK = 2641
        STOCK_FWP = 2642
        STOCK_FWRD = 2643
        STOCK_FXEP = 2644
        STOCK_FXJP = 2645
        STOCK_G = 2646
        STOCK_GAB = 2647
        STOCK_GABC = 2648
        STOCK_GABR = 2649
        STOCK_GABRW = 2650
        STOCK_GAB_D = 2651
        STOCK_GAB_G = 2652
        STOCK_GAB_H = 2653
        STOCK_GAB_J = 2654
        STOCK_GAIA = 2655
        STOCK_GAIN = 2656
        STOCK_GAINM = 2657
        STOCK_GAINN = 2658
        STOCK_GAINO = 2659
        STOCK_GALE = 2660
        STOCK_GALT = 2661
        STOCK_GAM = 2662
        STOCK_GAMR = 2663
        STOCK_GAM_B = 2664
        STOCK_GARD = 2665
        STOCK_GARS = 2666
        STOCK_GASS = 2667
        STOCK_GASX = 2668
        STOCK_GATX = 2669
        STOCK_GAZB = 2670
        STOCK_GBAB = 2671
        STOCK_GBCI = 2672
        STOCK_GBDC = 2673
        STOCK_GBIL = 2674
        STOCK_GBL = 2675
        STOCK_GBLI = 2676
        STOCK_GBLIL = 2677
        STOCK_GBLIZ = 2678
        STOCK_GBNK = 2679
        STOCK_GBR = 2680
        STOCK_GBT = 2681
        STOCK_GBX = 2682
        STOCK_GCAP = 2683
        STOCK_GCBC = 2684
        STOCK_GCH = 2685
        STOCK_GCI = 2686
        STOCK_GCO = 2687
        STOCK_GCOW = 2688
        STOCK_GCP = 2689
        STOCK_GCV = 2690
        STOCK_GCVRZ = 2691
        STOCK_GCV_B = 2692
        STOCK_GD = 2693
        STOCK_GDDY = 2694
        STOCK_GDEN = 2695
        STOCK_GDI = 2696
        STOCK_GDL = 2697
        STOCK_GDL_B = 2698
        STOCK_GDO = 2699
        STOCK_GDOT = 2700
        STOCK_GDP = 2701
        STOCK_GDS = 2702
        STOCK_GDV = 2703
        STOCK_GDVD = 2704
        STOCK_GDV_A = 2705
        STOCK_GDV_D = 2706
        STOCK_GDV_G = 2707
        STOCK_GE = 2708
        STOCK_GEB = 2709
        STOCK_GEC = 2710
        STOCK_GECC = 2711
        STOCK_GECCL = 2712
        STOCK_GEF__B = 2713
        STOCK_GEF = 2714
        STOCK_GEH = 2715
        STOCK_GEK = 2716
        STOCK_GEL = 2717
        STOCK_GEM = 2718
        STOCK_GEMP = 2719
        STOCK_GEN = 2720
        STOCK_GENC = 2721
        STOCK_GENE = 2722
        STOCK_GENY = 2723
        STOCK_GEO = 2724
        STOCK_GEOS = 2725
        STOCK_GER = 2726
        STOCK_GERN = 2727
        STOCK_GES = 2728
        STOCK_GEVO = 2729
        STOCK_GF = 2730
        STOCK_GFA = 2731
        STOCK_GFED = 2732
        STOCK_GFF = 2733
        STOCK_GFI = 2734
        STOCK_GFN = 2735
        STOCK_GFNCP = 2736
        STOCK_GFNSL = 2737
        STOCK_GFY = 2738
        STOCK_GG = 2739
        STOCK_GGAL = 2740
        STOCK_GGB = 2741
        STOCK_GGG = 2742
        STOCK_GGM = 2743
        STOCK_GGN = 2744
        STOCK_GGN_B = 2745
        STOCK_GGO = 2746
        STOCK_GGO_A = 2747
        STOCK_GGP = 2748
        STOCK_GGP_A = 2749
        STOCK_GGT = 2750
        STOCK_GGT_B = 2751
        STOCK_GGT_E = 2752
        STOCK_GGZ = 2753
        STOCK_GGZR = 2754
        STOCK_GGZRW = 2755
        STOCK_GGZ_A = 2756
        STOCK_GHC = 2757
        STOCK_GHDX = 2758
        STOCK_GHL = 2759
        STOCK_GHM = 2760
        STOCK_GHS = 2761
        STOCK_GHY = 2762
        STOCK_GHYB = 2763
        STOCK_GHYG = 2764
        STOCK_GIB = 2765
        STOCK_GIFI = 2766
        STOCK_GIGA = 2767
        STOCK_GIGB = 2768
        STOCK_GIGM = 2769
        STOCK_GIII = 2770
        STOCK_GIL = 2771
        STOCK_GILD = 2772
        STOCK_GILT = 2773
        STOCK_GIM = 2774
        STOCK_GIMO = 2775
        STOCK_GIS = 2776
        STOCK_GJH = 2777
        STOCK_GJO = 2778
        STOCK_GJP = 2779
        STOCK_GJR = 2780
        STOCK_GJS = 2781
        STOCK_GJT = 2782
        STOCK_GJV = 2783
        STOCK_GKOS = 2784
        STOCK_GLAD = 2785
        STOCK_GLADN = 2786
        STOCK_GLBL = 2787
        STOCK_GLBR = 2788
        STOCK_GLBS = 2789
        STOCK_GLBZ = 2790
        STOCK_GLDD = 2791
        STOCK_GLDW = 2792
        STOCK_GLMD = 2793
        STOCK_GLNG = 2794
        STOCK_GLO = 2795
        STOCK_GLOB = 2796
        STOCK_GLOG = 2797
        STOCK_GLOG_A = 2798
        STOCK_GLOP = 2799
        STOCK_GLOP_A = 2800
        STOCK_GLOW = 2801
        STOCK_GLP = 2802
        STOCK_GLPG = 2803
        STOCK_GLPI = 2804
        STOCK_GLQ = 2805
        STOCK_GLRE = 2806
        STOCK_GLT = 2807
        STOCK_GLU = 2808
        STOCK_GLUU = 2809
        STOCK_GLU_A = 2810
        STOCK_GLV = 2811
        STOCK_GLW = 2812
        STOCK_GLYC = 2813
        STOCK_GM__WS__B = 2814
        STOCK_GM = 2815
        STOCK_GME = 2816
        STOCK_GMED = 2817
        STOCK_GMFL = 2818
        STOCK_GMLP = 2819
        STOCK_GMLPP = 2820
        STOCK_GMO = 2821
        STOCK_GMRE = 2822
        STOCK_GMRE_A = 2823
        STOCK_GMS = 2824
        STOCK_GMTA = 2825
        STOCK_GMZ = 2826
        STOCK_GNBC = 2827
        STOCK_GNC = 2828
        STOCK_GNCA = 2829
        STOCK_GNCMA = 2830
        STOCK_GNE = 2831
        STOCK_GNE_A = 2832
        STOCK_GNK = 2833
        STOCK_GNL = 2834
        STOCK_GNL_A = 2835
        STOCK_GNMK = 2836
        STOCK_GNMX = 2837
        STOCK_GNRC = 2838
        STOCK_GNRT = 2839
        STOCK_GNRX = 2840
        STOCK_GNST = 2841
        STOCK_GNT = 2842
        STOCK_GNTX = 2843
        STOCK_GNTY = 2844
        STOCK_GNT_A = 2845
        STOCK_GNUS = 2846
        STOCK_GNW = 2847
        STOCK_GOAU = 2848
        STOCK_GOEX = 2849
        STOCK_GOF = 2850
        STOCK_GOGL = 2851
        STOCK_GOGO = 2852
        STOCK_GOL = 2853
        STOCK_GOLD = 2854
        STOCK_GOLF = 2855
        STOCK_GOOD = 2856
        STOCK_GOODM = 2857
        STOCK_GOODO = 2858
        STOCK_GOODP = 2859
        STOCK_GOOG = 2860
        STOCK_GOOGL = 2861
        STOCK_GOOS = 2862
        STOCK_GOP = 2863
        STOCK_GORO = 2864
        STOCK_GOV = 2865
        STOCK_GOVNI = 2866
        STOCK_GPAC = 2867
        STOCK_GPACU = 2868
        STOCK_GPACW = 2869
        STOCK_GPC = 2870
        STOCK_GPE_A__CL = 2871
        STOCK_GPI = 2872
        STOCK_GPIC = 2873
        STOCK_GPJA = 2874
        STOCK_GPK = 2875
        STOCK_GPL = 2876
        STOCK_GPM = 2877
        STOCK_GPMT = 2878
        STOCK_GPMTW = 2879
        STOCK_GPN = 2880
        STOCK_GPOR = 2881
        STOCK_GPP = 2882
        STOCK_GPRE = 2883
        STOCK_GPRK = 2884
        STOCK_GPRO = 2885
        STOCK_GPS = 2886
        STOCK_GPT = 2887
        STOCK_GPT_A = 2888
        STOCK_GPX = 2889
        STOCK_GRA = 2890
        STOCK_GRAM = 2891
        STOCK_GRBK = 2892
        STOCK_GRC = 2893
        STOCK_GRF = 2894
        STOCK_GRFS = 2895
        STOCK_GRIF = 2896
        STOCK_GRMN = 2897
        STOCK_GRMY = 2898
        STOCK_GRNB = 2899
        STOCK_GROW = 2900
        STOCK_GRP__U = 2901
        STOCK_GRPN = 2902
        STOCK_GRR = 2903
        STOCK_GRUB = 2904
        STOCK_GRVY = 2905
        STOCK_GRX = 2906
        STOCK_GRX_A = 2907
        STOCK_GRX_B = 2908
        STOCK_GS = 2909
        STOCK_GSAT = 2910
        STOCK_GSB = 2911
        STOCK_GSBC = 2912
        STOCK_GSBD = 2913
        STOCK_GSD = 2914
        STOCK_GSEU = 2915
        STOCK_GSEW = 2916
        STOCK_GSH = 2917
        STOCK_GSHT = 2918
        STOCK_GSHTU = 2919
        STOCK_GSHTW = 2920
        STOCK_GSIE = 2921
        STOCK_GSIT = 2922
        STOCK_GSJY = 2923
        STOCK_GSK = 2924
        STOCK_GSL = 2925
        STOCK_GSLC = 2926
        STOCK_GSL_B = 2927
        STOCK_GSM = 2928
        STOCK_GSS = 2929
        STOCK_GSSC = 2930
        STOCK_GST = 2931
        STOCK_GST_A = 2932
        STOCK_GST_B = 2933
        STOCK_GSUM = 2934
        STOCK_GSV = 2935
        STOCK_GSVC = 2936
        STOCK_GS_A = 2937
        STOCK_GS_B = 2938
        STOCK_GS_C = 2939
        STOCK_GS_D = 2940
        STOCK_GS_I__CL = 2941
        STOCK_GS_I = 2942
        STOCK_GS_J = 2943
        STOCK_GS_K = 2944
        STOCK_GS_N = 2945
        STOCK_GT = 2946
        STOCK_GTE = 2947
        STOCK_GTHX = 2948
        STOCK_GTIM = 2949
        STOCK_GTLS = 2950
        STOCK_GTN__A = 2951
        STOCK_GTN = 2952
        STOCK_GTO = 2953
        STOCK_GTS = 2954
        STOCK_GTT = 2955
        STOCK_GTXI = 2956
        STOCK_GTY = 2957
        STOCK_GTYH = 2958
        STOCK_GTYHU = 2959
        STOCK_GTYHW = 2960
        STOCK_GUDB = 2961
        STOCK_GURE = 2962
        STOCK_GUT = 2963
        STOCK_GUT_A = 2964
        STOCK_GUT_C = 2965
        STOCK_GV = 2966
        STOCK_GVA = 2967
        STOCK_GVIP = 2968
        STOCK_GVP = 2969
        STOCK_GWB = 2970
        STOCK_GWGH = 2971
        STOCK_GWPH = 2972
        STOCK_GWR = 2973
        STOCK_GWRE = 2974
        STOCK_GWRS = 2975
        STOCK_GWW = 2976
        STOCK_GXP = 2977
        STOCK_GYB = 2978
        STOCK_GYC = 2979
        STOCK_GYRO = 2980
        STOCK_GZT = 2981
        STOCK_H = 2982
        STOCK_HA = 2983
        STOCK_HABT = 2984
        STOCK_HACK = 2985
        STOCK_HACV = 2986
        STOCK_HACW = 2987
        STOCK_HAE = 2988
        STOCK_HAFC = 2989
        STOCK_HAHA = 2990
        STOCK_HAIN = 2991
        STOCK_HAIR = 2992
        STOCK_HAL = 2993
        STOCK_HALL = 2994
        STOCK_HALO = 2995
        STOCK_HAS = 2996
        STOCK_HASI = 2997
        STOCK_HAUD = 2998
        STOCK_HAWK = 2999
        STOCK_HAWX = 3000
        STOCK_HAYN = 3001
        STOCK_HAYU = 3002
        STOCK_HBAN = 3003
        STOCK_HBANN = 3004
        STOCK_HBANO = 3005
        STOCK_HBANP = 3006
        STOCK_HBB = 3007
        STOCK_HBCP = 3008
        STOCK_HBHC = 3009
        STOCK_HBHCL = 3010
        STOCK_HBI = 3011
        STOCK_HBIO = 3012
        STOCK_HBK = 3013
        STOCK_HBM__WS = 3014
        STOCK_HBM = 3015
        STOCK_HBMD = 3016
        STOCK_HBNC = 3017
        STOCK_HBP = 3018
        STOCK_HCA = 3019
        STOCK_HCAC__U = 3020
        STOCK_HCAC__WS = 3021
        STOCK_HCAC = 3022
        STOCK_HCAP = 3023
        STOCK_HCAPZ = 3024
        STOCK_HCC = 3025
        STOCK_HCCI = 3026
        STOCK_HCHC = 3027
        STOCK_HCI = 3028
        STOCK_HCKT = 3029
        STOCK_HCLP = 3030
        STOCK_HCM = 3031
        STOCK_HCN = 3032
        STOCK_HCN_I = 3033
        STOCK_HCOM = 3034
        STOCK_HCP = 3035
        STOCK_HCRF = 3036
        STOCK_HCSG = 3037
        STOCK_HD = 3038
        STOCK_HDAW = 3039
        STOCK_HDB = 3040
        STOCK_HDEE = 3041
        STOCK_HDEF = 3042
        STOCK_HDEZ = 3043
        STOCK_HDLV = 3044
        STOCK_HDMV = 3045
        STOCK_HDNG = 3046
        STOCK_HDP = 3047
        STOCK_HDRW = 3048
        STOCK_HDS = 3049
        STOCK_HDSN = 3050
        STOCK_HE = 3051
        STOCK_HEAR = 3052
        STOCK_HEB = 3053
        STOCK_HEBT = 3054
        STOCK_HEES = 3055
        STOCK_HEFV = 3056
        STOCK_HEI__A = 3057
        STOCK_HEI = 3058
        STOCK_HELE = 3059
        STOCK_HEMV = 3060
        STOCK_HEP = 3061
        STOCK_HEQ = 3062
        STOCK_HES = 3063
        STOCK_HESM = 3064
        STOCK_HES_A = 3065
        STOCK_HEUS = 3066
        STOCK_HEUV = 3067
        STOCK_HEWC = 3068
        STOCK_HEWI = 3069
        STOCK_HEWL = 3070
        STOCK_HEWP = 3071
        STOCK_HEWU = 3072
        STOCK_HEWW = 3073
        STOCK_HEWY = 3074
        STOCK_HE_U = 3075
        STOCK_HF = 3076
        STOCK_HFBC = 3077
        STOCK_HFBL = 3078
        STOCK_HFC = 3079
        STOCK_HFRO = 3080
        STOCK_HFWA = 3081
        STOCK_HFXE = 3082
        STOCK_HFXI = 3083
        STOCK_HFXJ = 3084
        STOCK_HGH = 3085
        STOCK_HGSD = 3086
        STOCK_HGSH = 3087
        STOCK_HGT = 3088
        STOCK_HGV = 3089
        STOCK_HHC = 3090
        STOCK_HHS = 3091
        STOCK_HHYX = 3092
        STOCK_HI = 3093
        STOCK_HIBB = 3094
        STOCK_HIE = 3095
        STOCK_HIFR = 3096
        STOCK_HIFS = 3097
        STOCK_HIG__WS = 3098
        STOCK_HIG = 3099
        STOCK_HIHO = 3100
        STOCK_HII = 3101
        STOCK_HIIQ = 3102
        STOCK_HIL = 3103
        STOCK_HIMX = 3104
        STOCK_HIO = 3105
        STOCK_HIPS = 3106
        STOCK_HIVE = 3107
        STOCK_HIW = 3108
        STOCK_HIX = 3109
        STOCK_HJPX = 3110
        STOCK_HJV = 3111
        STOCK_HK__WS = 3112
        STOCK_HK = 3113
        STOCK_HL = 3114
        STOCK_HLF = 3115
        STOCK_HLG = 3116
        STOCK_HLI = 3117
        STOCK_HLIT = 3118
        STOCK_HLM_ = 3119
        STOCK_HLNE = 3120
        STOCK_HLS = 3121
        STOCK_HLT = 3122
        STOCK_HLTH = 3123
        STOCK_HLX = 3124
        STOCK_HL_B = 3125
        STOCK_HMC = 3126
        STOCK_HMG = 3127
        STOCK_HMHC = 3128
        STOCK_HMLP = 3129
        STOCK_HMLP_A = 3130
        STOCK_HMN = 3131
        STOCK_HMNF = 3132
        STOCK_HMNY = 3133
        STOCK_HMST = 3134
        STOCK_HMSY = 3135
        STOCK_HMTA = 3136
        STOCK_HMTV = 3137
        STOCK_HMY = 3138
        STOCK_HNI = 3139
        STOCK_HNNA = 3140
        STOCK_HNP = 3141
        STOCK_HNRG = 3142
        STOCK_HNW = 3143
        STOCK_HOFT = 3144
        STOCK_HOG = 3145
        STOCK_HOLI = 3146
        STOCK_HOLX = 3147
        STOCK_HOMB = 3148
        STOCK_HOME = 3149
        STOCK_HOML = 3150
        STOCK_HON = 3151
        STOCK_HONE = 3152
        STOCK_HOPE = 3153
        STOCK_HOS = 3154
        STOCK_HOTR = 3155
        STOCK_HOV = 3156
        STOCK_HOVNP = 3157
        STOCK_HP = 3158
        STOCK_HPE = 3159
        STOCK_HPF = 3160
        STOCK_HPI = 3161
        STOCK_HPJ = 3162
        STOCK_HPP = 3163
        STOCK_HPQ = 3164
        STOCK_HPS = 3165
        STOCK_HPT = 3166
        STOCK_HQCL = 3167
        STOCK_HQH = 3168
        STOCK_HQL = 3169
        STOCK_HQY = 3170
        STOCK_HR = 3171
        STOCK_HRB = 3172
        STOCK_HRC = 3173
        STOCK_HRG = 3174
        STOCK_HRI = 3175
        STOCK_HRL = 3176
        STOCK_HRS = 3177
        STOCK_HRTG = 3178
        STOCK_HRTX = 3179
        STOCK_HRZN = 3180
        STOCK_HSBC = 3181
        STOCK_HSBC_A = 3182
        STOCK_HSC = 3183
        STOCK_HSCZ = 3184
        STOCK_HSEA = 3185
        STOCK_HSEB = 3186
        STOCK_HSGX = 3187
        STOCK_HSIC = 3188
        STOCK_HSII = 3189
        STOCK_HSKA = 3190
        STOCK_HSNI = 3191
        STOCK_HSON = 3192
        STOCK_HST = 3193
        STOCK_HSTM = 3194
        STOCK_HSY = 3195
        STOCK_HT = 3196
        STOCK_HTA = 3197
        STOCK_HTBI = 3198
        STOCK_HTBK = 3199
        STOCK_HTBX = 3200
        STOCK_HTD = 3201
        STOCK_HTF__CL = 3202
        STOCK_HTFA = 3203
        STOCK_HTGC = 3204
        STOCK_HTGM = 3205
        STOCK_HTGX = 3206
        STOCK_HTH = 3207
        STOCK_HTHT = 3208
        STOCK_HTLD = 3209
        STOCK_HTLF = 3210
        STOCK_HTM = 3211
        STOCK_HTRB = 3212
        STOCK_HTUS = 3213
        STOCK_HTY = 3214
        STOCK_HTZ = 3215
        STOCK_HT_C = 3216
        STOCK_HT_D = 3217
        STOCK_HT_E = 3218
        STOCK_HUBB = 3219
        STOCK_HUBG = 3220
        STOCK_HUBS = 3221
        STOCK_HUM = 3222
        STOCK_HUN = 3223
        STOCK_HUNT = 3224
        STOCK_HUNTU = 3225
        STOCK_HUNTW = 3226
        STOCK_HURC = 3227
        STOCK_HURN = 3228
        STOCK_HUSA = 3229
        STOCK_HUSV = 3230
        STOCK_HVBC = 3231
        STOCK_HVT__A = 3232
        STOCK_HVT = 3233
        STOCK_HWBK = 3234
        STOCK_HWCC = 3235
        STOCK_HWKN = 3236
        STOCK_HX = 3237
        STOCK_HXL = 3238
        STOCK_HY = 3239
        STOCK_HYACU = 3240
        STOCK_HYB = 3241
        STOCK_HYDB = 3242
        STOCK_HYDD = 3243
        STOCK_HYGS = 3244
        STOCK_HYH = 3245
        STOCK_HYHG = 3246
        STOCK_HYI = 3247
        STOCK_HYLB = 3248
        STOCK_HYLV = 3249
        STOCK_HYT = 3250
        STOCK_HYXE = 3251
        STOCK_HYXU = 3252
        STOCK_HZN = 3253
        STOCK_HZNP = 3254
        STOCK_HZO = 3255
        STOCK_I = 3256
        STOCK_IAC = 3257
        STOCK_IAE = 3258
        STOCK_IAF = 3259
        STOCK_IAG = 3260
        STOCK_IAGG = 3261
        STOCK_IAM = 3262
        STOCK_IAMXR = 3263
        STOCK_IAMXW = 3264
        STOCK_IART = 3265
        STOCK_IBA = 3266
        STOCK_IBCP = 3267
        STOCK_IBD = 3268
        STOCK_IBDR = 3269
        STOCK_IBDS = 3270
        STOCK_IBIO = 3271
        STOCK_IBKC = 3272
        STOCK_IBKCO = 3273
        STOCK_IBKCP = 3274
        STOCK_IBKR = 3275
        STOCK_IBM = 3276
        STOCK_IBMJ = 3277
        STOCK_IBMK = 3278
        STOCK_IBML = 3279
        STOCK_IBN = 3280
        STOCK_IBO = 3281
        STOCK_IBOC = 3282
        STOCK_IBP = 3283
        STOCK_IBTX = 3284
        STOCK_IBUY = 3285
        STOCK_ICAD = 3286
        STOCK_ICAN = 3287
        STOCK_ICB = 3288
        STOCK_ICBK = 3289
        STOCK_ICCC = 3290
        STOCK_ICCH = 3291
        STOCK_ICD = 3292
        STOCK_ICE = 3293
        STOCK_ICFI = 3294
        STOCK_ICHR = 3295
        STOCK_ICL = 3296
        STOCK_ICLR = 3297
        STOCK_ICON = 3298
        STOCK_ICOW = 3299
        STOCK_ICPT = 3300
        STOCK_ICSH = 3301
        STOCK_ICUI = 3302
        STOCK_ICVT = 3303
        STOCK_IDA = 3304
        STOCK_IDCC = 3305
        STOCK_IDE = 3306
        STOCK_IDEV = 3307
        STOCK_IDHD = 3308
        STOCK_IDLB = 3309
        STOCK_IDMO = 3310
        STOCK_IDN = 3311
        STOCK_IDRA = 3312
        STOCK_IDSA = 3313
        STOCK_IDSY = 3314
        STOCK_IDT = 3315
        STOCK_IDTI = 3316
        STOCK_IDXG = 3317
        STOCK_IDXX = 3318
        STOCK_IEC = 3319
        STOCK_IEP = 3320
        STOCK_IESC = 3321
        STOCK_IEX = 3322
        STOCK_IF = 3323
        STOCK_IFF = 3324
        STOCK_IFIX = 3325
        STOCK_IFLY = 3326
        STOCK_IFMK = 3327
        STOCK_IFN = 3328
        STOCK_IFON = 3329
        STOCK_IFRX = 3330
        STOCK_IGA = 3331
        STOCK_IGC = 3332
        STOCK_IGD = 3333
        STOCK_IGEB = 3334
        STOCK_IGEM = 3335
        STOCK_IGHG = 3336
        STOCK_IGI = 3337
        STOCK_IGLD = 3338
        STOCK_IGR = 3339
        STOCK_IGRO = 3340
        STOCK_IGT = 3341
        STOCK_IGVT = 3342
        STOCK_IGZ = 3343
        STOCK_IHC = 3344
        STOCK_IHD = 3345
        STOCK_IHG = 3346
        STOCK_IHIT = 3347
        STOCK_IHT = 3348
        STOCK_IID = 3349
        STOCK_IIF = 3350
        STOCK_III = 3351
        STOCK_IIIN = 3352
        STOCK_IIJI = 3353
        STOCK_IIM = 3354
        STOCK_IIN = 3355
        STOCK_IIPR = 3356
        STOCK_IIPR_A = 3357
        STOCK_IIVI = 3358
        STOCK_IKNX = 3359
        STOCK_ILG = 3360
        STOCK_ILMN = 3361
        STOCK_IMAX = 3362
        STOCK_IMDZ = 3363
        STOCK_IMGN = 3364
        STOCK_IMH = 3365
        STOCK_IMI = 3366
        STOCK_IMKTA = 3367
        STOCK_IMMR = 3368
        STOCK_IMMU = 3369
        STOCK_IMMY = 3370
        STOCK_IMNP = 3371
        STOCK_IMO = 3372
        STOCK_IMOM = 3373
        STOCK_IMOS = 3374
        STOCK_IMPV = 3375
        STOCK_IMRN = 3376
        STOCK_IMRNW = 3377
        STOCK_IMTB = 3378
        STOCK_IMTE = 3379
        STOCK_IMUC__WS = 3380
        STOCK_IMUC = 3381
        STOCK_INAP = 3382
        STOCK_INB = 3383
        STOCK_INBK = 3384
        STOCK_INBKL = 3385
        STOCK_INCR = 3386
        STOCK_INCY = 3387
        STOCK_INDB = 3388
        STOCK_INDF = 3389
        STOCK_INDU = 3390
        STOCK_INDUU = 3391
        STOCK_INDUW = 3392
        STOCK_INF = 3393
        STOCK_INFI = 3394
        STOCK_INFN = 3395
        STOCK_INFO = 3396
        STOCK_INFR = 3397
        STOCK_INFU = 3398
        STOCK_INFY = 3399
        STOCK_ING = 3400
        STOCK_INGN = 3401
        STOCK_INGR = 3402
        STOCK_INN = 3403
        STOCK_INN_B__CL = 3404
        STOCK_INN_B = 3405
        STOCK_INN_C = 3406
        STOCK_INN_D = 3407
        STOCK_INO = 3408
        STOCK_INOD = 3409
        STOCK_INOV = 3410
        STOCK_INPX = 3411
        STOCK_INS = 3412
        STOCK_INSE = 3413
        STOCK_INSG = 3414
        STOCK_INSI = 3415
        STOCK_INSM = 3416
        STOCK_INST = 3417
        STOCK_INSW = 3418
        STOCK_INSY = 3419
        STOCK_INT = 3420
        STOCK_INTC = 3421
        STOCK_INTG = 3422
        STOCK_INTL = 3423
        STOCK_INTT = 3424
        STOCK_INTU = 3425
        STOCK_INTX = 3426
        STOCK_INUV = 3427
        STOCK_INVA = 3428
        STOCK_INVE = 3429
        STOCK_INVH = 3430
        STOCK_INWK = 3431
        STOCK_INXN = 3432
        STOCK_IO = 3433
        STOCK_IONS = 3434
        STOCK_IOR = 3435
        STOCK_IOSP = 3436
        STOCK_IOTS = 3437
        STOCK_IOVA = 3438
        STOCK_IP = 3439
        STOCK_IPAR = 3440
        STOCK_IPAS = 3441
        STOCK_IPAY = 3442
        STOCK_IPB = 3443
        STOCK_IPCC = 3444
        STOCK_IPCI = 3445
        STOCK_IPDN = 3446
        STOCK_IPG = 3447
        STOCK_IPGP = 3448
        STOCK_IPHI = 3449
        STOCK_IPHS = 3450
        STOCK_IPI = 3451
        STOCK_IPL_D = 3452
        STOCK_IPOA__U = 3453
        STOCK_IPOA__WS = 3454
        STOCK_IPOA = 3455
        STOCK_IPOS = 3456
        STOCK_IPWR = 3457
        STOCK_IPXL = 3458
        STOCK_IQDG = 3459
        STOCK_IQI = 3460
        STOCK_IR = 3461
        STOCK_IRBT = 3462
        STOCK_IRCP = 3463
        STOCK_IRDM = 3464
        STOCK_IRDMB = 3465
        STOCK_IRET = 3466
        STOCK_IRET_B__CL = 3467
        STOCK_IRET_C = 3468
        STOCK_IRIX = 3469
        STOCK_IRL = 3470
        STOCK_IRLR = 3471
        STOCK_IRM = 3472
        STOCK_IRMD = 3473
        STOCK_IROQ = 3474
        STOCK_IRR = 3475
        STOCK_IRS = 3476
        STOCK_IRT = 3477
        STOCK_IRTC = 3478
        STOCK_IRWD = 3479
        STOCK_ISBC = 3480
        STOCK_ISCA = 3481
        STOCK_ISD = 3482
        STOCK_ISDR = 3483
        STOCK_ISF = 3484
        STOCK_ISG = 3485
        STOCK_ISIG = 3486
        STOCK_ISL = 3487
        STOCK_ISM = 3488
        STOCK_ISMD = 3489
        STOCK_ISNS = 3490
        STOCK_ISP__CL = 3491
        STOCK_ISR = 3492
        STOCK_ISRG = 3493
        STOCK_ISRL = 3494
        STOCK_ISSC = 3495
        STOCK_ISTR = 3496
        STOCK_ISZE = 3497
        STOCK_IT = 3498
        STOCK_ITCB = 3499
        STOCK_ITCI = 3500
        STOCK_ITEK = 3501
        STOCK_ITEQ = 3502
        STOCK_ITG = 3503
        STOCK_ITGR = 3504
        STOCK_ITI = 3505
        STOCK_ITIC = 3506
        STOCK_ITRI = 3507
        STOCK_ITRN = 3508
        STOCK_ITT = 3509
        STOCK_ITUB = 3510
        STOCK_ITUS = 3511
        STOCK_ITW = 3512
        STOCK_IVAC = 3513
        STOCK_IVAL = 3514
        STOCK_IVC = 3515
        STOCK_IVENC = 3516
        STOCK_IVFGC = 3517
        STOCK_IVFVC = 3518
        STOCK_IVH = 3519
        STOCK_IVLU = 3520
        STOCK_IVR = 3521
        STOCK_IVR_A = 3522
        STOCK_IVR_B = 3523
        STOCK_IVR_C = 3524
        STOCK_IVTY = 3525
        STOCK_IVZ = 3526
        STOCK_IX = 3527
        STOCK_IXYS = 3528
        STOCK_IYLD = 3529
        STOCK_IZEA = 3530
        STOCK_JACK = 3531
        STOCK_JAG = 3532
        STOCK_JAGX = 3533
        STOCK_JAKK = 3534
        STOCK_JASN = 3535
        STOCK_JASNW = 3536
        STOCK_JASO = 3537
        STOCK_JAX = 3538
        STOCK_JAZZ = 3539
        STOCK_JBGS = 3540
        STOCK_JBHT = 3541
        STOCK_JBK = 3542
        STOCK_JBL = 3543
        STOCK_JBLU = 3544
        STOCK_JBN = 3545
        STOCK_JBR = 3546
        STOCK_JBSS = 3547
        STOCK_JBT = 3548
        STOCK_JCAP = 3549
        STOCK_JCE = 3550
        STOCK_JCI = 3551
        STOCK_JCO = 3552
        STOCK_JCOM = 3553
        STOCK_JCP = 3554
        STOCK_JCS = 3555
        STOCK_JCTCF = 3556
        STOCK_JD = 3557
        STOCK_JDD = 3558
        STOCK_JDIV = 3559
        STOCK_JE = 3560
        STOCK_JEC = 3561
        STOCK_JELD = 3562
        STOCK_JEMD = 3563
        STOCK_JEQ = 3564
        STOCK_JETS = 3565
        STOCK_JE_A = 3566
        STOCK_JFR = 3567
        STOCK_JGH = 3568
        STOCK_JHA = 3569
        STOCK_JHB = 3570
        STOCK_JHD = 3571
        STOCK_JHG = 3572
        STOCK_JHI = 3573
        STOCK_JHMA = 3574
        STOCK_JHMC = 3575
        STOCK_JHMD = 3576
        STOCK_JHME = 3577
        STOCK_JHMF = 3578
        STOCK_JHMH = 3579
        STOCK_JHMI = 3580
        STOCK_JHML = 3581
        STOCK_JHMM = 3582
        STOCK_JHMS = 3583
        STOCK_JHMT = 3584
        STOCK_JHMU = 3585
        STOCK_JHS = 3586
        STOCK_JHSC = 3587
        STOCK_JHX = 3588
        STOCK_JHY = 3589
        STOCK_JILL = 3590
        STOCK_JJSF = 3591
        STOCK_JKHY = 3592
        STOCK_JKS = 3593
        STOCK_JLL = 3594
        STOCK_JLS = 3595
        STOCK_JMBA = 3596
        STOCK_JMEI = 3597
        STOCK_JMF = 3598
        STOCK_JMLP = 3599
        STOCK_JMM = 3600
        STOCK_JMOM = 3601
        STOCK_JMP = 3602
        STOCK_JMPB = 3603
        STOCK_JMPC = 3604
        STOCK_JMT = 3605
        STOCK_JMU = 3606
        STOCK_JNCE = 3607
        STOCK_JNJ = 3608
        STOCK_JNP = 3609
        STOCK_JNPR = 3610
        STOCK_JOB = 3611
        STOCK_JOBS = 3612
        STOCK_JOE = 3613
        STOCK_JOF = 3614
        STOCK_JONE = 3615
        STOCK_JOUT = 3616
        STOCK_JP = 3617
        STOCK_JPC = 3618
        STOCK_JPEH = 3619
        STOCK_JPEM = 3620
        STOCK_JPEU = 3621
        STOCK_JPGB = 3622
        STOCK_JPHF = 3623
        STOCK_JPHY = 3624
        STOCK_JPI = 3625
        STOCK_JPIH = 3626
        STOCK_JPIN = 3627
        STOCK_JPM__WS = 3628
        STOCK_JPM = 3629
        STOCK_JPME = 3630
        STOCK_JPM_A = 3631
        STOCK_JPM_B = 3632
        STOCK_JPM_D__CL = 3633
        STOCK_JPM_D = 3634
        STOCK_JPM_E = 3635
        STOCK_JPM_F = 3636
        STOCK_JPM_G = 3637
        STOCK_JPM_H = 3638
        STOCK_JPN = 3639
        STOCK_JPS = 3640
        STOCK_JPSE = 3641
        STOCK_JPST = 3642
        STOCK_JPT = 3643
        STOCK_JPUS = 3644
        STOCK_JPXN = 3645
        STOCK_JQC = 3646
        STOCK_JRI = 3647
        STOCK_JRJC = 3648
        STOCK_JRJR = 3649
        STOCK_JRO = 3650
        STOCK_JRS = 3651
        STOCK_JRVR = 3652
        STOCK_JSD = 3653
        STOCK_JSM = 3654
        STOCK_JSMD = 3655
        STOCK_JSML = 3656
        STOCK_JSYN = 3657
        STOCK_JSYNR = 3658
        STOCK_JSYNU = 3659
        STOCK_JSYNW = 3660
        STOCK_JT = 3661
        STOCK_JTA = 3662
        STOCK_JTD = 3663
        STOCK_JTPY = 3664
        STOCK_JUNO = 3665
        STOCK_JVA = 3666
        STOCK_JW__A = 3667
        STOCK_JW__B = 3668
        STOCK_JWN = 3669
        STOCK_JXSB = 3670
        STOCK_JYNT = 3671
        STOCK_K = 3672
        STOCK_KAAC = 3673
        STOCK_KAACU = 3674
        STOCK_KAACW = 3675
        STOCK_KAI = 3676
        STOCK_KALA = 3677
        STOCK_KALU = 3678
        STOCK_KALV = 3679
        STOCK_KAMN = 3680
        STOCK_KANG = 3681
        STOCK_KAP = 3682
        STOCK_KAR = 3683
        STOCK_KB = 3684
        STOCK_KBAL = 3685
        STOCK_KBH = 3686
        STOCK_KBLM = 3687
        STOCK_KBLMR = 3688
        STOCK_KBLMU = 3689
        STOCK_KBLMW = 3690
        STOCK_KBR = 3691
        STOCK_KBSF = 3692
        STOCK_KBWB = 3693
        STOCK_KBWD = 3694
        STOCK_KBWY = 3695
        STOCK_KCAP = 3696
        STOCK_KCAPL = 3697
        STOCK_KCNY = 3698
        STOCK_KDMN = 3699
        STOCK_KE = 3700
        STOCK_KED = 3701
        STOCK_KEG = 3702
        STOCK_KELYA = 3703
        STOCK_KELYB = 3704
        STOCK_KEM = 3705
        STOCK_KEMP = 3706
        STOCK_KEMQ = 3707
        STOCK_KEN = 3708
        STOCK_KEP = 3709
        STOCK_KEQU = 3710
        STOCK_KERX = 3711
        STOCK_KEX = 3712
        STOCK_KEY = 3713
        STOCK_KEYS = 3714
        STOCK_KEYW = 3715
        STOCK_KEY_I = 3716
        STOCK_KF = 3717
        STOCK_KFFB = 3718
        STOCK_KFN_ = 3719
        STOCK_KFRC = 3720
        STOCK_KFS = 3721
        STOCK_KFY = 3722
        STOCK_KGC = 3723
        STOCK_KGJI = 3724
        STOCK_KGRN = 3725
        STOCK_KHC = 3726
        STOCK_KIDS = 3727
        STOCK_KIM = 3728
        STOCK_KIM_I = 3729
        STOCK_KIM_J = 3730
        STOCK_KIM_K = 3731
        STOCK_KIM_L = 3732
        STOCK_KIN = 3733
        STOCK_KINS = 3734
        STOCK_KIO = 3735
        STOCK_KIOR = 3736
        STOCK_KIORW = 3737
        STOCK_KIQ = 3738
        STOCK_KIRK = 3739
        STOCK_KKR = 3740
        STOCK_KKR_A = 3741
        STOCK_KKR_B = 3742
        STOCK_KL = 3743
        STOCK_KLAC = 3744
        STOCK_KLDW = 3745
        STOCK_KLDX = 3746
        STOCK_KLIC = 3747
        STOCK_KLXI = 3748
        STOCK_KMB = 3749
        STOCK_KMDA = 3750
        STOCK_KMF = 3751
        STOCK_KMG = 3752
        STOCK_KMI = 3753
        STOCK_KMI_A = 3754
        STOCK_KMM = 3755
        STOCK_KMPA = 3756
        STOCK_KMPH = 3757
        STOCK_KMPR = 3758
        STOCK_KMT = 3759
        STOCK_KMX = 3760
        STOCK_KN = 3761
        STOCK_KND = 3762
        STOCK_KNDI = 3763
        STOCK_KNL = 3764
        STOCK_KNOP = 3765
        STOCK_KNSL = 3766
        STOCK_KNX = 3767
        STOCK_KO = 3768
        STOCK_KODK__WS__A = 3769
        STOCK_KODK__WS = 3770
        STOCK_KODK = 3771
        STOCK_KOF = 3772
        STOCK_KONA = 3773
        STOCK_KONE = 3774
        STOCK_KOOL = 3775
        STOCK_KOP = 3776
        STOCK_KOPN = 3777
        STOCK_KOR = 3778
        STOCK_KORS = 3779
        STOCK_KOS = 3780
        STOCK_KOSS = 3781
        STOCK_KPTI = 3782
        STOCK_KR = 3783
        STOCK_KRA = 3784
        STOCK_KRC = 3785
        STOCK_KREF = 3786
        STOCK_KRG = 3787
        STOCK_KRMA = 3788
        STOCK_KRNT = 3789
        STOCK_KRNY = 3790
        STOCK_KRO = 3791
        STOCK_KRP = 3792
        STOCK_KRYS = 3793
        STOCK_KS = 3794
        STOCK_KSA = 3795
        STOCK_KSM = 3796
        STOCK_KSS = 3797
        STOCK_KST = 3798
        STOCK_KSU = 3799
        STOCK_KSU_ = 3800
        STOCK_KT = 3801
        STOCK_KTCC = 3802
        STOCK_KTEC = 3803
        STOCK_KTF = 3804
        STOCK_KTH = 3805
        STOCK_KTN = 3806
        STOCK_KTOS = 3807
        STOCK_KTOV = 3808
        STOCK_KTOVW = 3809
        STOCK_KTP = 3810
        STOCK_KTWO = 3811
        STOCK_KURA = 3812
        STOCK_KVHI = 3813
        STOCK_KW = 3814
        STOCK_KWEB = 3815
        STOCK_KWN__CL = 3816
        STOCK_KWN = 3817
        STOCK_KWR = 3818
        STOCK_KYE = 3819
        STOCK_KYN = 3820
        STOCK_KYN_F = 3821
        STOCK_KYO = 3822
        STOCK_L = 3823
        STOCK_LABL = 3824
        STOCK_LAD = 3825
        STOCK_LADR = 3826
        STOCK_LAKE = 3827
        STOCK_LAMR = 3828
        STOCK_LANC = 3829
        STOCK_LAND = 3830
        STOCK_LANDP = 3831
        STOCK_LAQ = 3832
        STOCK_LARE = 3833
        STOCK_LARK = 3834
        STOCK_LAUR = 3835
        STOCK_LAWS = 3836
        STOCK_LAYN = 3837
        STOCK_LAZ = 3838
        STOCK_LB = 3839
        STOCK_LBAI = 3840
        STOCK_LBDC = 3841
        STOCK_LBIX = 3842
        STOCK_LBRDA = 3843
        STOCK_LBRDK = 3844
        STOCK_LBTYA = 3845
        STOCK_LBTYB = 3846
        STOCK_LBTYK = 3847
        STOCK_LBY = 3848
        STOCK_LC = 3849
        STOCK_LCA = 3850
        STOCK_LCAHU = 3851
        STOCK_LCAHW = 3852
        STOCK_LCI = 3853
        STOCK_LCII = 3854
        STOCK_LCM = 3855
        STOCK_LCNB = 3856
        STOCK_LCUT = 3857
        STOCK_LDF = 3858
        STOCK_LDL = 3859
        STOCK_LDOS = 3860
        STOCK_LDP = 3861
        STOCK_LDR = 3862
        STOCK_LE = 3863
        STOCK_LEA = 3864
        STOCK_LEAD = 3865
        STOCK_LECO = 3866
        STOCK_LEDS = 3867
        STOCK_LEE = 3868
        STOCK_LEG = 3869
        STOCK_LEJU = 3870
        STOCK_LEN__B = 3871
        STOCK_LEN = 3872
        STOCK_LENS = 3873
        STOCK_LEO = 3874
        STOCK_LEU = 3875
        STOCK_LEXEA = 3876
        STOCK_LEXEB = 3877
        STOCK_LFC = 3878
        STOCK_LFEQ = 3879
        STOCK_LFGR = 3880
        STOCK_LFUS = 3881
        STOCK_LFVN = 3882
        STOCK_LGCY = 3883
        STOCK_LGCYO = 3884
        STOCK_LGCYP = 3885
        STOCK_LGF__A = 3886
        STOCK_LGF__B = 3887
        STOCK_LGI = 3888
        STOCK_LGIH = 3889
        STOCK_LGL = 3890
        STOCK_LGLR = 3891
        STOCK_LGND = 3892
        STOCK_LH = 3893
        STOCK_LHCG = 3894
        STOCK_LHO = 3895
        STOCK_LHO_I = 3896
        STOCK_LHO_J = 3897
        STOCK_LIFE = 3898
        STOCK_LII = 3899
        STOCK_LILA = 3900
        STOCK_LILAK = 3901
        STOCK_LINC = 3902
        STOCK_LIND = 3903
        STOCK_LINDW = 3904
        STOCK_LINK = 3905
        STOCK_LINU = 3906
        STOCK_LION = 3907
        STOCK_LIQT = 3908
        STOCK_LITB = 3909
        STOCK_LITE = 3910
        STOCK_LIVE = 3911
        STOCK_LIVN = 3912
        STOCK_LJPC = 3913
        STOCK_LKFN = 3914
        STOCK_LKOR = 3915
        STOCK_LKQ = 3916
        STOCK_LKSD = 3917
        STOCK_LL = 3918
        STOCK_LLEX = 3919
        STOCK_LLIT = 3920
        STOCK_LLL = 3921
        STOCK_LLNW = 3922
        STOCK_LLQD = 3923
        STOCK_LLY = 3924
        STOCK_LM = 3925
        STOCK_LMAT = 3926
        STOCK_LMB = 3927
        STOCK_LMFA = 3928
        STOCK_LMFAW = 3929
        STOCK_LMHA = 3930
        STOCK_LMHB = 3931
        STOCK_LMNR = 3932
        STOCK_LMNX = 3933
        STOCK_LMOS = 3934
        STOCK_LMRK = 3935
        STOCK_LMRKO = 3936
        STOCK_LMRKP = 3937
        STOCK_LMT = 3938
        STOCK_LN = 3939
        STOCK_LNC__WS = 3940
        STOCK_LNC = 3941
        STOCK_LNCE = 3942
        STOCK_LND = 3943
        STOCK_LNDC = 3944
        STOCK_LNG = 3945
        STOCK_LNGR = 3946
        STOCK_LNN = 3947
        STOCK_LNT = 3948
        STOCK_LNTH = 3949
        STOCK_LOAN = 3950
        STOCK_LOB = 3951
        STOCK_LOCO = 3952
        STOCK_LODE = 3953
        STOCK_LOGI = 3954
        STOCK_LOGM = 3955
        STOCK_LOGO = 3956
        STOCK_LOMA = 3957
        STOCK_LONE = 3958
        STOCK_LOPE = 3959
        STOCK_LOR = 3960
        STOCK_LORL = 3961
        STOCK_LOV = 3962
        STOCK_LOVW = 3963
        STOCK_LOW = 3964
        STOCK_LOXO = 3965
        STOCK_LPCN = 3966
        STOCK_LPG = 3967
        STOCK_LPI = 3968
        STOCK_LPL = 3969
        STOCK_LPLA = 3970
        STOCK_LPNT = 3971
        STOCK_LPSN = 3972
        STOCK_LPT = 3973
        STOCK_LPTH = 3974
        STOCK_LPTX = 3975
        STOCK_LPX = 3976
        STOCK_LQ = 3977
        STOCK_LQDT = 3978
        STOCK_LRAD = 3979
        STOCK_LRCX = 3980
        STOCK_LRET = 3981
        STOCK_LRGE = 3982
        STOCK_LRN = 3983
        STOCK_LSBK = 3984
        STOCK_LSCC = 3985
        STOCK_LSI = 3986
        STOCK_LSTR = 3987
        STOCK_LSVX = 3988
        STOCK_LSXMA = 3989
        STOCK_LSXMB = 3990
        STOCK_LSXMK = 3991
        STOCK_LTBR = 3992
        STOCK_LTC = 3993
        STOCK_LTEA = 3994
        STOCK_LTM = 3995
        STOCK_LTRPA = 3996
        STOCK_LTRPB = 3997
        STOCK_LTRX = 3998
        STOCK_LTS = 3999
        STOCK_LTS_A = 4000
        STOCK_LTXB = 4001
        STOCK_LUB = 4002
        STOCK_LUK = 4003
        STOCK_LULU = 4004
        STOCK_LUNA = 4005
        STOCK_LUV = 4006
        STOCK_LVHB = 4007
        STOCK_LVHD = 4008
        STOCK_LVHE = 4009
        STOCK_LVHI = 4010
        STOCK_LVIN = 4011
        STOCK_LVLT = 4012
        STOCK_LVNTA = 4013
        STOCK_LVNTB = 4014
        STOCK_LVS = 4015
        STOCK_LVUS = 4016
        STOCK_LW = 4017
        STOCK_LWAY = 4018
        STOCK_LXFR = 4019
        STOCK_LXFT = 4020
        STOCK_LXP = 4021
        STOCK_LXP_C = 4022
        STOCK_LXRX = 4023
        STOCK_LXU = 4024
        STOCK_LYB = 4025
        STOCK_LYG = 4026
        STOCK_LYL = 4027
        STOCK_LYTS = 4028
        STOCK_LYV = 4029
        STOCK_LZB = 4030
        STOCK_M = 4031
        STOCK_MA = 4032
        STOCK_MAA = 4033
        STOCK_MAA_I = 4034
        STOCK_MAB = 4035
        STOCK_MAC = 4036
        STOCK_MACK = 4037
        STOCK_MACQ = 4038
        STOCK_MACQU = 4039
        STOCK_MACQW = 4040
        STOCK_MAG = 4041
        STOCK_MAGA = 4042
        STOCK_MAGS = 4043
        STOCK_MAIN = 4044
        STOCK_MAMS = 4045
        STOCK_MAN = 4046
        STOCK_MANH = 4047
        STOCK_MANT = 4048
        STOCK_MANU = 4049
        STOCK_MAPI = 4050
        STOCK_MAR = 4051
        STOCK_MARA = 4052
        STOCK_MARK = 4053
        STOCK_MARPS = 4054
        STOCK_MAS = 4055
        STOCK_MASI = 4056
        STOCK_MAT = 4057
        STOCK_MATF = 4058
        STOCK_MATR = 4059
        STOCK_MATW = 4060
        STOCK_MATX = 4061
        STOCK_MAV = 4062
        STOCK_MAXR = 4063
        STOCK_MAYS = 4064
        STOCK_MB = 4065
        STOCK_MBCN = 4066
        STOCK_MBFI = 4067
        STOCK_MBFIP = 4068
        STOCK_MBI = 4069
        STOCK_MBII = 4070
        STOCK_MBIN = 4071
        STOCK_MBIO = 4072
        STOCK_MBOT = 4073
        STOCK_MBRX = 4074
        STOCK_MBT = 4075
        STOCK_MBTF = 4076
        STOCK_MBUU = 4077
        STOCK_MBVX = 4078
        STOCK_MBWM = 4079
        STOCK_MC = 4080
        STOCK_MCA = 4081
        STOCK_MCB = 4082
        STOCK_MCBC = 4083
        STOCK_MCC = 4084
        STOCK_MCD = 4085
        STOCK_MCEF = 4086
        STOCK_MCEP = 4087
        STOCK_MCF = 4088
        STOCK_MCFT = 4089
        STOCK_MCHP = 4090
        STOCK_MCHX = 4091
        STOCK_MCI = 4092
        STOCK_MCK = 4093
        STOCK_MCN = 4094
        STOCK_MCO = 4095
        STOCK_MCR = 4096
        STOCK_MCRB = 4097
        STOCK_MCRI = 4098
        STOCK_MCRN = 4099
        STOCK_MCS = 4100
        STOCK_MCV = 4101
        STOCK_MCX = 4102
        STOCK_MCY = 4103
        STOCK_MD = 4104
        STOCK_MDB = 4105
        STOCK_MDC = 4106
        STOCK_MDCA = 4107
        STOCK_MDCO = 4108
        STOCK_MDGL = 4109
        STOCK_MDGS = 4110
        STOCK_MDLQ = 4111
        STOCK_MDLX = 4112
        STOCK_MDLY = 4113
        STOCK_MDLZ = 4114
        STOCK_MDP = 4115
        STOCK_MDR = 4116
        STOCK_MDRX = 4117
        STOCK_MDSO = 4118
        STOCK_MDT = 4119
        STOCK_MDU = 4120
        STOCK_MDVX = 4121
        STOCK_MDVXW = 4122
        STOCK_MDWD = 4123
        STOCK_MDXG = 4124
        STOCK_MEAR = 4125
        STOCK_MED = 4126
        STOCK_MEDP = 4127
        STOCK_MEET = 4128
        STOCK_MEI = 4129
        STOCK_MEIP = 4130
        STOCK_MELI = 4131
        STOCK_MELR = 4132
        STOCK_MEN = 4133
        STOCK_MENU = 4134
        STOCK_MEOH = 4135
        STOCK_MERC = 4136
        STOCK_MER_K = 4137
        STOCK_MER_P = 4138
        STOCK_MESO = 4139
        STOCK_MET = 4140
        STOCK_METC = 4141
        STOCK_MET_A = 4142
        STOCK_MEXX = 4143
        STOCK_MFA = 4144
        STOCK_MFA_B = 4145
        STOCK_MFC = 4146
        STOCK_MFCB = 4147
        STOCK_MFDX = 4148
        STOCK_MFEM = 4149
        STOCK_MFG = 4150
        STOCK_MFGP = 4151
        STOCK_MFIN = 4152
        STOCK_MFINL = 4153
        STOCK_MFL = 4154
        STOCK_MFM = 4155
        STOCK_MFNC = 4156
        STOCK_MFO = 4157
        STOCK_MFSF = 4158
        STOCK_MFT = 4159
        STOCK_MFUS = 4160
        STOCK_MFV = 4161
        STOCK_MG = 4162
        STOCK_MGA = 4163
        STOCK_MGCD = 4164
        STOCK_MGEE = 4165
        STOCK_MGEN = 4166
        STOCK_MGF = 4167
        STOCK_MGI = 4168
        STOCK_MGIC = 4169
        STOCK_MGLN = 4170
        STOCK_MGM = 4171
        STOCK_MGNX = 4172
        STOCK_MGP = 4173
        STOCK_MGPI = 4174
        STOCK_MGRC = 4175
        STOCK_MGU = 4176
        STOCK_MGYR = 4177
        STOCK_MHD = 4178
        STOCK_MHE = 4179
        STOCK_MHF = 4180
        STOCK_MHH = 4181
        STOCK_MHI = 4182
        STOCK_MHK = 4183
        STOCK_MHLA = 4184
        STOCK_MHLD = 4185
        STOCK_MHN = 4186
        STOCK_MHNC = 4187
        STOCK_MHO = 4188
        STOCK_MH_A = 4189
        STOCK_MH_C = 4190
        STOCK_MH_D = 4191
        STOCK_MIC = 4192
        STOCK_MICR = 4193
        STOCK_MICT = 4194
        STOCK_MICTW = 4195
        STOCK_MIDD = 4196
        STOCK_MIE = 4197
        STOCK_MIII = 4198
        STOCK_MIIIU = 4199
        STOCK_MIIIW = 4200
        STOCK_MIK = 4201
        STOCK_MILN = 4202
        STOCK_MIME = 4203
        STOCK_MIN = 4204
        STOCK_MIND = 4205
        STOCK_MINDP = 4206
        STOCK_MINI = 4207
        STOCK_MITK = 4208
        STOCK_MITL = 4209
        STOCK_MITT = 4210
        STOCK_MITT_A = 4211
        STOCK_MITT_B = 4212
        STOCK_MIW = 4213
        STOCK_MIXT = 4214
        STOCK_MIY = 4215
        STOCK_MJCO = 4216
        STOCK_MKC__V = 4217
        STOCK_MKC = 4218
        STOCK_MKL = 4219
        STOCK_MKSI = 4220
        STOCK_MKTX = 4221
        STOCK_MLAB = 4222
        STOCK_MLCO = 4223
        STOCK_MLHR = 4224
        STOCK_MLI = 4225
        STOCK_MLM = 4226
        STOCK_MLNK = 4227
        STOCK_MLNT = 4228
        STOCK_MLNX = 4229
        STOCK_MLP = 4230
        STOCK_MLPB = 4231
        STOCK_MLPQ = 4232
        STOCK_MLPZ = 4233
        STOCK_MLQD = 4234
        STOCK_MLR = 4235
        STOCK_MLSS = 4236
        STOCK_MLTI = 4237
        STOCK_MLVF = 4238
        STOCK_MMAC = 4239
        STOCK_MMC = 4240
        STOCK_MMD = 4241
        STOCK_MMDM = 4242
        STOCK_MMDMR = 4243
        STOCK_MMDMU = 4244
        STOCK_MMDMW = 4245
        STOCK_MMI = 4246
        STOCK_MMIT = 4247
        STOCK_MMLP = 4248
        STOCK_MMM = 4249
        STOCK_MMP = 4250
        STOCK_MMS = 4251
        STOCK_MMSI = 4252
        STOCK_MMT = 4253
        STOCK_MMU = 4254
        STOCK_MMV = 4255
        STOCK_MMYT = 4256
        STOCK_MN = 4257
        STOCK_MNDO = 4258
        STOCK_MNE = 4259
        STOCK_MNGA = 4260
        STOCK_MNI = 4261
        STOCK_MNK = 4262
        STOCK_MNKD = 4263
        STOCK_MNOV = 4264
        STOCK_MNP = 4265
        STOCK_MNR = 4266
        STOCK_MNRO = 4267
        STOCK_MNR_C = 4268
        STOCK_MNST = 4269
        STOCK_MNTA = 4270
        STOCK_MNTX = 4271
        STOCK_MO = 4272
        STOCK_MOBL = 4273
        STOCK_MOC = 4274
        STOCK_MOD = 4275
        STOCK_MODN = 4276
        STOCK_MOFG = 4277
        STOCK_MOG__A = 4278
        STOCK_MOG__B = 4279
        STOCK_MOGLC = 4280
        STOCK_MOH = 4281
        STOCK_MOLC = 4282
        STOCK_MOMO = 4283
        STOCK_MON = 4284
        STOCK_MORN = 4285
        STOCK_MOS = 4286
        STOCK_MOSC__U = 4287
        STOCK_MOSY = 4288
        STOCK_MOTI = 4289
        STOCK_MOV = 4290
        STOCK_MOXC = 4291
        STOCK_MPA = 4292
        STOCK_MPAA = 4293
        STOCK_MPAC = 4294
        STOCK_MPACU = 4295
        STOCK_MPACW = 4296
        STOCK_MPB = 4297
        STOCK_MPC = 4298
        STOCK_MPCT = 4299
        STOCK_MPLX = 4300
        STOCK_MPO = 4301
        STOCK_MPV = 4302
        STOCK_MPVD = 4303
        STOCK_MPW = 4304
        STOCK_MPWR = 4305
        STOCK_MPX = 4306
        STOCK_MP_D = 4307
        STOCK_MQT = 4308
        STOCK_MQY = 4309
        STOCK_MRAM = 4310
        STOCK_MRBK = 4311
        STOCK_MRC = 4312
        STOCK_MRCC = 4313
        STOCK_MRCY = 4314
        STOCK_MRDN = 4315
        STOCK_MRDNW = 4316
        STOCK_MRIN = 4317
        STOCK_MRK = 4318
        STOCK_MRLN = 4319
        STOCK_MRNS = 4320
        STOCK_MRO = 4321
        STOCK_MRRL = 4322
        STOCK_MRSN = 4323
        STOCK_MRT = 4324
        STOCK_MRTN = 4325
        STOCK_MRTX = 4326
        STOCK_MRUS = 4327
        STOCK_MRVL = 4328
        STOCK_MS = 4329
        STOCK_MSA = 4330
        STOCK_MSB = 4331
        STOCK_MSBF = 4332
        STOCK_MSBI = 4333
        STOCK_MSCA = 4334
        STOCK_MSCC = 4335
        STOCK_MSCI = 4336
        STOCK_MSD = 4337
        STOCK_MSDI = 4338
        STOCK_MSDIW = 4339
        STOCK_MSEX = 4340
        STOCK_MSF = 4341
        STOCK_MSFG = 4342
        STOCK_MSFT = 4343
        STOCK_MSG = 4344
        STOCK_MSGN = 4345
        STOCK_MSI = 4346
        STOCK_MSL = 4347
        STOCK_MSM = 4348
        STOCK_MSN = 4349
        STOCK_MSON = 4350
        STOCK_MSP = 4351
        STOCK_MSTR = 4352
        STOCK_MS_A = 4353
        STOCK_MS_E = 4354
        STOCK_MS_F = 4355
        STOCK_MS_G = 4356
        STOCK_MS_I = 4357
        STOCK_MS_K = 4358
        STOCK_MT = 4359
        STOCK_MTB__WS = 4360
        STOCK_MTB = 4361
        STOCK_MTBC = 4362
        STOCK_MTBCP = 4363
        STOCK_MTB_ = 4364
        STOCK_MTB_C = 4365
        STOCK_MTCH = 4366
        STOCK_MTD = 4367
        STOCK_MTDR = 4368
        STOCK_MTEM = 4369
        STOCK_MTEX = 4370
        STOCK_MTFB = 4371
        STOCK_MTFBW = 4372
        STOCK_MTG = 4373
        STOCK_MTGE = 4374
        STOCK_MTGEP = 4375
        STOCK_MTH = 4376
        STOCK_MTL = 4377
        STOCK_MTLS = 4378
        STOCK_MTL_ = 4379
        STOCK_MTN = 4380
        STOCK_MTNB = 4381
        STOCK_MTOR = 4382
        STOCK_MTP = 4383
        STOCK_MTR = 4384
        STOCK_MTRN = 4385
        STOCK_MTRX = 4386
        STOCK_MTSC = 4387
        STOCK_MTSI = 4388
        STOCK_MTSL = 4389
        STOCK_MTT = 4390
        STOCK_MTU = 4391
        STOCK_MTW = 4392
        STOCK_MTX = 4393
        STOCK_MTZ = 4394
        STOCK_MU = 4395
        STOCK_MUA = 4396
        STOCK_MUC = 4397
        STOCK_MUE = 4398
        STOCK_MUH = 4399
        STOCK_MUI = 4400
        STOCK_MUJ = 4401
        STOCK_MULE = 4402
        STOCK_MUR = 4403
        STOCK_MUS = 4404
        STOCK_MUSA = 4405
        STOCK_MUX = 4406
        STOCK_MVC = 4407
        STOCK_MVCB = 4408
        STOCK_MVF = 4409
        STOCK_MVIN = 4410
        STOCK_MVIS = 4411
        STOCK_MVO = 4412
        STOCK_MVT = 4413
        STOCK_MWA = 4414
        STOCK_MX = 4415
        STOCK_MXC = 4416
        STOCK_MXDU = 4417
        STOCK_MXE = 4418
        STOCK_MXF = 4419
        STOCK_MXIM = 4420
        STOCK_MXL = 4421
        STOCK_MXWL = 4422
        STOCK_MYC = 4423
        STOCK_MYD = 4424
        STOCK_MYE = 4425
        STOCK_MYF = 4426
        STOCK_MYGN = 4427
        STOCK_MYI = 4428
        STOCK_MYJ = 4429
        STOCK_MYL = 4430
        STOCK_MYN = 4431
        STOCK_MYND = 4432
        STOCK_MYNDW = 4433
        STOCK_MYO = 4434
        STOCK_MYOK = 4435
        STOCK_MYOS = 4436
        STOCK_MYOV = 4437
        STOCK_MYRG = 4438
        STOCK_MYSZ = 4439
        STOCK_MZA = 4440
        STOCK_MZF = 4441
        STOCK_MZOR = 4442
        STOCK_NAC = 4443
        STOCK_NAD = 4444
        STOCK_NAII = 4445
        STOCK_NAIL = 4446
        STOCK_NAK = 4447
        STOCK_NAKD = 4448
        STOCK_NAN = 4449
        STOCK_NANO = 4450
        STOCK_NANR = 4451
        STOCK_NAO = 4452
        STOCK_NAOV = 4453
        STOCK_NAP = 4454
        STOCK_NAT = 4455
        STOCK_NATH = 4456
        STOCK_NATI = 4457
        STOCK_NATR = 4458
        STOCK_NAUH = 4459
        STOCK_NAV = 4460
        STOCK_NAVB = 4461
        STOCK_NAVG = 4462
        STOCK_NAVI = 4463
        STOCK_NAV_D = 4464
        STOCK_NAZ = 4465
        STOCK_NBB = 4466
        STOCK_NBD = 4467
        STOCK_NBEV = 4468
        STOCK_NBH = 4469
        STOCK_NBHC = 4470
        STOCK_NBIX = 4471
        STOCK_NBL = 4472
        STOCK_NBLX = 4473
        STOCK_NBN = 4474
        STOCK_NBO = 4475
        STOCK_NBR = 4476
        STOCK_NBRV = 4477
        STOCK_NBTB = 4478
        STOCK_NBW = 4479
        STOCK_NBY = 4480
        STOCK_NC = 4481
        STOCK_NCA = 4482
        STOCK_NCB = 4483
        STOCK_NCBS = 4484
        STOCK_NCI = 4485
        STOCK_NCLH = 4486
        STOCK_NCMI = 4487
        STOCK_NCNA = 4488
        STOCK_NCOM = 4489
        STOCK_NCR = 4490
        STOCK_NCS = 4491
        STOCK_NCSM = 4492
        STOCK_NCTY = 4493
        STOCK_NCV = 4494
        STOCK_NCZ = 4495
        STOCK_NDAQ = 4496
        STOCK_NDLS = 4497
        STOCK_NDP = 4498
        STOCK_NDRA = 4499
        STOCK_NDRAW = 4500
        STOCK_NDRM = 4501
        STOCK_NDRO = 4502
        STOCK_NDSN = 4503
        STOCK_NE = 4504
        STOCK_NEA = 4505
        STOCK_NEE = 4506
        STOCK_NEE_C__CL = 4507
        STOCK_NEE_C = 4508
        STOCK_NEE_G__CL = 4509
        STOCK_NEE_H__CL = 4510
        STOCK_NEE_I = 4511
        STOCK_NEE_J = 4512
        STOCK_NEE_K = 4513
        STOCK_NEE_Q = 4514
        STOCK_NEE_R = 4515
        STOCK_NEM = 4516
        STOCK_NEN = 4517
        STOCK_NEO = 4518
        STOCK_NEOG = 4519
        STOCK_NEON = 4520
        STOCK_NEOS = 4521
        STOCK_NEOT = 4522
        STOCK_NEP = 4523
        STOCK_NEPT = 4524
        STOCK_NERV = 4525
        STOCK_NES = 4526
        STOCK_NESR = 4527
        STOCK_NESRW = 4528
        STOCK_NETE = 4529
        STOCK_NETS = 4530
        STOCK_NEU = 4531
        STOCK_NEV = 4532
        STOCK_NEWA = 4533
        STOCK_NEWM = 4534
        STOCK_NEWR = 4535
        STOCK_NEWS = 4536
        STOCK_NEWT = 4537
        STOCK_NEWTL = 4538
        STOCK_NEWTZ = 4539
        STOCK_NEXA = 4540
        STOCK_NEXT = 4541
        STOCK_NEXTW = 4542
        STOCK_NFBK = 4543
        STOCK_NFEC = 4544
        STOCK_NFG = 4545
        STOCK_NFJ = 4546
        STOCK_NFLT = 4547
        STOCK_NFLX = 4548
        STOCK_NFX = 4549
        STOCK_NG = 4550
        STOCK_NGD = 4551
        STOCK_NGG = 4552
        STOCK_NGHC = 4553
        STOCK_NGHCN = 4554
        STOCK_NGHCO = 4555
        STOCK_NGHCP = 4556
        STOCK_NGHCZ = 4557
        STOCK_NGL = 4558
        STOCK_NGLS_A = 4559
        STOCK_NGL_B = 4560
        STOCK_NGS = 4561
        STOCK_NGVC = 4562
        STOCK_NGVT = 4563
        STOCK_NH = 4564
        STOCK_NHA = 4565
        STOCK_NHC = 4566
        STOCK_NHF = 4567
        STOCK_NHI = 4568
        STOCK_NHLD = 4569
        STOCK_NHLDW = 4570
        STOCK_NHS = 4571
        STOCK_NHTC = 4572
        STOCK_NI = 4573
        STOCK_NICE = 4574
        STOCK_NICK = 4575
        STOCK_NID = 4576
        STOCK_NIE = 4577
        STOCK_NIHD = 4578
        STOCK_NIM = 4579
        STOCK_NIQ = 4580
        STOCK_NITE = 4581
        STOCK_NJR = 4582
        STOCK_NJV = 4583
        STOCK_NK = 4584
        STOCK_NKE = 4585
        STOCK_NKG = 4586
        STOCK_NKSH = 4587
        STOCK_NKTR = 4588
        STOCK_NKX = 4589
        STOCK_NL = 4590
        STOCK_NLNK = 4591
        STOCK_NLS = 4592
        STOCK_NLSN = 4593
        STOCK_NLST = 4594
        STOCK_NLY = 4595
        STOCK_NLY_C = 4596
        STOCK_NLY_D = 4597
        STOCK_NLY_E = 4598
        STOCK_NLY_F = 4599
        STOCK_NM = 4600
        STOCK_NMFC = 4601
        STOCK_NMI = 4602
        STOCK_NMIH = 4603
        STOCK_NMK_B = 4604
        STOCK_NMK_C = 4605
        STOCK_NML = 4606
        STOCK_NMM = 4607
        STOCK_NMR = 4608
        STOCK_NMRX = 4609
        STOCK_NMS = 4610
        STOCK_NMT = 4611
        STOCK_NMY = 4612
        STOCK_NMZ = 4613
        STOCK_NM_G = 4614
        STOCK_NM_H = 4615
        STOCK_NNA = 4616
        STOCK_NNBR = 4617
        STOCK_NNC = 4618
        STOCK_NNDM = 4619
        STOCK_NNI = 4620
        STOCK_NNN = 4621
        STOCK_NNN_E = 4622
        STOCK_NNN_F = 4623
        STOCK_NNVC = 4624
        STOCK_NNY = 4625
        STOCK_NOA = 4626
        STOCK_NOAH = 4627
        STOCK_NOC = 4628
        STOCK_NODK = 4629
        STOCK_NOG = 4630
        STOCK_NOK = 4631
        STOCK_NOM = 4632
        STOCK_NOMD = 4633
        STOCK_NOV = 4634
        STOCK_NOVN = 4635
        STOCK_NOVT = 4636
        STOCK_NOW = 4637
        STOCK_NP = 4638
        STOCK_NPK = 4639
        STOCK_NPN = 4640
        STOCK_NPO = 4641
        STOCK_NPTN = 4642
        STOCK_NPV = 4643
        STOCK_NQ = 4644
        STOCK_NQP = 4645
        STOCK_NR = 4646
        STOCK_NRCIA = 4647
        STOCK_NRCIB = 4648
        STOCK_NRE = 4649
        STOCK_NRG = 4650
        STOCK_NRIM = 4651
        STOCK_NRK = 4652
        STOCK_NRO = 4653
        STOCK_NRP = 4654
        STOCK_NRT = 4655
        STOCK_NRZ = 4656
        STOCK_NS = 4657
        STOCK_NSA = 4658
        STOCK_NSA_A = 4659
        STOCK_NSC = 4660
        STOCK_NSEC = 4661
        STOCK_NSH = 4662
        STOCK_NSIT = 4663
        STOCK_NSL = 4664
        STOCK_NSM = 4665
        STOCK_NSP = 4666
        STOCK_NSPR__WS__B = 4667
        STOCK_NSPR__WS = 4668
        STOCK_NSPR = 4669
        STOCK_NSS = 4670
        STOCK_NSSC = 4671
        STOCK_NSTG = 4672
        STOCK_NSU = 4673
        STOCK_NSYS = 4674
        STOCK_NS_A = 4675
        STOCK_NS_B = 4676
        STOCK_NTAP = 4677
        STOCK_NTB = 4678
        STOCK_NTC = 4679
        STOCK_NTCT = 4680
        STOCK_NTEC = 4681
        STOCK_NTES = 4682
        STOCK_NTG = 4683
        STOCK_NTGR = 4684
        STOCK_NTIC = 4685
        STOCK_NTIP = 4686
        STOCK_NTL = 4687
        STOCK_NTLA = 4688
        STOCK_NTN = 4689
        STOCK_NTNX = 4690
        STOCK_NTP = 4691
        STOCK_NTRA = 4692
        STOCK_NTRI = 4693
        STOCK_NTRP = 4694
        STOCK_NTRS = 4695
        STOCK_NTRSP = 4696
        STOCK_NTWK = 4697
        STOCK_NTX = 4698
        STOCK_NTZ = 4699
        STOCK_NUAG = 4700
        STOCK_NUAN = 4701
        STOCK_NUBD = 4702
        STOCK_NUDM = 4703
        STOCK_NUE = 4704
        STOCK_NUEM = 4705
        STOCK_NULG = 4706
        STOCK_NULV = 4707
        STOCK_NUM = 4708
        STOCK_NUMG = 4709
        STOCK_NUMV = 4710
        STOCK_NUO = 4711
        STOCK_NURE = 4712
        STOCK_NURO = 4713
        STOCK_NUROW = 4714
        STOCK_NUS = 4715
        STOCK_NUSA = 4716
        STOCK_NUSC = 4717
        STOCK_NUV = 4718
        STOCK_NUVA = 4719
        STOCK_NUW = 4720
        STOCK_NVAX = 4721
        STOCK_NVCN = 4722
        STOCK_NVCR = 4723
        STOCK_NVDA = 4724
        STOCK_NVEC = 4725
        STOCK_NVEE = 4726
        STOCK_NVFY = 4727
        STOCK_NVG = 4728
        STOCK_NVGN = 4729
        STOCK_NVGS = 4730
        STOCK_NVIV = 4731
        STOCK_NVLN = 4732
        STOCK_NVMI = 4733
        STOCK_NVO = 4734
        STOCK_NVR = 4735
        STOCK_NVRO = 4736
        STOCK_NVS = 4737
        STOCK_NVTA = 4738
        STOCK_NVTR = 4739
        STOCK_NVUS = 4740
        STOCK_NWBI = 4741
        STOCK_NWE = 4742
        STOCK_NWFL = 4743
        STOCK_NWHM = 4744
        STOCK_NWL = 4745
        STOCK_NWLI = 4746
        STOCK_NWN = 4747
        STOCK_NWPX = 4748
        STOCK_NWS = 4749
        STOCK_NWSA = 4750
        STOCK_NWY = 4751
        STOCK_NW_C__CL = 4752
        STOCK_NX = 4753
        STOCK_NXC = 4754
        STOCK_NXE = 4755
        STOCK_NXEO = 4756
        STOCK_NXEOU = 4757
        STOCK_NXEOW = 4758
        STOCK_NXJ = 4759
        STOCK_NXN = 4760
        STOCK_NXP = 4761
        STOCK_NXPI = 4762
        STOCK_NXQ = 4763
        STOCK_NXR = 4764
        STOCK_NXRT = 4765
        STOCK_NXST = 4766
        STOCK_NXTD = 4767
        STOCK_NXTDW = 4768
        STOCK_NXTM = 4769
        STOCK_NYCB = 4770
        STOCK_NYCB_A = 4771
        STOCK_NYCB_U = 4772
        STOCK_NYH = 4773
        STOCK_NYLD__A = 4774
        STOCK_NYLD = 4775
        STOCK_NYMT = 4776
        STOCK_NYMTN = 4777
        STOCK_NYMTO = 4778
        STOCK_NYMTP = 4779
        STOCK_NYMX = 4780
        STOCK_NYNY = 4781
        STOCK_NYRT = 4782
        STOCK_NYT = 4783
        STOCK_NYV = 4784
        STOCK_NZF = 4785
        STOCK_O = 4786
        STOCK_OA = 4787
        STOCK_OACQ = 4788
        STOCK_OACQR = 4789
        STOCK_OACQU = 4790
        STOCK_OACQW = 4791
        STOCK_OAK = 4792
        STOCK_OAKS = 4793
        STOCK_OAKS_A = 4794
        STOCK_OAPH = 4795
        STOCK_OAS = 4796
        STOCK_OASI = 4797
        STOCK_OASM = 4798
        STOCK_OBAS = 4799
        STOCK_OBCI = 4800
        STOCK_OBE = 4801
        STOCK_OBLN = 4802
        STOCK_OBOR = 4803
        STOCK_OBSV = 4804
        STOCK_OC = 4805
        STOCK_OCC = 4806
        STOCK_OCFC = 4807
        STOCK_OCIO = 4808
        STOCK_OCIP = 4809
        STOCK_OCLR = 4810
        STOCK_OCN = 4811
        STOCK_OCRX = 4812
        STOCK_OCSI = 4813
        STOCK_OCSL = 4814
        STOCK_OCSLL = 4815
        STOCK_OCUL = 4816
        STOCK_OCX = 4817
        STOCK_ODC = 4818
        STOCK_ODFL = 4819
        STOCK_ODP = 4820
        STOCK_OEC = 4821
        STOCK_OESX = 4822
        STOCK_OEUH = 4823
        STOCK_OEUR = 4824
        STOCK_OEW = 4825
        STOCK_OFC = 4826
        STOCK_OFED = 4827
        STOCK_OFG = 4828
        STOCK_OFG_A = 4829
        STOCK_OFG_B = 4830
        STOCK_OFG_D = 4831
        STOCK_OFIX = 4832
        STOCK_OFLX = 4833
        STOCK_OFS = 4834
        STOCK_OGCP = 4835
        STOCK_OGE = 4836
        STOCK_OGEN = 4837
        STOCK_OGS = 4838
        STOCK_OHAI = 4839
        STOCK_OHGI = 4840
        STOCK_OHI = 4841
        STOCK_OHRP = 4842
        STOCK_OI = 4843
        STOCK_OIA = 4844
        STOCK_OIBR__C = 4845
        STOCK_OII = 4846
        STOCK_OIIL = 4847
        STOCK_OIIM = 4848
        STOCK_OILB = 4849
        STOCK_OILD = 4850
        STOCK_OILK = 4851
        STOCK_OILU = 4852
        STOCK_OILX = 4853
        STOCK_OIS = 4854
        STOCK_OKE = 4855
        STOCK_OKSB = 4856
        STOCK_OKTA = 4857
        STOCK_OLBK = 4858
        STOCK_OLD = 4859
        STOCK_OLED = 4860
        STOCK_OLLI = 4861
        STOCK_OLN = 4862
        STOCK_OLP = 4863
        STOCK_OMAA = 4864
        STOCK_OMAB = 4865
        STOCK_OMAM = 4866
        STOCK_OMC = 4867
        STOCK_OMCL = 4868
        STOCK_OME = 4869
        STOCK_OMED = 4870
        STOCK_OMER = 4871
        STOCK_OMEX = 4872
        STOCK_OMF = 4873
        STOCK_OMFL = 4874
        STOCK_OMFS = 4875
        STOCK_OMI = 4876
        STOCK_OMN = 4877
        STOCK_OMNT = 4878
        STOCK_OMP = 4879
        STOCK_ON = 4880
        STOCK_ONB = 4881
        STOCK_ONCE = 4882
        STOCK_ONCS = 4883
        STOCK_ONDK = 4884
        STOCK_ONEO = 4885
        STOCK_ONEV = 4886
        STOCK_ONEY = 4887
        STOCK_ONP = 4888
        STOCK_ONS = 4889
        STOCK_ONSIW = 4890
        STOCK_ONSIZ = 4891
        STOCK_ONTL = 4892
        STOCK_ONTX = 4893
        STOCK_ONTXW = 4894
        STOCK_ONVI = 4895
        STOCK_ONVO = 4896
        STOCK_OOMA = 4897
        STOCK_OPB = 4898
        STOCK_OPGN = 4899
        STOCK_OPGNW = 4900
        STOCK_OPHC = 4901
        STOCK_OPHT = 4902
        STOCK_OPK = 4903
        STOCK_OPNT = 4904
        STOCK_OPOF = 4905
        STOCK_OPP = 4906
        STOCK_OPTN = 4907
        STOCK_OPTT = 4908
        STOCK_OPY = 4909
        STOCK_OR = 4910
        STOCK_ORA = 4911
        STOCK_ORAN = 4912
        STOCK_ORBC = 4913
        STOCK_ORBK = 4914
        STOCK_ORC = 4915
        STOCK_ORCL = 4916
        STOCK_OREX = 4917
        STOCK_ORG = 4918
        STOCK_ORI = 4919
        STOCK_ORIG = 4920
        STOCK_ORIT = 4921
        STOCK_ORLY = 4922
        STOCK_ORM = 4923
        STOCK_ORMP = 4924
        STOCK_ORN = 4925
        STOCK_ORPN = 4926
        STOCK_ORRF = 4927
        STOCK_OSB = 4928
        STOCK_OSBC = 4929
        STOCK_OSBCP = 4930
        STOCK_OSG = 4931
        STOCK_OSIS = 4932
        STOCK_OSK = 4933
        STOCK_OSLE = 4934
        STOCK_OSN = 4935
        STOCK_OSPR = 4936
        STOCK_OSPRU = 4937
        STOCK_OSPRW = 4938
        STOCK_OSTK = 4939
        STOCK_OSUR = 4940
        STOCK_OTEL = 4941
        STOCK_OTEX = 4942
        STOCK_OTG = 4943
        STOCK_OTIC = 4944
        STOCK_OTIV = 4945
        STOCK_OTTR = 4946
        STOCK_OTTW = 4947
        STOCK_OUSA = 4948
        STOCK_OUSM = 4949
        STOCK_OUT = 4950
        STOCK_OVAS = 4951
        STOCK_OVBC = 4952
        STOCK_OVID = 4953
        STOCK_OVLY = 4954
        STOCK_OXBR = 4955
        STOCK_OXBRW = 4956
        STOCK_OXFD = 4957
        STOCK_OXLC = 4958
        STOCK_OXLCM = 4959
        STOCK_OXLCO = 4960
        STOCK_OXM = 4961
        STOCK_OXY = 4962
        STOCK_OZM = 4963
        STOCK_OZRK = 4964
        STOCK_P = 4965
        STOCK_PAA = 4966
        STOCK_PAAS = 4967
        STOCK_PAC = 4968
        STOCK_PACB = 4969
        STOCK_PACW = 4970
        STOCK_PAG = 4971
        STOCK_PAGP = 4972
        STOCK_PAH = 4973
        STOCK_PAHC = 4974
        STOCK_PAI = 4975
        STOCK_PAM = 4976
        STOCK_PANL = 4977
        STOCK_PANW = 4978
        STOCK_PAR = 4979
        STOCK_PARR = 4980
        STOCK_PATI = 4981
        STOCK_PATK = 4982
        STOCK_PAVE = 4983
        STOCK_PAVM = 4984
        STOCK_PAVMW = 4985
        STOCK_PAY = 4986
        STOCK_PAYC = 4987
        STOCK_PAYX = 4988
        STOCK_PB = 4989
        STOCK_PBA = 4990
        STOCK_PBB = 4991
        STOCK_PBBI = 4992
        STOCK_PBCT = 4993
        STOCK_PBCTP = 4994
        STOCK_PBDM = 4995
        STOCK_PBEE = 4996
        STOCK_PBF = 4997
        STOCK_PBFX = 4998
        STOCK_PBH = 4999
        STOCK_PBHC = 5000
        STOCK_PBI = 5001
        STOCK_PBIB = 5002
        STOCK_PBIO = 5003
        STOCK_PBIP = 5004
        STOCK_PBI_B = 5005
        STOCK_PBMD = 5006
        STOCK_PBNC = 5007
        STOCK_PBND = 5008
        STOCK_PBPB = 5009
        STOCK_PBR__A = 5010
        STOCK_PBR = 5011
        STOCK_PBSK = 5012
        STOCK_PBSM = 5013
        STOCK_PBT = 5014
        STOCK_PBUS = 5015
        STOCK_PBYI = 5016
        STOCK_PCAR = 5017
        STOCK_PCBK = 5018
        STOCK_PCF = 5019
        STOCK_PCG = 5020
        STOCK_PCG_A = 5021
        STOCK_PCG_B = 5022
        STOCK_PCG_C = 5023
        STOCK_PCG_D = 5024
        STOCK_PCG_E = 5025
        STOCK_PCG_G = 5026
        STOCK_PCG_H = 5027
        STOCK_PCG_I = 5028
        STOCK_PCH = 5029
        STOCK_PCI = 5030
        STOCK_PCK = 5031
        STOCK_PCLN = 5032
        STOCK_PCM = 5033
        STOCK_PCMI = 5034
        STOCK_PCN = 5035
        STOCK_PCO = 5036
        STOCK_PCOM = 5037
        STOCK_PCQ = 5038
        STOCK_PCRX = 5039
        STOCK_PCSB = 5040
        STOCK_PCTI = 5041
        STOCK_PCTY = 5042
        STOCK_PCYG = 5043
        STOCK_PCYO = 5044
        STOCK_PDCE = 5045
        STOCK_PDCO = 5046
        STOCK_PDEX = 5047
        STOCK_PDFS = 5048
        STOCK_PDI = 5049
        STOCK_PDLB = 5050
        STOCK_PDLI = 5051
        STOCK_PDM = 5052
        STOCK_PDP = 5053
        STOCK_PDS = 5054
        STOCK_PDT = 5055
        STOCK_PDVW = 5056
        STOCK_PE = 5057
        STOCK_PEB = 5058
        STOCK_PEBK = 5059
        STOCK_PEBO = 5060
        STOCK_PEB_C = 5061
        STOCK_PEB_D = 5062
        STOCK_PED = 5063
        STOCK_PEG = 5064
        STOCK_PEGA = 5065
        STOCK_PEGI = 5066
        STOCK_PEI = 5067
        STOCK_PEIX = 5068
        STOCK_PEI_B = 5069
        STOCK_PEI_C = 5070
        STOCK_PEI_D = 5071
        STOCK_PEN = 5072
        STOCK_PENN = 5073
        STOCK_PEO = 5074
        STOCK_PEP = 5075
        STOCK_PER = 5076
        STOCK_PERI = 5077
        STOCK_PERY = 5078
        STOCK_PES = 5079
        STOCK_PESI = 5080
        STOCK_PETQ = 5081
        STOCK_PETS = 5082
        STOCK_PETX = 5083
        STOCK_PETZ = 5084
        STOCK_PF = 5085
        STOCK_PFBC = 5086
        STOCK_PFBI = 5087
        STOCK_PFBX = 5088
        STOCK_PFD = 5089
        STOCK_PFE = 5090
        STOCK_PFFD = 5091
        STOCK_PFFR = 5092
        STOCK_PFG = 5093
        STOCK_PFGC = 5094
        STOCK_PFH = 5095
        STOCK_PFI = 5096
        STOCK_PFIE = 5097
        STOCK_PFIN = 5098
        STOCK_PFIS = 5099
        STOCK_PFK = 5100
        STOCK_PFL = 5101
        STOCK_PFLT = 5102
        STOCK_PFMT = 5103
        STOCK_PFN = 5104
        STOCK_PFNX = 5105
        STOCK_PFO = 5106
        STOCK_PFPT = 5107
        STOCK_PFS = 5108
        STOCK_PFSI = 5109
        STOCK_PFSW = 5110
        STOCK_PG = 5111
        STOCK_PGC = 5112
        STOCK_PGEM = 5113
        STOCK_PGH = 5114
        STOCK_PGLC = 5115
        STOCK_PGNX = 5116
        STOCK_PGP = 5117
        STOCK_PGR = 5118
        STOCK_PGRE = 5119
        STOCK_PGTI = 5120
        STOCK_PGZ = 5121
        STOCK_PH = 5122
        STOCK_PHD = 5123
        STOCK_PHG = 5124
        STOCK_PHH = 5125
        STOCK_PHI = 5126
        STOCK_PHII = 5127
        STOCK_PHIIK = 5128
        STOCK_PHK = 5129
        STOCK_PHM = 5130
        STOCK_PHO = 5131
        STOCK_PHT = 5132
        STOCK_PHX = 5133
        STOCK_PHYS = 5134
        STOCK_PI = 5135
        STOCK_PICO = 5136
        STOCK_PID = 5137
        STOCK_PIH = 5138
        STOCK_PII = 5139
        STOCK_PIM = 5140
        STOCK_PINC = 5141
        STOCK_PIR = 5142
        STOCK_PIRS = 5143
        STOCK_PIXY = 5144
        STOCK_PIY = 5145
        STOCK_PIZ = 5146
        STOCK_PJC = 5147
        STOCK_PJH = 5148
        STOCK_PJT = 5149
        STOCK_PK = 5150
        STOCK_PKBK = 5151
        STOCK_PKD = 5152
        STOCK_PKE = 5153
        STOCK_PKG = 5154
        STOCK_PKI = 5155
        STOCK_PKO = 5156
        STOCK_PKOH = 5157
        STOCK_PKW = 5158
        STOCK_PKX = 5159
        STOCK_PKY = 5160
        STOCK_PLAB = 5161
        STOCK_PLAY = 5162
        STOCK_PLBC = 5163
        STOCK_PLCE = 5164
        STOCK_PLD = 5165
        STOCK_PLG = 5166
        STOCK_PLM = 5167
        STOCK_PLNT = 5168
        STOCK_PLOW = 5169
        STOCK_PLPC = 5170
        STOCK_PLPM = 5171
        STOCK_PLSE = 5172
        STOCK_PLT = 5173
        STOCK_PLUG = 5174
        STOCK_PLUS = 5175
        STOCK_PLW = 5176
        STOCK_PLX = 5177
        STOCK_PLXP = 5178
        STOCK_PLXS = 5179
        STOCK_PLYA = 5180
        STOCK_PLYM = 5181
        STOCK_PLYM_A = 5182
        STOCK_PM = 5183
        STOCK_PMBC = 5184
        STOCK_PMC = 5185
        STOCK_PMD = 5186
        STOCK_PME = 5187
        STOCK_PMF = 5188
        STOCK_PML = 5189
        STOCK_PMM = 5190
        STOCK_PMO = 5191
        STOCK_PMOM = 5192
        STOCK_PMPT = 5193
        STOCK_PMT = 5194
        STOCK_PMTS = 5195
        STOCK_PMT_A = 5196
        STOCK_PMT_B = 5197
        STOCK_PMX = 5198
        STOCK_PN = 5199
        STOCK_PNBK = 5200
        STOCK_PNC__WS = 5201
        STOCK_PNC = 5202
        STOCK_PNC_P = 5203
        STOCK_PNC_Q = 5204
        STOCK_PNF = 5205
        STOCK_PNFP = 5206
        STOCK_PNI = 5207
        STOCK_PNK = 5208
        STOCK_PNM = 5209
        STOCK_PNNT = 5210
        STOCK_PNR = 5211
        STOCK_PNRG = 5212
        STOCK_PNTR = 5213
        STOCK_PNW = 5214
        STOCK_PODD = 5215
        STOCK_POL = 5216
        STOCK_POLA = 5217
        STOCK_POOL = 5218
        STOCK_POPE = 5219
        STOCK_POR = 5220
        STOCK_POST = 5221
        STOCK_POT = 5222
        STOCK_POWI = 5223
        STOCK_POWL = 5224
        STOCK_PPBI = 5225
        STOCK_PPC = 5226
        STOCK_PPDF = 5227
        STOCK_PPG = 5228
        STOCK_PPHM = 5229
        STOCK_PPHMP = 5230
        STOCK_PPIH = 5231
        STOCK_PPL = 5232
        STOCK_PPLN = 5233
        STOCK_PPR = 5234
        STOCK_PPSI = 5235
        STOCK_PPT = 5236
        STOCK_PPX = 5237
        STOCK_PQ = 5238
        STOCK_PQG = 5239
        STOCK_PRA = 5240
        STOCK_PRAA = 5241
        STOCK_PRAH = 5242
        STOCK_PRAN = 5243
        STOCK_PRCP = 5244
        STOCK_PREF = 5245
        STOCK_PRE_F = 5246
        STOCK_PRE_G = 5247
        STOCK_PRE_H = 5248
        STOCK_PRE_I = 5249
        STOCK_PRFT = 5250
        STOCK_PRGO = 5251
        STOCK_PRGS = 5252
        STOCK_PRGX = 5253
        STOCK_PRH = 5254
        STOCK_PRI = 5255
        STOCK_PRIM = 5256
        STOCK_PRK = 5257
        STOCK_PRKR = 5258
        STOCK_PRLB = 5259
        STOCK_PRME = 5260
        STOCK_PRMW = 5261
        STOCK_PRNT = 5262
        STOCK_PRO = 5263
        STOCK_PROV = 5264
        STOCK_PRPH = 5265
        STOCK_PRPO = 5266
        STOCK_PRQR = 5267
        STOCK_PRSC = 5268
        STOCK_PRSS = 5269
        STOCK_PRTA = 5270
        STOCK_PRTK = 5271
        STOCK_PRTO = 5272
        STOCK_PRTS = 5273
        STOCK_PRTY = 5274
        STOCK_PRU = 5275
        STOCK_PSA = 5276
        STOCK_PSA_A = 5277
        STOCK_PSA_B = 5278
        STOCK_PSA_C = 5279
        STOCK_PSA_D = 5280
        STOCK_PSA_E = 5281
        STOCK_PSA_F = 5282
        STOCK_PSA_G = 5283
        STOCK_PSA_U = 5284
        STOCK_PSA_V = 5285
        STOCK_PSA_W = 5286
        STOCK_PSA_X = 5287
        STOCK_PSA_Y = 5288
        STOCK_PSA_Z = 5289
        STOCK_PSB = 5290
        STOCK_PSB_T = 5291
        STOCK_PSB_U = 5292
        STOCK_PSB_V = 5293
        STOCK_PSB_W = 5294
        STOCK_PSB_X = 5295
        STOCK_PSC = 5296
        STOCK_PSDO = 5297
        STOCK_PSDV = 5298
        STOCK_PSEC = 5299
        STOCK_PSET = 5300
        STOCK_PSF = 5301
        STOCK_PSL = 5302
        STOCK_PSLV = 5303
        STOCK_PSMB = 5304
        STOCK_PSMC = 5305
        STOCK_PSMG = 5306
        STOCK_PSMM = 5307
        STOCK_PSMT = 5308
        STOCK_PSO = 5309
        STOCK_PSTB = 5310
        STOCK_PSTG = 5311
        STOCK_PSTI = 5312
        STOCK_PSX = 5313
        STOCK_PSXP = 5314
        STOCK_PTC = 5315
        STOCK_PTCT = 5316
        STOCK_PTEN = 5317
        STOCK_PTEU = 5318
        STOCK_PTF = 5319
        STOCK_PTGX = 5320
        STOCK_PTH = 5321
        STOCK_PTI = 5322
        STOCK_PTIE = 5323
        STOCK_PTLA = 5324
        STOCK_PTLC = 5325
        STOCK_PTMC = 5326
        STOCK_PTN = 5327
        STOCK_PTNQ = 5328
        STOCK_PTNR = 5329
        STOCK_PTR = 5330
        STOCK_PTSI = 5331
        STOCK_PTX = 5332
        STOCK_PTY = 5333
        STOCK_PUB = 5334
        STOCK_PUI = 5335
        STOCK_PUK = 5336
        STOCK_PUK_ = 5337
        STOCK_PUK_A = 5338
        STOCK_PULM = 5339
        STOCK_PUMP = 5340
        STOCK_PUTW = 5341
        STOCK_PVAC = 5342
        STOCK_PVAL = 5343
        STOCK_PVBC = 5344
        STOCK_PVG = 5345
        STOCK_PVH = 5346
        STOCK_PW = 5347
        STOCK_PWOD = 5348
        STOCK_PWR = 5349
        STOCK_PW_A = 5350
        STOCK_PX = 5351
        STOCK_PXD = 5352
        STOCK_PXI = 5353
        STOCK_PXLW = 5354
        STOCK_PXS = 5355
        STOCK_PXUS = 5356
        STOCK_PY = 5357
        STOCK_PYDS = 5358
        STOCK_PYN = 5359
        STOCK_PYPL = 5360
        STOCK_PYS = 5361
        STOCK_PYT = 5362
        STOCK_PYZ = 5363
        STOCK_PZC = 5364
        STOCK_PZE = 5365
        STOCK_PZG = 5366
        STOCK_PZN = 5367
        STOCK_PZRX = 5368
        STOCK_PZZA = 5369
        STOCK_Q = 5370
        STOCK_QADA = 5371
        STOCK_QADB = 5372
        STOCK_QBAK = 5373
        STOCK_QCOM = 5374
        STOCK_QCP = 5375
        STOCK_QCRH = 5376
        STOCK_QD = 5377
        STOCK_QDEL = 5378
        STOCK_QEP = 5379
        STOCK_QGEN = 5380
        STOCK_QGTA = 5381
        STOCK_QHC = 5382
        STOCK_QIWI = 5383
        STOCK_QLC = 5384
        STOCK_QLYS = 5385
        STOCK_QMOM = 5386
        STOCK_QNST = 5387
        STOCK_QQQX = 5388
        STOCK_QRHC = 5389
        STOCK_QRVO = 5390
        STOCK_QSII = 5391
        STOCK_QSR = 5392
        STOCK_QTM = 5393
        STOCK_QTNA = 5394
        STOCK_QTNT = 5395
        STOCK_QTRH = 5396
        STOCK_QTS = 5397
        STOCK_QTWO = 5398
        STOCK_QUAD = 5399
        STOCK_QUIK = 5400
        STOCK_QUMU = 5401
        STOCK_QUOT = 5402
        STOCK_QURE = 5403
        STOCK_QVAL = 5404
        STOCK_QVCA = 5405
        STOCK_QVCB = 5406
        STOCK_QVM = 5407
        STOCK_QXGG = 5408
        STOCK_QXMI = 5409
        STOCK_QXRR = 5410
        STOCK_QXTR = 5411
        STOCK_R = 5412
        STOCK_RA = 5413
        STOCK_RACE = 5414
        STOCK_RAD = 5415
        STOCK_RADA = 5416
        STOCK_RAIL = 5417
        STOCK_RAND = 5418
        STOCK_RARE = 5419
        STOCK_RARX = 5420
        STOCK_RAS = 5421
        STOCK_RAS_A = 5422
        STOCK_RAS_B = 5423
        STOCK_RAS_C = 5424
        STOCK_RATE = 5425
        STOCK_RAVE = 5426
        STOCK_RAVN = 5427
        STOCK_RBA = 5428
        STOCK_RBB = 5429
        STOCK_RBC = 5430
        STOCK_RBCAA = 5431
        STOCK_RBCN = 5432
        STOCK_RBIN = 5433
        STOCK_RBIO = 5434
        STOCK_RBPAA = 5435
        STOCK_RBS = 5436
        STOCK_RBS_S = 5437
        STOCK_RBUS = 5438
        STOCK_RCG = 5439
        STOCK_RCI = 5440
        STOCK_RCII = 5441
        STOCK_RCKY = 5442
        STOCK_RCL = 5443
        STOCK_RCM = 5444
        STOCK_RCMT = 5445
        STOCK_RCOM = 5446
        STOCK_RCON = 5447
        STOCK_RCS = 5448
        STOCK_RDC = 5449
        STOCK_RDCM = 5450
        STOCK_RDFN = 5451
        STOCK_RDHL = 5452
        STOCK_RDI = 5453
        STOCK_RDIB = 5454
        STOCK_RDN = 5455
        STOCK_RDNT = 5456
        STOCK_RDS__A = 5457
        STOCK_RDS__B = 5458
        STOCK_RDUS = 5459
        STOCK_RDWR = 5460
        STOCK_RDY = 5461
        STOCK_RE = 5462
        STOCK_RECN = 5463
        STOCK_REDU = 5464
        STOCK_REED = 5465
        STOCK_REEM = 5466
        STOCK_REFA = 5467
        STOCK_REFR = 5468
        STOCK_REG = 5469
        STOCK_REGI = 5470
        STOCK_REGN = 5471
        STOCK_REI = 5472
        STOCK_REIS = 5473
        STOCK_RELL = 5474
        STOCK_RELV = 5475
        STOCK_RELX = 5476
        STOCK_RELY = 5477
        STOCK_REML = 5478
        STOCK_REN = 5479
        STOCK_RENN = 5480
        STOCK_RENX = 5481
        STOCK_REPH = 5482
        STOCK_RES = 5483
        STOCK_RESI = 5484
        STOCK_RESN = 5485
        STOCK_RETA = 5486
        STOCK_REV = 5487
        STOCK_REVG = 5488
        STOCK_REX = 5489
        STOCK_REXR = 5490
        STOCK_REXR_A = 5491
        STOCK_REXX = 5492
        STOCK_RF = 5493
        STOCK_RFAP = 5494
        STOCK_RFCI = 5495
        STOCK_RFDA = 5496
        STOCK_RFDI = 5497
        STOCK_RFEM = 5498
        STOCK_RFEU = 5499
        STOCK_RFFC = 5500
        STOCK_RFI = 5501
        STOCK_RFIL = 5502
        STOCK_RFP = 5503
        STOCK_RFT = 5504
        STOCK_RFTA = 5505
        STOCK_RFUN = 5506
        STOCK_RF_A = 5507
        STOCK_RF_B = 5508
        STOCK_RGA = 5509
        STOCK_RGC = 5510
        STOCK_RGCO = 5511
        STOCK_RGEN = 5512
        STOCK_RGLB = 5513
        STOCK_RGLD = 5514
        STOCK_RGLS = 5515
        STOCK_RGNX = 5516
        STOCK_RGR = 5517
        STOCK_RGS = 5518
        STOCK_RGSE = 5519
        STOCK_RGT = 5520
        STOCK_RH = 5521
        STOCK_RHE = 5522
        STOCK_RHE_A = 5523
        STOCK_RHI = 5524
        STOCK_RHP = 5525
        STOCK_RHT = 5526
        STOCK_RIBT = 5527
        STOCK_RIBTW = 5528
        STOCK_RIC = 5529
        STOCK_RICE = 5530
        STOCK_RICK = 5531
        STOCK_RIF = 5532
        STOCK_RIG = 5533
        STOCK_RIGL = 5534
        STOCK_RILY = 5535
        STOCK_RILYL = 5536
        STOCK_RILYZ = 5537
        STOCK_RIO = 5538
        STOCK_RIOT = 5539
        STOCK_RISE = 5540
        STOCK_RIV = 5541
        STOCK_RIVR = 5542
        STOCK_RIVRW = 5543
        STOCK_RJF = 5544
        STOCK_RKDA = 5545
        STOCK_RL = 5546
        STOCK_RLGT = 5547
        STOCK_RLGT_A = 5548
        STOCK_RLGY = 5549
        STOCK_RLH = 5550
        STOCK_RLI = 5551
        STOCK_RLJ = 5552
        STOCK_RLJE = 5553
        STOCK_RLJ_A = 5554
        STOCK_RLOG = 5555
        STOCK_RM = 5556
        STOCK_RMAX = 5557
        STOCK_RMBL = 5558
        STOCK_RMBS = 5559
        STOCK_RMCF = 5560
        STOCK_RMD = 5561
        STOCK_RMGN = 5562
        STOCK_RMNI = 5563
        STOCK_RMNIU = 5564
        STOCK_RMNIW = 5565
        STOCK_RMP = 5566
        STOCK_RMPL_ = 5567
        STOCK_RMR = 5568
        STOCK_RMT = 5569
        STOCK_RMTI = 5570
        STOCK_RNDB = 5571
        STOCK_RNDM = 5572
        STOCK_RNDV = 5573
        STOCK_RNEM = 5574
        STOCK_RNET = 5575
        STOCK_RNG = 5576
        STOCK_RNGR = 5577
        STOCK_RNLC = 5578
        STOCK_RNMC = 5579
        STOCK_RNN = 5580
        STOCK_RNP = 5581
        STOCK_RNR = 5582
        STOCK_RNR_C = 5583
        STOCK_RNR_E = 5584
        STOCK_RNSC = 5585
        STOCK_RNST = 5586
        STOCK_RNVA = 5587
        STOCK_RNVAZ = 5588
        STOCK_RNWK = 5589
        STOCK_ROAM = 5590
        STOCK_ROCK = 5591
        STOCK_RODM = 5592
        STOCK_ROG = 5593
        STOCK_ROGS = 5594
        STOCK_ROIC = 5595
        STOCK_ROK = 5596
        STOCK_ROKA = 5597
        STOCK_ROKU = 5598
        STOCK_ROL = 5599
        STOCK_ROLL = 5600
        STOCK_ROP = 5601
        STOCK_RORE = 5602
        STOCK_ROSE = 5603
        STOCK_ROSEU = 5604
        STOCK_ROSEW = 5605
        STOCK_ROSG = 5606
        STOCK_ROST = 5607
        STOCK_ROUS = 5608
        STOCK_ROX = 5609
        STOCK_ROYT = 5610
        STOCK_RP = 5611
        STOCK_RPAI = 5612
        STOCK_RPAI_A__CL = 5613
        STOCK_RPAI_A = 5614
        STOCK_RPD = 5615
        STOCK_RPM = 5616
        STOCK_RPRX = 5617
        STOCK_RPT = 5618
        STOCK_RPT_D = 5619
        STOCK_RPXC = 5620
        STOCK_RQI = 5621
        STOCK_RRC = 5622
        STOCK_RRD = 5623
        STOCK_RRGB = 5624
        STOCK_RRR = 5625
        STOCK_RRTS = 5626
        STOCK_RS = 5627
        STOCK_RSG = 5628
        STOCK_RSLS = 5629
        STOCK_RSO = 5630
        STOCK_RSO_A = 5631
        STOCK_RSO_B = 5632
        STOCK_RSO_C = 5633
        STOCK_RSPP = 5634
        STOCK_RST = 5635
        STOCK_RSYS = 5636
        STOCK_RT = 5637
        STOCK_RTEC = 5638
        STOCK_RTIX = 5639
        STOCK_RTK = 5640
        STOCK_RTN = 5641
        STOCK_RTNB = 5642
        STOCK_RTRX = 5643
        STOCK_RTTR = 5644
        STOCK_RUBI = 5645
        STOCK_RUN = 5646
        STOCK_RUSHA = 5647
        STOCK_RUSHB = 5648
        STOCK_RUTH = 5649
        STOCK_RVEN = 5650
        STOCK_RVLT = 5651
        STOCK_RVNC = 5652
        STOCK_RVP = 5653
        STOCK_RVRS = 5654
        STOCK_RVSB = 5655
        STOCK_RVT = 5656
        STOCK_RWC = 5657
        STOCK_RWLK = 5658
        STOCK_RWT = 5659
        STOCK_RXDX = 5660
        STOCK_RXII = 5661
        STOCK_RXIIW = 5662
        STOCK_RXN = 5663
        STOCK_RXN_A = 5664
        STOCK_RY = 5665
        STOCK_RYAAY = 5666
        STOCK_RYAM = 5667
        STOCK_RYAM_A = 5668
        STOCK_RYB = 5669
        STOCK_RYI = 5670
        STOCK_RYN = 5671
        STOCK_RYTM = 5672
        STOCK_RY_S__CL = 5673
        STOCK_RY_T = 5674
        STOCK_RZA = 5675
        STOCK_RZB = 5676
        STOCK_S = 5677
        STOCK_SA = 5678
        STOCK_SAB = 5679
        STOCK_SABR = 5680
        STOCK_SACH = 5681
        STOCK_SAEX = 5682
        STOCK_SAFE = 5683
        STOCK_SAFM = 5684
        STOCK_SAFT = 5685
        STOCK_SAGE = 5686
        STOCK_SAH = 5687
        STOCK_SAIA = 5688
        STOCK_SAIC = 5689
        STOCK_SAIL = 5690
        STOCK_SAL = 5691
        STOCK_SALM = 5692
        STOCK_SALT = 5693
        STOCK_SAM = 5694
        STOCK_SAMG = 5695
        STOCK_SAN = 5696
        STOCK_SAND = 5697
        STOCK_SANM = 5698
        STOCK_SANW = 5699
        STOCK_SAN_A = 5700
        STOCK_SAN_B = 5701
        STOCK_SAN_C = 5702
        STOCK_SAN_I = 5703
        STOCK_SAP = 5704
        STOCK_SAR = 5705
        STOCK_SASR = 5706
        STOCK_SATS = 5707
        STOCK_SAUC = 5708
        STOCK_SAVE = 5709
        STOCK_SB = 5710
        STOCK_SBAC = 5711
        STOCK_SBBC = 5712
        STOCK_SBBP = 5713
        STOCK_SBBX = 5714
        STOCK_SBCF = 5715
        STOCK_SBCP = 5716
        STOCK_SBFG = 5717
        STOCK_SBFGP = 5718
        STOCK_SBGI = 5719
        STOCK_SBGL = 5720
        STOCK_SBH = 5721
        STOCK_SBI = 5722
        STOCK_SBLK = 5723
        STOCK_SBLKL = 5724
        STOCK_SBNA = 5725
        STOCK_SBNB = 5726
        STOCK_SBNY = 5727
        STOCK_SBNYW = 5728
        STOCK_SBOT = 5729
        STOCK_SBOW = 5730
        STOCK_SBPH = 5731
        STOCK_SBR = 5732
        STOCK_SBRA = 5733
        STOCK_SBRAP = 5734
        STOCK_SBS = 5735
        STOCK_SBSI = 5736
        STOCK_SBT = 5737
        STOCK_SBUX = 5738
        STOCK_SB_B = 5739
        STOCK_SB_C = 5740
        STOCK_SB_D = 5741
        STOCK_SC = 5742
        STOCK_SCA = 5743
        STOCK_SCAC = 5744
        STOCK_SCACU = 5745
        STOCK_SCACW = 5746
        STOCK_SCAP = 5747
        STOCK_SCCI = 5748
        STOCK_SCCO = 5749
        STOCK_SCD = 5750
        STOCK_SCE_B = 5751
        STOCK_SCE_C = 5752
        STOCK_SCE_D = 5753
        STOCK_SCE_E = 5754
        STOCK_SCE_G = 5755
        STOCK_SCE_H = 5756
        STOCK_SCE_J = 5757
        STOCK_SCE_K = 5758
        STOCK_SCE_L = 5759
        STOCK_SCG = 5760
        STOCK_SCHK = 5761
        STOCK_SCHL = 5762
        STOCK_SCHN = 5763
        STOCK_SCHW = 5764
        STOCK_SCHW_B__CL = 5765
        STOCK_SCHW_B = 5766
        STOCK_SCHW_C = 5767
        STOCK_SCHW_D = 5768
        STOCK_SCI = 5769
        STOCK_SCKT = 5770
        STOCK_SCL = 5771
        STOCK_SCLN = 5772
        STOCK_SCM = 5773
        STOCK_SCMP = 5774
        STOCK_SCON = 5775
        STOCK_SCPH = 5776
        STOCK_SCS = 5777
        STOCK_SCSC = 5778
        STOCK_SCVL = 5779
        STOCK_SCWX = 5780
        STOCK_SCX = 5781
        STOCK_SCYX = 5782
        STOCK_SD = 5783
        STOCK_SDLP = 5784
        STOCK_SDPI = 5785
        STOCK_SDR = 5786
        STOCK_SDRL = 5787
        STOCK_SDT = 5788
        STOCK_SDVY = 5789
        STOCK_SE = 5790
        STOCK_SEAC = 5791
        STOCK_SEAS = 5792
        STOCK_SEB = 5793
        STOCK_SECO = 5794
        STOCK_SECT = 5795
        STOCK_SEDG = 5796
        STOCK_SEE = 5797
        STOCK_SEED = 5798
        STOCK_SEIC = 5799
        STOCK_SELB = 5800
        STOCK_SELF = 5801
        STOCK_SEM = 5802
        STOCK_SEMG = 5803
        STOCK_SEND = 5804
        STOCK_SENEA = 5805
        STOCK_SENEB = 5806
        STOCK_SENS = 5807
        STOCK_SEP = 5808
        STOCK_SERV = 5809
        STOCK_SF = 5810
        STOCK_SFB = 5811
        STOCK_SFBC = 5812
        STOCK_SFBS = 5813
        STOCK_SFE = 5814
        STOCK_SFHY = 5815
        STOCK_SFIG = 5816
        STOCK_SFIX = 5817
        STOCK_SFL = 5818
        STOCK_SFLY = 5819
        STOCK_SFM = 5820
        STOCK_SFNC = 5821
        STOCK_SFR = 5822
        STOCK_SFS = 5823
        STOCK_SFST = 5824
        STOCK_SFUN = 5825
        STOCK_SF_A = 5826
        STOCK_SGA = 5827
        STOCK_SGB = 5828
        STOCK_SGBX = 5829
        STOCK_SGC = 5830
        STOCK_SGEN = 5831
        STOCK_SGF = 5832
        STOCK_SGH = 5833
        STOCK_SGLB = 5834
        STOCK_SGLBW = 5835
        STOCK_SGMA = 5836
        STOCK_SGMO = 5837
        STOCK_SGMS = 5838
        STOCK_SGOC = 5839
        STOCK_SGQI = 5840
        STOCK_SGRP = 5841
        STOCK_SGRY = 5842
        STOCK_SGU = 5843
        STOCK_SGY__WS = 5844
        STOCK_SGY = 5845
        STOCK_SGYP = 5846
        STOCK_SGZA = 5847
        STOCK_SHAG = 5848
        STOCK_SHAK = 5849
        STOCK_SHBI = 5850
        STOCK_SHE = 5851
        STOCK_SHEN = 5852
        STOCK_SHG = 5853
        STOCK_SHI = 5854
        STOCK_SHIP = 5855
        STOCK_SHIPW = 5856
        STOCK_SHLD = 5857
        STOCK_SHLDW = 5858
        STOCK_SHLM = 5859
        STOCK_SHLO = 5860
        STOCK_SHLX = 5861
        STOCK_SHNY = 5862
        STOCK_SHO = 5863
        STOCK_SHOO = 5864
        STOCK_SHOP = 5865
        STOCK_SHOS = 5866
        STOCK_SHO_E = 5867
        STOCK_SHO_F = 5868
        STOCK_SHPG = 5869
        STOCK_SHSP = 5870
        STOCK_SHW = 5871
        STOCK_SID = 5872
        STOCK_SIEB = 5873
        STOCK_SIEN = 5874
        STOCK_SIF = 5875
        STOCK_SIFI = 5876
        STOCK_SIFY = 5877
        STOCK_SIG = 5878
        STOCK_SIGI = 5879
        STOCK_SIGM = 5880
        STOCK_SILC = 5881
        STOCK_SIM = 5882
        STOCK_SIMO = 5883
        STOCK_SINA = 5884
        STOCK_SINO = 5885
        STOCK_SIR = 5886
        STOCK_SIRI = 5887
        STOCK_SITE = 5888
        STOCK_SITO = 5889
        STOCK_SIVB = 5890
        STOCK_SIVBO = 5891
        STOCK_SIX = 5892
        STOCK_SJI = 5893
        STOCK_SJM = 5894
        STOCK_SJR = 5895
        STOCK_SJT = 5896
        STOCK_SJW = 5897
        STOCK_SKIS = 5898
        STOCK_SKLN = 5899
        STOCK_SKM = 5900
        STOCK_SKT = 5901
        STOCK_SKX = 5902
        STOCK_SKY = 5903
        STOCK_SKYS = 5904
        STOCK_SKYW = 5905
        STOCK_SLAB = 5906
        STOCK_SLB = 5907
        STOCK_SLCA = 5908
        STOCK_SLCT = 5909
        STOCK_SLD = 5910
        STOCK_SLDA = 5911
        STOCK_SLF = 5912
        STOCK_SLG = 5913
        STOCK_SLGN = 5914
        STOCK_SLG_I = 5915
        STOCK_SLIM = 5916
        STOCK_SLM = 5917
        STOCK_SLMBP = 5918
        STOCK_SLNO = 5919
        STOCK_SLNOW = 5920
        STOCK_SLP = 5921
        STOCK_SLRA = 5922
        STOCK_SLRC = 5923
        STOCK_SLTB = 5924
        STOCK_SM = 5925
        STOCK_SMBC = 5926
        STOCK_SMBK = 5927
        STOCK_SMCI = 5928
        STOCK_SMCP = 5929
        STOCK_SMED = 5930
        STOCK_SMFG = 5931
        STOCK_SMG = 5932
        STOCK_SMHD = 5933
        STOCK_SMHI = 5934
        STOCK_SMI = 5935
        STOCK_SMIN = 5936
        STOCK_SMIT = 5937
        STOCK_SMLP = 5938
        STOCK_SMM = 5939
        STOCK_SMMD = 5940
        STOCK_SMMF = 5941
        STOCK_SMMT = 5942
        STOCK_SMMV = 5943
        STOCK_SMP = 5944
        STOCK_SMPL = 5945
        STOCK_SMPLW = 5946
        STOCK_SMRT = 5947
        STOCK_SMSI = 5948
        STOCK_SMTC = 5949
        STOCK_SMTS = 5950
        STOCK_SMTX = 5951
        STOCK_SN = 5952
        STOCK_SNA = 5953
        STOCK_SNAK = 5954
        STOCK_SNAP = 5955
        STOCK_SNBC = 5956
        STOCK_SNBR = 5957
        STOCK_SNC = 5958
        STOCK_SNCR = 5959
        STOCK_SND = 5960
        STOCK_SNDE = 5961
        STOCK_SNDR = 5962
        STOCK_SNDX = 5963
        STOCK_SNE = 5964
        STOCK_SNES = 5965
        STOCK_SNFCA = 5966
        STOCK_SNGX = 5967
        STOCK_SNGXW = 5968
        STOCK_SNH = 5969
        STOCK_SNHNI = 5970
        STOCK_SNHNL = 5971
        STOCK_SNHY = 5972
        STOCK_SNI = 5973
        STOCK_SNMP = 5974
        STOCK_SNMX = 5975
        STOCK_SNN = 5976
        STOCK_SNNA = 5977
        STOCK_SNOA = 5978
        STOCK_SNOAW = 5979
        STOCK_SNP = 5980
        STOCK_SNPS = 5981
        STOCK_SNR = 5982
        STOCK_SNSR = 5983
        STOCK_SNSS = 5984
        STOCK_SNV = 5985
        STOCK_SNV_C = 5986
        STOCK_SNX = 5987
        STOCK_SNY = 5988
        STOCK_SO = 5989
        STOCK_SODA = 5990
        STOCK_SOFO = 5991
        STOCK_SOGO = 5992
        STOCK_SOHO = 5993
        STOCK_SOHOB = 5994
        STOCK_SOHOM = 5995
        STOCK_SOHOO = 5996
        STOCK_SOHU = 5997
        STOCK_SOI = 5998
        STOCK_SOJA = 5999
        STOCK_SOJB = 6000
        STOCK_SOL = 6001
        STOCK_SON = 6002
        STOCK_SONA = 6003
        STOCK_SONC = 6004
        STOCK_SONS = 6005
        STOCK_SOR = 6006
        STOCK_SORL = 6007
        STOCK_SOVB = 6008
        STOCK_SOV_C = 6009
        STOCK_SP = 6010
        STOCK_SPA = 6011
        STOCK_SPAB = 6012
        STOCK_SPAR = 6013
        STOCK_SPB = 6014
        STOCK_SPCB = 6015
        STOCK_SPDN = 6016
        STOCK_SPDW = 6017
        STOCK_SPE = 6018
        STOCK_SPEM = 6019
        STOCK_SPEX = 6020
        STOCK_SPE_B = 6021
        STOCK_SPG = 6022
        STOCK_SPGI = 6023
        STOCK_SPG_J = 6024
        STOCK_SPH = 6025
        STOCK_SPHS = 6026
        STOCK_SPI = 6027
        STOCK_SPIB = 6028
        STOCK_SPIL = 6029
        STOCK_SPKE = 6030
        STOCK_SPKEP = 6031
        STOCK_SPLB = 6032
        STOCK_SPLG = 6033
        STOCK_SPLK = 6034
        STOCK_SPLP = 6035
        STOCK_SPLP_A = 6036
        STOCK_SPLP_T = 6037
        STOCK_SPMD = 6038
        STOCK_SPMO = 6039
        STOCK_SPMV = 6040
        STOCK_SPN = 6041
        STOCK_SPNE = 6042
        STOCK_SPNS = 6043
        STOCK_SPOK = 6044
        STOCK_SPPI = 6045
        STOCK_SPPP = 6046
        STOCK_SPR = 6047
        STOCK_SPRO = 6048
        STOCK_SPRT = 6049
        STOCK_SPSB = 6050
        STOCK_SPSC = 6051
        STOCK_SPSM = 6052
        STOCK_SPTL = 6053
        STOCK_SPTM = 6054
        STOCK_SPTN = 6055
        STOCK_SPTS = 6056
        STOCK_SPUN = 6057
        STOCK_SPVM = 6058
        STOCK_SPVU = 6059
        STOCK_SPWH = 6060
        STOCK_SPWR = 6061
        STOCK_SPXC = 6062
        STOCK_SPXE = 6063
        STOCK_SPXN = 6064
        STOCK_SPXT = 6065
        STOCK_SPXV = 6066
        STOCK_SPXX = 6067
        STOCK_SPYD = 6068
        STOCK_SPYX = 6069
        STOCK_SQ = 6070
        STOCK_SQBG = 6071
        STOCK_SQLV = 6072
        STOCK_SQM = 6073
        STOCK_SQNS = 6074
        STOCK_SQZZ = 6075
        STOCK_SR = 6076
        STOCK_SRAX = 6077
        STOCK_SRC = 6078
        STOCK_SRCE = 6079
        STOCK_SRCI = 6080
        STOCK_SRCL = 6081
        STOCK_SRCLP = 6082
        STOCK_SRC_A = 6083
        STOCK_SRDX = 6084
        STOCK_SRE = 6085
        STOCK_SREV = 6086
        STOCK_SRF = 6087
        STOCK_SRG = 6088
        STOCK_SRI = 6089
        STOCK_SRLP = 6090
        STOCK_SRNE = 6091
        STOCK_SRPT = 6092
        STOCK_SRRA = 6093
        STOCK_SRT = 6094
        STOCK_SRTS = 6095
        STOCK_SRTSW = 6096
        STOCK_SRUN = 6097
        STOCK_SRUNU = 6098
        STOCK_SRUNW = 6099
        STOCK_SRV = 6100
        STOCK_SRVA = 6101
        STOCK_SSB = 6102
        STOCK_SSBI = 6103
        STOCK_SSC = 6104
        STOCK_SSD = 6105
        STOCK_SSFN = 6106
        STOCK_SSI = 6107
        STOCK_SSKN = 6108
        STOCK_SSL = 6109
        STOCK_SSN = 6110
        STOCK_SSNC = 6111
        STOCK_SSNI = 6112
        STOCK_SSNT = 6113
        STOCK_SSP = 6114
        STOCK_SSRM = 6115
        STOCK_SSTI = 6116
        STOCK_SSTK = 6117
        STOCK_SSW = 6118
        STOCK_SSWA = 6119
        STOCK_SSWN = 6120
        STOCK_SSW_D = 6121
        STOCK_SSW_E = 6122
        STOCK_SSW_G = 6123
        STOCK_SSW_H = 6124
        STOCK_SSY = 6125
        STOCK_SSYS = 6126
        STOCK_ST = 6127
        STOCK_STAA = 6128
        STOCK_STAF = 6129
        STOCK_STAG = 6130
        STOCK_STAG_B = 6131
        STOCK_STAG_C = 6132
        STOCK_STAR = 6133
        STOCK_STAR_D = 6134
        STOCK_STAR_E = 6135
        STOCK_STAR_F = 6136
        STOCK_STAR_G = 6137
        STOCK_STAR_I = 6138
        STOCK_STAY = 6139
        STOCK_STB = 6140
        STOCK_STBA = 6141
        STOCK_STBZ = 6142
        STOCK_STC = 6143
        STOCK_STDY = 6144
        STOCK_STE = 6145
        STOCK_STFC = 6146
        STOCK_STI__WS__A = 6147
        STOCK_STI__WS__B = 6148
        STOCK_STI = 6149
        STOCK_STI_A = 6150
        STOCK_STI_E = 6151
        STOCK_STK = 6152
        STOCK_STKL = 6153
        STOCK_STKS = 6154
        STOCK_STL = 6155
        STOCK_STLD = 6156
        STOCK_STLR = 6157
        STOCK_STLRU = 6158
        STOCK_STLRW = 6159
        STOCK_STLY = 6160
        STOCK_STL_A = 6161
        STOCK_STM = 6162
        STOCK_STML = 6163
        STOCK_STMP = 6164
        STOCK_STN = 6165
        STOCK_STNG = 6166
        STOCK_STNL = 6167
        STOCK_STNLU = 6168
        STOCK_STO = 6169
        STOCK_STON = 6170
        STOCK_STOR = 6171
        STOCK_STOT = 6172
        STOCK_STPP = 6173
        STOCK_STRA = 6174
        STOCK_STRL = 6175
        STOCK_STRM = 6176
        STOCK_STRP = 6177
        STOCK_STRS = 6178
        STOCK_STRT = 6179
        STOCK_STT = 6180
        STOCK_STT_C = 6181
        STOCK_STT_D = 6182
        STOCK_STT_E = 6183
        STOCK_STT_G = 6184
        STOCK_STWD = 6185
        STOCK_STX = 6186
        STOCK_STZ__B = 6187
        STOCK_STZ = 6188
        STOCK_SU = 6189
        STOCK_SUI = 6190
        STOCK_SUI_A = 6191
        STOCK_SUM = 6192
        STOCK_SUMR = 6193
        STOCK_SUN = 6194
        STOCK_SUNS = 6195
        STOCK_SUNW = 6196
        STOCK_SUP = 6197
        STOCK_SUPN = 6198
        STOCK_SUPV = 6199
        STOCK_SUSA = 6200
        STOCK_SUSB = 6201
        STOCK_SUSC = 6202
        STOCK_SVA = 6203
        STOCK_SVBI = 6204
        STOCK_SVM = 6205
        STOCK_SVRA = 6206
        STOCK_SVT = 6207
        STOCK_SVU = 6208
        STOCK_SVVC = 6209
        STOCK_SWCH = 6210
        STOCK_SWIN = 6211
        STOCK_SWIR = 6212
        STOCK_SWJ = 6213
        STOCK_SWK = 6214
        STOCK_SWKS = 6215
        STOCK_SWM = 6216
        STOCK_SWN = 6217
        STOCK_SWNC = 6218
        STOCK_SWP = 6219
        STOCK_SWX = 6220
        STOCK_SWZ = 6221
        STOCK_SXC = 6222
        STOCK_SXCP = 6223
        STOCK_SXE = 6224
        STOCK_SXI = 6225
        STOCK_SXT = 6226
        STOCK_SYBT = 6227
        STOCK_SYBX = 6228
        STOCK_SYF = 6229
        STOCK_SYK = 6230
        STOCK_SYKE = 6231
        STOCK_SYMC = 6232
        STOCK_SYMX = 6233
        STOCK_SYN = 6234
        STOCK_SYNA = 6235
        STOCK_SYNC = 6236
        STOCK_SYNL = 6237
        STOCK_SYNT = 6238
        STOCK_SYPR = 6239
        STOCK_SYRS = 6240
        STOCK_SYT = 6241
        STOCK_SYX = 6242
        STOCK_SYY = 6243
        STOCK_SZC = 6244
        STOCK_T = 6245
        STOCK_TA = 6246
        STOCK_TAC = 6247
        STOCK_TACO = 6248
        STOCK_TACOW = 6249
        STOCK_TACT = 6250
        STOCK_TAHO = 6251
        STOCK_TAIL = 6252
        STOCK_TAIT = 6253
        STOCK_TAL = 6254
        STOCK_TANH = 6255
        STOCK_TANNI = 6256
        STOCK_TANNL = 6257
        STOCK_TANNZ = 6258
        STOCK_TAP__A = 6259
        STOCK_TAP = 6260
        STOCK_TAPR = 6261
        STOCK_TARO = 6262
        STOCK_TAST = 6263
        STOCK_TAT = 6264
        STOCK_TATT = 6265
        STOCK_TAX = 6266
        STOCK_TAXR = 6267
        STOCK_TAYD = 6268
        STOCK_TBB = 6269
        STOCK_TBBK = 6270
        STOCK_TBI = 6271
        STOCK_TBK = 6272
        STOCK_TBLU = 6273
        STOCK_TBNK = 6274
        STOCK_TBPH = 6275
        STOCK_TCAP = 6276
        STOCK_TCBI = 6277
        STOCK_TCBIL = 6278
        STOCK_TCBIP = 6279
        STOCK_TCBIW = 6280
        STOCK_TCBK = 6281
        STOCK_TCCA = 6282
        STOCK_TCCB = 6283
        STOCK_TCCO = 6284
        STOCK_TCF__WS = 6285
        STOCK_TCF = 6286
        STOCK_TCFC = 6287
        STOCK_TCF_B__CL = 6288
        STOCK_TCF_C = 6289
        STOCK_TCF_D = 6290
        STOCK_TCGP = 6291
        STOCK_TCHF = 6292
        STOCK_TCI = 6293
        STOCK_TCMD = 6294
        STOCK_TCO = 6295
        STOCK_TCON = 6296
        STOCK_TCO_J = 6297
        STOCK_TCO_K = 6298
        STOCK_TCP = 6299
        STOCK_TCPC = 6300
        STOCK_TCRD = 6301
        STOCK_TCRX = 6302
        STOCK_TCRZ = 6303
        STOCK_TCS = 6304
        STOCK_TCTL = 6305
        STOCK_TCX = 6306
        STOCK_TD = 6307
        STOCK_TDA = 6308
        STOCK_TDC = 6309
        STOCK_TDE = 6310
        STOCK_TDF = 6311
        STOCK_TDG = 6312
        STOCK_TDI = 6313
        STOCK_TDJ = 6314
        STOCK_TDOC = 6315
        STOCK_TDS = 6316
        STOCK_TDW__WS__A = 6317
        STOCK_TDW__WS__B = 6318
        STOCK_TDW = 6319
        STOCK_TDY = 6320
        STOCK_TEAM = 6321
        STOCK_TEAR = 6322
        STOCK_TECD = 6323
        STOCK_TECH = 6324
        STOCK_TECK = 6325
        STOCK_TEDU = 6326
        STOCK_TEF = 6327
        STOCK_TEGP = 6328
        STOCK_TEI = 6329
        STOCK_TEL = 6330
        STOCK_TELL = 6331
        STOCK_TEN = 6332
        STOCK_TENX = 6333
        STOCK_TEO = 6334
        STOCK_TEP = 6335
        STOCK_TER = 6336
        STOCK_TERM = 6337
        STOCK_TERP = 6338
        STOCK_TESO = 6339
        STOCK_TESS = 6340
        STOCK_TETF = 6341
        STOCK_TEUM = 6342
        STOCK_TEVA = 6343
        STOCK_TEX = 6344
        STOCK_TFSL = 6345
        STOCK_TFX = 6346
        STOCK_TG = 6347
        STOCK_TGA = 6348
        STOCK_TGB = 6349
        STOCK_TGC = 6350
        STOCK_TGEN = 6351
        STOCK_TGH = 6352
        STOCK_TGI = 6353
        STOCK_TGLS = 6354
        STOCK_TGNA = 6355
        STOCK_TGP = 6356
        STOCK_TGP_A = 6357
        STOCK_TGP_B = 6358
        STOCK_TGS = 6359
        STOCK_TGT = 6360
        STOCK_TGTX = 6361
        STOCK_THC = 6362
        STOCK_THFF = 6363
        STOCK_THG = 6364
        STOCK_THGA = 6365
        STOCK_THM = 6366
        STOCK_THO = 6367
        STOCK_THQ = 6368
        STOCK_THR = 6369
        STOCK_THRM = 6370
        STOCK_THS = 6371
        STOCK_THST = 6372
        STOCK_THW = 6373
        STOCK_TI__A = 6374
        STOCK_TI = 6375
        STOCK_TICC = 6376
        STOCK_TICCL = 6377
        STOCK_TIER = 6378
        STOCK_TIF = 6379
        STOCK_TIG = 6380
        STOCK_TIK = 6381
        STOCK_TIL = 6382
        STOCK_TILE = 6383
        STOCK_TIME = 6384
        STOCK_TIPT = 6385
        STOCK_TIS = 6386
        STOCK_TISA = 6387
        STOCK_TISI = 6388
        STOCK_TITN = 6389
        STOCK_TIVO = 6390
        STOCK_TJX = 6391
        STOCK_TK = 6392
        STOCK_TKAT = 6393
        STOCK_TKC = 6394
        STOCK_TKF = 6395
        STOCK_TKR = 6396
        STOCK_TLDH = 6397
        STOCK_TLEH = 6398
        STOCK_TLF = 6399
        STOCK_TLGT = 6400
        STOCK_TLI = 6401
        STOCK_TLK = 6402
        STOCK_TLND = 6403
        STOCK_TLP = 6404
        STOCK_TLRA = 6405
        STOCK_TLRD = 6406
        STOCK_TLYS = 6407
        STOCK_TM = 6408
        STOCK_TMHC = 6409
        STOCK_TMK = 6410
        STOCK_TMK_B = 6411
        STOCK_TMK_C = 6412
        STOCK_TMO = 6413
        STOCK_TMP = 6414
        STOCK_TMQ = 6415
        STOCK_TMST = 6416
        STOCK_TMUS = 6417
        STOCK_TMUSP = 6418
        STOCK_TNAV = 6419
        STOCK_TNC = 6420
        STOCK_TNDM = 6421
        STOCK_TNET = 6422
        STOCK_TNH = 6423
        STOCK_TNK = 6424
        STOCK_TNP = 6425
        STOCK_TNP_B = 6426
        STOCK_TNP_C = 6427
        STOCK_TNP_D = 6428
        STOCK_TNP_E = 6429
        STOCK_TNTR = 6430
        STOCK_TNXP = 6431
        STOCK_TOCA = 6432
        STOCK_TOL = 6433
        STOCK_TOO = 6434
        STOCK_TOO_A = 6435
        STOCK_TOO_B = 6436
        STOCK_TOPS = 6437
        STOCK_TORM = 6438
        STOCK_TOT = 6439
        STOCK_TOUR = 6440
        STOCK_TOWN = 6441
        STOCK_TOWR = 6442
        STOCK_TPB = 6443
        STOCK_TPC = 6444
        STOCK_TPGE__U = 6445
        STOCK_TPGE__WS = 6446
        STOCK_TPGE = 6447
        STOCK_TPGH__U = 6448
        STOCK_TPGH__WS = 6449
        STOCK_TPGH = 6450
        STOCK_TPH = 6451
        STOCK_TPHS = 6452
        STOCK_TPIC = 6453
        STOCK_TPIV = 6454
        STOCK_TPL = 6455
        STOCK_TPOR = 6456
        STOCK_TPR = 6457
        STOCK_TPRE = 6458
        STOCK_TPVG = 6459
        STOCK_TPVY = 6460
        STOCK_TPX = 6461
        STOCK_TPYP = 6462
        STOCK_TPZ = 6463
        STOCK_TR = 6464
        STOCK_TRC = 6465
        STOCK_TRCB = 6466
        STOCK_TRCH = 6467
        STOCK_TRCO = 6468
        STOCK_TRCR = 6469
        STOCK_TRCRW = 6470
        STOCK_TREC = 6471
        STOCK_TREE = 6472
        STOCK_TREX = 6473
        STOCK_TRGP = 6474
        STOCK_TRHC = 6475
        STOCK_TRI = 6476
        STOCK_TRIB = 6477
        STOCK_TRIL = 6478
        STOCK_TRIP = 6479
        STOCK_TRK = 6480
        STOCK_TRMB = 6481
        STOCK_TRMK = 6482
        STOCK_TRMT = 6483
        STOCK_TRN = 6484
        STOCK_TRNC = 6485
        STOCK_TRNO = 6486
        STOCK_TRNS = 6487
        STOCK_TROV = 6488
        STOCK_TROW = 6489
        STOCK_TROX = 6490
        STOCK_TRP = 6491
        STOCK_TRPX = 6492
        STOCK_TRQ = 6493
        STOCK_TRS = 6494
        STOCK_TRST = 6495
        STOCK_TRT = 6496
        STOCK_TRTN = 6497
        STOCK_TRTX = 6498
        STOCK_TRU = 6499
        STOCK_TRUE = 6500
        STOCK_TRUP = 6501
        STOCK_TRV = 6502
        STOCK_TRVG = 6503
        STOCK_TRVN = 6504
        STOCK_TRX = 6505
        STOCK_TRXC = 6506
        STOCK_TS = 6507
        STOCK_TSBK = 6508
        STOCK_TSC = 6509
        STOCK_TSCO = 6510
        STOCK_TSE = 6511
        STOCK_TSEM = 6512
        STOCK_TSG = 6513
        STOCK_TSI = 6514
        STOCK_TSLA = 6515
        STOCK_TSLF = 6516
        STOCK_TSLX = 6517
        STOCK_TSM = 6518
        STOCK_TSN = 6519
        STOCK_TSQ = 6520
        STOCK_TSRI = 6521
        STOCK_TSRO = 6522
        STOCK_TSS = 6523
        STOCK_TST = 6524
        STOCK_TSU = 6525
        STOCK_TTAC = 6526
        STOCK_TTAI = 6527
        STOCK_TTC = 6528
        STOCK_TTD = 6529
        STOCK_TTEC = 6530
        STOCK_TTEK = 6531
        STOCK_TTF = 6532
        STOCK_TTGT = 6533
        STOCK_TTI = 6534
        STOCK_TTM = 6535
        STOCK_TTMI = 6536
        STOCK_TTNP = 6537
        STOCK_TTOO = 6538
        STOCK_TTP = 6539
        STOCK_TTPH = 6540
        STOCK_TTS = 6541
        STOCK_TTWO = 6542
        STOCK_TU = 6543
        STOCK_TUES = 6544
        STOCK_TUP = 6545
        STOCK_TURN = 6546
        STOCK_TUSK = 6547
        STOCK_TV = 6548
        STOCK_TVC = 6549
        STOCK_TVE = 6550
        STOCK_TVPT = 6551
        STOCK_TVTY = 6552
        STOCK_TWI = 6553
        STOCK_TWIN = 6554
        STOCK_TWLO = 6555
        STOCK_TWMC = 6556
        STOCK_TWN = 6557
        STOCK_TWNK = 6558
        STOCK_TWNKW = 6559
        STOCK_TWO = 6560
        STOCK_TWOU = 6561
        STOCK_TWOW = 6562
        STOCK_TWO_A = 6563
        STOCK_TWO_B = 6564
        STOCK_TWTR = 6565
        STOCK_TWX = 6566
        STOCK_TX = 6567
        STOCK_TXMD = 6568
        STOCK_TXN = 6569
        STOCK_TXRH = 6570
        STOCK_TXT = 6571
        STOCK_TY = 6572
        STOCK_TYG = 6573
        STOCK_TYHT = 6574
        STOCK_TYL = 6575
        STOCK_TYME = 6576
        STOCK_TYPE = 6577
        STOCK_TY_ = 6578
        STOCK_TZOO = 6579
        STOCK_UA = 6580
        STOCK_UAA = 6581
        STOCK_UAL = 6582
        STOCK_UAMY = 6583
        STOCK_UAN = 6584
        STOCK_UBA = 6585
        STOCK_UBCP = 6586
        STOCK_UBFO = 6587
        STOCK_UBIO = 6588
        STOCK_UBNK = 6589
        STOCK_UBNT = 6590
        STOCK_UBOH = 6591
        STOCK_UBP = 6592
        STOCK_UBP_F__CL = 6593
        STOCK_UBP_G = 6594
        STOCK_UBP_H = 6595
        STOCK_UBRT = 6596
        STOCK_UBS = 6597
        STOCK_UBSH = 6598
        STOCK_UBSI = 6599
        STOCK_UCBA = 6600
        STOCK_UCBI = 6601
        STOCK_UCFC = 6602
        STOCK_UCTT = 6603
        STOCK_UDBI = 6604
        STOCK_UDR = 6605
        STOCK_UE = 6606
        STOCK_UEC = 6607
        STOCK_UEIC = 6608
        STOCK_UEPS = 6609
        STOCK_UEVM = 6610
        STOCK_UFAB = 6611
        STOCK_UFCS = 6612
        STOCK_UFI = 6613
        STOCK_UFPI = 6614
        STOCK_UFPT = 6615
        STOCK_UFS = 6616
        STOCK_UG = 6617
        STOCK_UGI = 6618
        STOCK_UGP = 6619
        STOCK_UHAL = 6620
        STOCK_UHS = 6621
        STOCK_UHT = 6622
        STOCK_UIHC = 6623
        STOCK_UIS = 6624
        STOCK_UITB = 6625
        STOCK_UIVM = 6626
        STOCK_UL = 6627
        STOCK_ULBI = 6628
        STOCK_ULH = 6629
        STOCK_ULTA = 6630
        STOCK_ULTI = 6631
        STOCK_ULVM = 6632
        STOCK_UMBF = 6633
        STOCK_UMC = 6634
        STOCK_UMH = 6635
        STOCK_UMH_B = 6636
        STOCK_UMH_C = 6637
        STOCK_UMPQ = 6638
        STOCK_UN = 6639
        STOCK_UNAM = 6640
        STOCK_UNB = 6641
        STOCK_UNF = 6642
        STOCK_UNFI = 6643
        STOCK_UNH = 6644
        STOCK_UNIT = 6645
        STOCK_UNM = 6646
        STOCK_UNP = 6647
        STOCK_UNT = 6648
        STOCK_UNTY = 6649
        STOCK_UNVR = 6650
        STOCK_UONE = 6651
        STOCK_UONEK = 6652
        STOCK_UPL = 6653
        STOCK_UPLD = 6654
        STOCK_UPS = 6655
        STOCK_UQM = 6656
        STOCK_URBN = 6657
        STOCK_URG = 6658
        STOCK_URGN = 6659
        STOCK_URI = 6660
        STOCK_USA = 6661
        STOCK_USAC = 6662
        STOCK_USAK = 6663
        STOCK_USAP = 6664
        STOCK_USAS = 6665
        STOCK_USAT = 6666
        STOCK_USATP = 6667
        STOCK_USAU = 6668
        STOCK_USB = 6669
        STOCK_USB_A = 6670
        STOCK_USB_H = 6671
        STOCK_USB_M = 6672
        STOCK_USB_O = 6673
        STOCK_USCR = 6674
        STOCK_USDP = 6675
        STOCK_USEG = 6676
        STOCK_USEQ = 6677
        STOCK_USFD = 6678
        STOCK_USG = 6679
        STOCK_USHY = 6680
        STOCK_USLB = 6681
        STOCK_USLM = 6682
        STOCK_USM = 6683
        STOCK_USMC = 6684
        STOCK_USMF = 6685
        STOCK_USNA = 6686
        STOCK_USOD = 6687
        STOCK_USOI = 6688
        STOCK_USOU = 6689
        STOCK_USPH = 6690
        STOCK_USRT = 6691
        STOCK_USTB = 6692
        STOCK_USVM = 6693
        STOCK_UTES = 6694
        STOCK_UTF = 6695
        STOCK_UTG = 6696
        STOCK_UTHR = 6697
        STOCK_UTI = 6698
        STOCK_UTL = 6699
        STOCK_UTLF = 6700
        STOCK_UTMD = 6701
        STOCK_UTSI = 6702
        STOCK_UTSL = 6703
        STOCK_UTX = 6704
        STOCK_UUU = 6705
        STOCK_UUUU__WS = 6706
        STOCK_UUUU = 6707
        STOCK_UVE = 6708
        STOCK_UVSP = 6709
        STOCK_UVV = 6710
        STOCK_UWN = 6711
        STOCK_UWT = 6712
        STOCK_UZA = 6713
        STOCK_UZB = 6714
        STOCK_UZC = 6715
        STOCK_V = 6716
        STOCK_VAC = 6717
        STOCK_VALE__P = 6718
        STOCK_VALE = 6719
        STOCK_VALU = 6720
        STOCK_VALX = 6721
        STOCK_VAMO = 6722
        STOCK_VAR = 6723
        STOCK_VBF = 6724
        STOCK_VBFC = 6725
        STOCK_VBIV = 6726
        STOCK_VBLT = 6727
        STOCK_VBND = 6728
        STOCK_VBTX = 6729
        STOCK_VC = 6730
        STOCK_VCEL = 6731
        STOCK_VCF = 6732
        STOCK_VCO = 6733
        STOCK_VCRA = 6734
        STOCK_VCV = 6735
        STOCK_VCYT = 6736
        STOCK_VDSI = 6737
        STOCK_VDTH = 6738
        STOCK_VEAC = 6739
        STOCK_VEACU = 6740
        STOCK_VEACW = 6741
        STOCK_VEC = 6742
        STOCK_VECO = 6743
        STOCK_VEDL = 6744
        STOCK_VEEV = 6745
        STOCK_VEON = 6746
        STOCK_VER = 6747
        STOCK_VERI = 6748
        STOCK_VERU = 6749
        STOCK_VER_F = 6750
        STOCK_VESH = 6751
        STOCK_VET = 6752
        STOCK_VFC = 6753
        STOCK_VFL = 6754
        STOCK_VG = 6755
        STOCK_VGFO = 6756
        STOCK_VGI = 6757
        STOCK_VGM = 6758
        STOCK_VGR = 6759
        STOCK_VGZ = 6760
        STOCK_VHC = 6761
        STOCK_VHI = 6762
        STOCK_VIA = 6763
        STOCK_VIAB = 6764
        STOCK_VIAV = 6765
        STOCK_VICL = 6766
        STOCK_VICR = 6767
        STOCK_VIGI = 6768
        STOCK_VII = 6769
        STOCK_VIPS = 6770
        STOCK_VIRC = 6771
        STOCK_VIRT = 6772
        STOCK_VISI = 6773
        STOCK_VIST = 6774
        STOCK_VIV = 6775
        STOCK_VIVE = 6776
        STOCK_VIVO = 6777
        STOCK_VJET = 6778
        STOCK_VKI = 6779
        STOCK_VKQ = 6780
        STOCK_VKTX = 6781
        STOCK_VKTXW = 6782
        STOCK_VLGEA = 6783
        STOCK_VLO = 6784
        STOCK_VLP = 6785
        STOCK_VLRS = 6786
        STOCK_VLRX = 6787
        STOCK_VLT = 6788
        STOCK_VLY__WS = 6789
        STOCK_VLY = 6790
        STOCK_VLY_A = 6791
        STOCK_VLY_B = 6792
        STOCK_VMAX = 6793
        STOCK_VMC = 6794
        STOCK_VMET = 6795
        STOCK_VMI = 6796
        STOCK_VMIN = 6797
        STOCK_VMM = 6798
        STOCK_VMO = 6799
        STOCK_VMOT = 6800
        STOCK_VMW = 6801
        STOCK_VNCE = 6802
        STOCK_VNDA = 6803
        STOCK_VNET = 6804
        STOCK_VNLA = 6805
        STOCK_VNO = 6806
        STOCK_VNOM = 6807
        STOCK_VNO_G = 6808
        STOCK_VNO_I = 6809
        STOCK_VNO_K = 6810
        STOCK_VNO_L = 6811
        STOCK_VNRX = 6812
        STOCK_VNTR = 6813
        STOCK_VNTV = 6814
        STOCK_VOC = 6815
        STOCK_VOD = 6816
        STOCK_VOXX = 6817
        STOCK_VOYA = 6818
        STOCK_VPG = 6819
        STOCK_VPV = 6820
        STOCK_VR = 6821
        STOCK_VRA = 6822
        STOCK_VRAY = 6823
        STOCK_VREX = 6824
        STOCK_VRIG = 6825
        STOCK_VRML = 6826
        STOCK_VRNA = 6827
        STOCK_VRNS = 6828
        STOCK_VRNT = 6829
        STOCK_VRS = 6830
        STOCK_VRSK = 6831
        STOCK_VRSN = 6832
        STOCK_VRTS = 6833
        STOCK_VRTSP = 6834
        STOCK_VRTU = 6835
        STOCK_VRTV = 6836
        STOCK_VRTX = 6837
        STOCK_VRX = 6838
        STOCK_VR_A = 6839
        STOCK_VR_B = 6840
        STOCK_VSAR = 6841
        STOCK_VSAT = 6842
        STOCK_VSDA = 6843
        STOCK_VSEC = 6844
        STOCK_VSH = 6845
        STOCK_VSI = 6846
        STOCK_VSLR = 6847
        STOCK_VSM = 6848
        STOCK_VSMV = 6849
        STOCK_VST = 6850
        STOCK_VSTM = 6851
        STOCK_VSTO = 6852
        STOCK_VTA = 6853
        STOCK_VTC = 6854
        STOCK_VTEB = 6855
        STOCK_VTGN = 6856
        STOCK_VTL = 6857
        STOCK_VTN = 6858
        STOCK_VTNR = 6859
        STOCK_VTR = 6860
        STOCK_VTRB = 6861
        STOCK_VTVT = 6862
        STOCK_VUZI = 6863
        STOCK_VVC = 6864
        STOCK_VVI = 6865
        STOCK_VVPR = 6866
        STOCK_VVR = 6867
        STOCK_VVUS = 6868
        STOCK_VVV = 6869
        STOCK_VWR = 6870
        STOCK_VYGR = 6871
        STOCK_VYMI = 6872
        STOCK_VZ = 6873
        STOCK_VZA = 6874
        STOCK_W = 6875
        STOCK_WAAS = 6876
        STOCK_WAB = 6877
        STOCK_WABC = 6878
        STOCK_WAC = 6879
        STOCK_WAFD = 6880
        STOCK_WAFDW = 6881
        STOCK_WAGE = 6882
        STOCK_WAIR = 6883
        STOCK_WAL = 6884
        STOCK_WALA = 6885
        STOCK_WASH = 6886
        STOCK_WAT = 6887
        STOCK_WATT = 6888
        STOCK_WAYN = 6889
        STOCK_WB = 6890
        STOCK_WBA = 6891
        STOCK_WBAI = 6892
        STOCK_WBBW = 6893
        STOCK_WBC = 6894
        STOCK_WBIA = 6895
        STOCK_WBIB = 6896
        STOCK_WBIC = 6897
        STOCK_WBID = 6898
        STOCK_WBIE = 6899
        STOCK_WBIF = 6900
        STOCK_WBIG = 6901
        STOCK_WBIH = 6902
        STOCK_WBII = 6903
        STOCK_WBIL = 6904
        STOCK_WBIR = 6905
        STOCK_WBIY = 6906
        STOCK_WBK = 6907
        STOCK_WBKC = 6908
        STOCK_WBS = 6909
        STOCK_WBS_E = 6910
        STOCK_WBT = 6911
        STOCK_WCC = 6912
        STOCK_WCFB = 6913
        STOCK_WCG = 6914
        STOCK_WCN = 6915
        STOCK_WD = 6916
        STOCK_WDAY = 6917
        STOCK_WDC = 6918
        STOCK_WDFC = 6919
        STOCK_WDR = 6920
        STOCK_WDRW = 6921
        STOCK_WEA = 6922
        STOCK_WEAR = 6923
        STOCK_WEB = 6924
        STOCK_WEBK = 6925
        STOCK_WEC = 6926
        STOCK_WEN = 6927
        STOCK_WERN = 6928
        STOCK_WES = 6929
        STOCK_WETF = 6930
        STOCK_WEX = 6931
        STOCK_WEXP = 6932
        STOCK_WEYS = 6933
        STOCK_WF = 6934
        STOCK_WFBI = 6935
        STOCK_WFC__WS = 6936
        STOCK_WFC = 6937
        STOCK_WFC_J = 6938
        STOCK_WFC_L = 6939
        STOCK_WFC_N = 6940
        STOCK_WFC_O = 6941
        STOCK_WFC_P = 6942
        STOCK_WFC_Q = 6943
        STOCK_WFC_R = 6944
        STOCK_WFC_T = 6945
        STOCK_WFC_V = 6946
        STOCK_WFC_W = 6947
        STOCK_WFC_X = 6948
        STOCK_WFC_Y = 6949
        STOCK_WFE_A = 6950
        STOCK_WFHY = 6951
        STOCK_WFIG = 6952
        STOCK_WFT = 6953
        STOCK_WG = 6954
        STOCK_WGL = 6955
        STOCK_WGO = 6956
        STOCK_WGP = 6957
        STOCK_WHF = 6958
        STOCK_WHFBL = 6959
        STOCK_WHG = 6960
        STOCK_WHLM = 6961
        STOCK_WHLR = 6962
        STOCK_WHLRD = 6963
        STOCK_WHLRP = 6964
        STOCK_WHLRW = 6965
        STOCK_WHR = 6966
        STOCK_WIA = 6967
        STOCK_WIFI = 6968
        STOCK_WILC = 6969
        STOCK_WIN = 6970
        STOCK_WINA = 6971
        STOCK_WING = 6972
        STOCK_WINS = 6973
        STOCK_WIRE = 6974
        STOCK_WIT = 6975
        STOCK_WIW = 6976
        STOCK_WIX = 6977
        STOCK_WK = 6978
        STOCK_WKHS = 6979
        STOCK_WLB = 6980
        STOCK_WLDN = 6981
        STOCK_WLFC = 6982
        STOCK_WLH = 6983
        STOCK_WLK = 6984
        STOCK_WLKP = 6985
        STOCK_WLL = 6986
        STOCK_WLTW = 6987
        STOCK_WM = 6988
        STOCK_WMB = 6989
        STOCK_WMC = 6990
        STOCK_WMGI = 6991
        STOCK_WMGIZ = 6992
        STOCK_WMIH = 6993
        STOCK_WMK = 6994
        STOCK_WMLP = 6995
        STOCK_WMS = 6996
        STOCK_WMT = 6997
        STOCK_WNC = 6998
        STOCK_WNEB = 6999
        STOCK_WNFM = 7000
        STOCK_WNRL = 7001
        STOCK_WNS = 7002
        STOCK_WOR = 7003
        STOCK_WOW = 7004
        STOCK_WPC = 7005
        STOCK_WPCS = 7006
        STOCK_WPG = 7007
        STOCK_WPG_H = 7008
        STOCK_WPG_I = 7009
        STOCK_WPM = 7010
        STOCK_WPPGY = 7011
        STOCK_WPRT = 7012
        STOCK_WPX = 7013
        STOCK_WPXP = 7014
        STOCK_WPZ = 7015
        STOCK_WR = 7016
        STOCK_WRB = 7017
        STOCK_WRB_B = 7018
        STOCK_WRB_C = 7019
        STOCK_WRB_D = 7020
        STOCK_WRD = 7021
        STOCK_WRE = 7022
        STOCK_WRI = 7023
        STOCK_WRK = 7024
        STOCK_WRLD = 7025
        STOCK_WRLS = 7026
        STOCK_WRLSR = 7027
        STOCK_WRLSU = 7028
        STOCK_WRLSW = 7029
        STOCK_WRN = 7030
        STOCK_WSBC = 7031
        STOCK_WSBF = 7032
        STOCK_WSCI = 7033
        STOCK_WSFS = 7034
        STOCK_WSKY = 7035
        STOCK_WSM = 7036
        STOCK_WSO__B = 7037
        STOCK_WSO = 7038
        STOCK_WSPT = 7039
        STOCK_WSR = 7040
        STOCK_WST = 7041
        STOCK_WSTG = 7042
        STOCK_WSTL = 7043
        STOCK_WTBA = 7044
        STOCK_WTFC = 7045
        STOCK_WTFCM = 7046
        STOCK_WTFCW = 7047
        STOCK_WTI = 7048
        STOCK_WTID = 7049
        STOCK_WTIU = 7050
        STOCK_WTM = 7051
        STOCK_WTR = 7052
        STOCK_WTRX = 7053
        STOCK_WTS = 7054
        STOCK_WTT = 7055
        STOCK_WTTR = 7056
        STOCK_WTW = 7057
        STOCK_WU = 7058
        STOCK_WUBA = 7059
        STOCK_WUSA = 7060
        STOCK_WVE = 7061
        STOCK_WVFC = 7062
        STOCK_WVVI = 7063
        STOCK_WVVIP = 7064
        STOCK_WWD = 7065
        STOCK_WWE = 7066
        STOCK_WWR = 7067
        STOCK_WWW = 7068
        STOCK_WY = 7069
        STOCK_WYDE = 7070
        STOCK_WYIG = 7071
        STOCK_WYIGU = 7072
        STOCK_WYIGW = 7073
        STOCK_WYN = 7074
        STOCK_WYNN = 7075
        STOCK_WYY = 7076
        STOCK_X = 7077
        STOCK_XBIO = 7078
        STOCK_XBIT = 7079
        STOCK_XBKS = 7080
        STOCK_XCEM = 7081
        STOCK_XCO = 7082
        STOCK_XCRA = 7083
        STOCK_XEC = 7084
        STOCK_XEL = 7085
        STOCK_XELA = 7086
        STOCK_XELB = 7087
        STOCK_XENE = 7088
        STOCK_XENT = 7089
        STOCK_XFLT = 7090
        STOCK_XGTI = 7091
        STOCK_XGTIW = 7092
        STOCK_XHR = 7093
        STOCK_XIN = 7094
        STOCK_XINA = 7095
        STOCK_XITK = 7096
        STOCK_XIVH = 7097
        STOCK_XL = 7098
        STOCK_XLNX = 7099
        STOCK_XLRE = 7100
        STOCK_XLRN = 7101
        STOCK_XMX = 7102
        STOCK_XNCR = 7103
        STOCK_XNET = 7104
        STOCK_XNTK = 7105
        STOCK_XNY = 7106
        STOCK_XOG = 7107
        STOCK_XOM = 7108
        STOCK_XOMA = 7109
        STOCK_XON = 7110
        STOCK_XONE = 7111
        STOCK_XOXO = 7112
        STOCK_XPER = 7113
        STOCK_XPL = 7114
        STOCK_XPLR = 7115
        STOCK_XPO = 7116
        STOCK_XRAY = 7117
        STOCK_XRF = 7118
        STOCK_XRM = 7119
        STOCK_XRX = 7120
        STOCK_XSHD = 7121
        STOCK_XSHQ = 7122
        STOCK_XTH = 7123
        STOCK_XTLB = 7124
        STOCK_XTNT = 7125
        STOCK_XUSA = 7126
        STOCK_XWEB = 7127
        STOCK_XXII = 7128
        STOCK_XYL = 7129
        STOCK_Y = 7130
        STOCK_YECO = 7131
        STOCK_YELP = 7132
        STOCK_YERR = 7133
        STOCK_YESR = 7134
        STOCK_YEXT = 7135
        STOCK_YGE = 7136
        STOCK_YGYI = 7137
        STOCK_YIN = 7138
        STOCK_YLD = 7139
        STOCK_YLDE = 7140
        STOCK_YNDX = 7141
        STOCK_YOGA = 7142
        STOCK_YORW = 7143
        STOCK_YPF = 7144
        STOCK_YRCW = 7145
        STOCK_YRD = 7146
        STOCK_YTEN = 7147
        STOCK_YTRA = 7148
        STOCK_YUM = 7149
        STOCK_YUMA = 7150
        STOCK_YUMC = 7151
        STOCK_YUME = 7152
        STOCK_YY = 7153
        STOCK_Z = 7154
        STOCK_ZAGG = 7155
        STOCK_ZAIS = 7156
        STOCK_ZAYO = 7157
        STOCK_ZBH = 7158
        STOCK_ZBIO = 7159
        STOCK_ZBK = 7160
        STOCK_ZBRA = 7161
        STOCK_ZBZX = 7162
        STOCK_ZB_A = 7163
        STOCK_ZB_G = 7164
        STOCK_ZB_H = 7165
        STOCK_ZDGE = 7166
        STOCK_ZEAL = 7167
        STOCK_ZEN = 7168
        STOCK_ZEUS = 7169
        STOCK_ZF = 7170
        STOCK_ZFGN = 7171
        STOCK_ZG = 7172
        STOCK_ZGNX = 7173
        STOCK_ZION = 7174
        STOCK_ZIONW = 7175
        STOCK_ZIONZ = 7176
        STOCK_ZIOP = 7177
        STOCK_ZIXI = 7178
        STOCK_ZJZZT = 7179
        STOCK_ZKIN = 7180
        STOCK_ZLAB = 7181
        STOCK_ZN = 7182
        STOCK_ZNGA = 7183
        STOCK_ZNH = 7184
        STOCK_ZNWAA = 7185
        STOCK_ZOES = 7186
        STOCK_ZSAN = 7187
        STOCK_ZTO = 7188
        STOCK_ZTR = 7189
        STOCK_ZTS = 7190
        STOCK_ZUMZ = 7191
        STOCK_ZVV = 7192
        STOCK_ZX = 7193
        STOCK_ZYME = 7194
        STOCK_ZYNE = 7195

        def __str__(self):
            if self == stock.STOCK.STOCK_INVALID:
                return "invalid"
            elif self == stock.STOCK.STOCK_A:
                return "a"
            elif self == stock.STOCK.STOCK_AA:
                return "aa"
            elif self == stock.STOCK.STOCK_AAAP:
                return "aaap"
            elif self == stock.STOCK.STOCK_AABA:
                return "aaba"
            elif self == stock.STOCK.STOCK_AAC:
                return "aac"
            elif self == stock.STOCK.STOCK_AAL:
                return "aal"
            elif self == stock.STOCK.STOCK_AAMC:
                return "aamc"
            elif self == stock.STOCK.STOCK_AAME:
                return "aame"
            elif self == stock.STOCK.STOCK_AAN:
                return "aan"
            elif self == stock.STOCK.STOCK_AAOI:
                return "aaoi"
            elif self == stock.STOCK.STOCK_AAON:
                return "aaon"
            elif self == stock.STOCK.STOCK_AAP:
                return "aap"
            elif self == stock.STOCK.STOCK_AAPL:
                return "aapl"
            elif self == stock.STOCK.STOCK_AAT:
                return "aat"
            elif self == stock.STOCK.STOCK_AAU:
                return "aau"
            elif self == stock.STOCK.STOCK_AAV:
                return "aav"
            elif self == stock.STOCK.STOCK_AAWW:
                return "aaww"
            elif self == stock.STOCK.STOCK_AAXN:
                return "aaxn"
            elif self == stock.STOCK.STOCK_AB:
                return "ab"
            elif self == stock.STOCK.STOCK_ABAC:
                return "abac"
            elif self == stock.STOCK.STOCK_ABAX:
                return "abax"
            elif self == stock.STOCK.STOCK_ABB:
                return "abb"
            elif self == stock.STOCK.STOCK_ABBV:
                return "abbv"
            elif self == stock.STOCK.STOCK_ABC:
                return "abc"
            elif self == stock.STOCK.STOCK_ABCB:
                return "abcb"
            elif self == stock.STOCK.STOCK_ABCD:
                return "abcd"
            elif self == stock.STOCK.STOCK_ABCO:
                return "abco"
            elif self == stock.STOCK.STOCK_ABDC:
                return "abdc"
            elif self == stock.STOCK.STOCK_ABE:
                return "abe"
            elif self == stock.STOCK.STOCK_ABEO:
                return "abeo"
            elif self == stock.STOCK.STOCK_ABEOW:
                return "abeow"
            elif self == stock.STOCK.STOCK_ABEV:
                return "abev"
            elif self == stock.STOCK.STOCK_ABG:
                return "abg"
            elif self == stock.STOCK.STOCK_ABIL:
                return "abil"
            elif self == stock.STOCK.STOCK_ABIO:
                return "abio"
            elif self == stock.STOCK.STOCK_ABLX:
                return "ablx"
            elif self == stock.STOCK.STOCK_ABM:
                return "abm"
            elif self == stock.STOCK.STOCK_ABMD:
                return "abmd"
            elif self == stock.STOCK.STOCK_ABR:
                return "abr"
            elif self == stock.STOCK.STOCK_ABRN:
                return "abrn"
            elif self == stock.STOCK.STOCK_ABR_A:
                return "abr_a"
            elif self == stock.STOCK.STOCK_ABR_B:
                return "abr_b"
            elif self == stock.STOCK.STOCK_ABR_C:
                return "abr_c"
            elif self == stock.STOCK.STOCK_ABT:
                return "abt"
            elif self == stock.STOCK.STOCK_ABTX:
                return "abtx"
            elif self == stock.STOCK.STOCK_ABUS:
                return "abus"
            elif self == stock.STOCK.STOCK_ABX:
                return "abx"
            elif self == stock.STOCK.STOCK_ABY:
                return "aby"
            elif self == stock.STOCK.STOCK_AC:
                return "ac"
            elif self == stock.STOCK.STOCK_ACAD:
                return "acad"
            elif self == stock.STOCK.STOCK_ACBI:
                return "acbi"
            elif self == stock.STOCK.STOCK_ACC:
                return "acc"
            elif self == stock.STOCK.STOCK_ACCO:
                return "acco"
            elif self == stock.STOCK.STOCK_ACCP:
                return "accp"
            elif self == stock.STOCK.STOCK_ACER:
                return "acer"
            elif self == stock.STOCK.STOCK_ACERW:
                return "acerw"
            elif self == stock.STOCK.STOCK_ACET:
                return "acet"
            elif self == stock.STOCK.STOCK_ACFC:
                return "acfc"
            elif self == stock.STOCK.STOCK_ACGL:
                return "acgl"
            elif self == stock.STOCK.STOCK_ACGLO:
                return "acglo"
            elif self == stock.STOCK.STOCK_ACGLP:
                return "acglp"
            elif self == stock.STOCK.STOCK_ACH:
                return "ach"
            elif self == stock.STOCK.STOCK_ACHC:
                return "achc"
            elif self == stock.STOCK.STOCK_ACHN:
                return "achn"
            elif self == stock.STOCK.STOCK_ACHV:
                return "achv"
            elif self == stock.STOCK.STOCK_ACIA:
                return "acia"
            elif self == stock.STOCK.STOCK_ACIU:
                return "aciu"
            elif self == stock.STOCK.STOCK_ACIW:
                return "aciw"
            elif self == stock.STOCK.STOCK_ACLS:
                return "acls"
            elif self == stock.STOCK.STOCK_ACM:
                return "acm"
            elif self == stock.STOCK.STOCK_ACMR:
                return "acmr"
            elif self == stock.STOCK.STOCK_ACN:
                return "acn"
            elif self == stock.STOCK.STOCK_ACNB:
                return "acnb"
            elif self == stock.STOCK.STOCK_ACOR:
                return "acor"
            elif self == stock.STOCK.STOCK_ACP:
                return "acp"
            elif self == stock.STOCK.STOCK_ACRE:
                return "acre"
            elif self == stock.STOCK.STOCK_ACRS:
                return "acrs"
            elif self == stock.STOCK.STOCK_ACRX:
                return "acrx"
            elif self == stock.STOCK.STOCK_ACSF:
                return "acsf"
            elif self == stock.STOCK.STOCK_ACSI:
                return "acsi"
            elif self == stock.STOCK.STOCK_ACST:
                return "acst"
            elif self == stock.STOCK.STOCK_ACTA:
                return "acta"
            elif self == stock.STOCK.STOCK_ACTG:
                return "actg"
            elif self == stock.STOCK.STOCK_ACU:
                return "acu"
            elif self == stock.STOCK.STOCK_ACV:
                return "acv"
            elif self == stock.STOCK.STOCK_ACXM:
                return "acxm"
            elif self == stock.STOCK.STOCK_ACY:
                return "acy"
            elif self == stock.STOCK.STOCK_ADAP:
                return "adap"
            elif self == stock.STOCK.STOCK_ADBE:
                return "adbe"
            elif self == stock.STOCK.STOCK_ADC:
                return "adc"
            elif self == stock.STOCK.STOCK_ADES:
                return "ades"
            elif self == stock.STOCK.STOCK_ADHD:
                return "adhd"
            elif self == stock.STOCK.STOCK_ADI:
                return "adi"
            elif self == stock.STOCK.STOCK_ADM:
                return "adm"
            elif self == stock.STOCK.STOCK_ADMA:
                return "adma"
            elif self == stock.STOCK.STOCK_ADMP:
                return "admp"
            elif self == stock.STOCK.STOCK_ADMS:
                return "adms"
            elif self == stock.STOCK.STOCK_ADNT:
                return "adnt"
            elif self == stock.STOCK.STOCK_ADOM:
                return "adom"
            elif self == stock.STOCK.STOCK_ADP:
                return "adp"
            elif self == stock.STOCK.STOCK_ADRO:
                return "adro"
            elif self == stock.STOCK.STOCK_ADS:
                return "ads"
            elif self == stock.STOCK.STOCK_ADSK:
                return "adsk"
            elif self == stock.STOCK.STOCK_ADSW:
                return "adsw"
            elif self == stock.STOCK.STOCK_ADTN:
                return "adtn"
            elif self == stock.STOCK.STOCK_ADUS:
                return "adus"
            elif self == stock.STOCK.STOCK_ADVM:
                return "advm"
            elif self == stock.STOCK.STOCK_ADX:
                return "adx"
            elif self == stock.STOCK.STOCK_ADXS:
                return "adxs"
            elif self == stock.STOCK.STOCK_ADXSW:
                return "adxsw"
            elif self == stock.STOCK.STOCK_AE:
                return "ae"
            elif self == stock.STOCK.STOCK_AEB:
                return "aeb"
            elif self == stock.STOCK.STOCK_AED:
                return "aed"
            elif self == stock.STOCK.STOCK_AEE:
                return "aee"
            elif self == stock.STOCK.STOCK_AEG:
                return "aeg"
            elif self == stock.STOCK.STOCK_AEGN:
                return "aegn"
            elif self == stock.STOCK.STOCK_AEH:
                return "aeh"
            elif self == stock.STOCK.STOCK_AEHR:
                return "aehr"
            elif self == stock.STOCK.STOCK_AEIS:
                return "aeis"
            elif self == stock.STOCK.STOCK_AEK:
                return "aek"
            elif self == stock.STOCK.STOCK_AEL:
                return "ael"
            elif self == stock.STOCK.STOCK_AEM:
                return "aem"
            elif self == stock.STOCK.STOCK_AEMD:
                return "aemd"
            elif self == stock.STOCK.STOCK_AEO:
                return "aeo"
            elif self == stock.STOCK.STOCK_AEP:
                return "aep"
            elif self == stock.STOCK.STOCK_AER:
                return "aer"
            elif self == stock.STOCK.STOCK_AERI:
                return "aeri"
            elif self == stock.STOCK.STOCK_AES:
                return "aes"
            elif self == stock.STOCK.STOCK_AET:
                return "aet"
            elif self == stock.STOCK.STOCK_AETI:
                return "aeti"
            elif self == stock.STOCK.STOCK_AEUA:
                return "aeua"
            elif self == stock.STOCK.STOCK_AEY:
                return "aey"
            elif self == stock.STOCK.STOCK_AEZS:
                return "aezs"
            elif self == stock.STOCK.STOCK_AFAM:
                return "afam"
            elif self == stock.STOCK.STOCK_AFB:
                return "afb"
            elif self == stock.STOCK.STOCK_AFC:
                return "afc"
            elif self == stock.STOCK.STOCK_AFG:
                return "afg"
            elif self == stock.STOCK.STOCK_AFGE:
                return "afge"
            elif self == stock.STOCK.STOCK_AFGH:
                return "afgh"
            elif self == stock.STOCK.STOCK_AFH:
                return "afh"
            elif self == stock.STOCK.STOCK_AFHBL:
                return "afhbl"
            elif self == stock.STOCK.STOCK_AFI:
                return "afi"
            elif self == stock.STOCK.STOCK_AFL:
                return "afl"
            elif self == stock.STOCK.STOCK_AFMD:
                return "afmd"
            elif self == stock.STOCK.STOCK_AFSD:
                return "afsd"
            elif self == stock.STOCK.STOCK_AFSI:
                return "afsi"
            elif self == stock.STOCK.STOCK_AFSI_A:
                return "afsi_a"
            elif self == stock.STOCK.STOCK_AFSI_B:
                return "afsi_b"
            elif self == stock.STOCK.STOCK_AFSI_C:
                return "afsi_c"
            elif self == stock.STOCK.STOCK_AFSI_D:
                return "afsi_d"
            elif self == stock.STOCK.STOCK_AFSI_E:
                return "afsi_e"
            elif self == stock.STOCK.STOCK_AFSI_F:
                return "afsi_f"
            elif self == stock.STOCK.STOCK_AFSS:
                return "afss"
            elif self == stock.STOCK.STOCK_AFST:
                return "afst"
            elif self == stock.STOCK.STOCK_AFT:
                return "aft"
            elif self == stock.STOCK.STOCK_AFTY:
                return "afty"
            elif self == stock.STOCK.STOCK_AG:
                return "ag"
            elif self == stock.STOCK.STOCK_AGC:
                return "agc"
            elif self == stock.STOCK.STOCK_AGCO:
                return "agco"
            elif self == stock.STOCK.STOCK_AGD:
                return "agd"
            elif self == stock.STOCK.STOCK_AGEN:
                return "agen"
            elif self == stock.STOCK.STOCK_AGFS:
                return "agfs"
            elif self == stock.STOCK.STOCK_AGFSW:
                return "agfsw"
            elif self == stock.STOCK.STOCK_AGGE:
                return "agge"
            elif self == stock.STOCK.STOCK_AGGP:
                return "aggp"
            elif self == stock.STOCK.STOCK_AGGY:
                return "aggy"
            elif self == stock.STOCK.STOCK_AGI:
                return "agi"
            elif self == stock.STOCK.STOCK_AGII:
                return "agii"
            elif self == stock.STOCK.STOCK_AGIIL:
                return "agiil"
            elif self == stock.STOCK.STOCK_AGIO:
                return "agio"
            elif self == stock.STOCK.STOCK_AGLE:
                return "agle"
            elif self == stock.STOCK.STOCK_AGM-A:
                return "agm-a"
            elif self == stock.STOCK.STOCK_AGM:
                return "agm"
            elif self == stock.STOCK.STOCK_AGM_A:
                return "agm_a"
            elif self == stock.STOCK.STOCK_AGM_B:
                return "agm_b"
            elif self == stock.STOCK.STOCK_AGM_C:
                return "agm_c"
            elif self == stock.STOCK.STOCK_AGN:
                return "agn"
            elif self == stock.STOCK.STOCK_AGNC:
                return "agnc"
            elif self == stock.STOCK.STOCK_AGNCB:
                return "agncb"
            elif self == stock.STOCK.STOCK_AGNCN:
                return "agncn"
            elif self == stock.STOCK.STOCK_AGN_A:
                return "agn_a"
            elif self == stock.STOCK.STOCK_AGO:
                return "ago"
            elif self == stock.STOCK.STOCK_AGO_B:
                return "ago_b"
            elif self == stock.STOCK.STOCK_AGO_E:
                return "ago_e"
            elif self == stock.STOCK.STOCK_AGO_F:
                return "ago_f"
            elif self == stock.STOCK.STOCK_AGR:
                return "agr"
            elif self == stock.STOCK.STOCK_AGRO:
                return "agro"
            elif self == stock.STOCK.STOCK_AGRX:
                return "agrx"
            elif self == stock.STOCK.STOCK_AGT:
                return "agt"
            elif self == stock.STOCK.STOCK_AGTC:
                return "agtc"
            elif self == stock.STOCK.STOCK_AGU:
                return "agu"
            elif self == stock.STOCK.STOCK_AGX:
                return "agx"
            elif self == stock.STOCK.STOCK_AGYS:
                return "agys"
            elif self == stock.STOCK.STOCK_AHC:
                return "ahc"
            elif self == stock.STOCK.STOCK_AHGP:
                return "ahgp"
            elif self == stock.STOCK.STOCK_AHH:
                return "ahh"
            elif self == stock.STOCK.STOCK_AHL:
                return "ahl"
            elif self == stock.STOCK.STOCK_AHL_C:
                return "ahl_c"
            elif self == stock.STOCK.STOCK_AHL_D:
                return "ahl_d"
            elif self == stock.STOCK.STOCK_AHP:
                return "ahp"
            elif self == stock.STOCK.STOCK_AHPA:
                return "ahpa"
            elif self == stock.STOCK.STOCK_AHPAU:
                return "ahpau"
            elif self == stock.STOCK.STOCK_AHPAW:
                return "ahpaw"
            elif self == stock.STOCK.STOCK_AHPI:
                return "ahpi"
            elif self == stock.STOCK.STOCK_AHP_B:
                return "ahp_b"
            elif self == stock.STOCK.STOCK_AHT:
                return "aht"
            elif self == stock.STOCK.STOCK_AHT_D:
                return "aht_d"
            elif self == stock.STOCK.STOCK_AHT_F:
                return "aht_f"
            elif self == stock.STOCK.STOCK_AHT_G:
                return "aht_g"
            elif self == stock.STOCK.STOCK_AHT_H:
                return "aht_h"
            elif self == stock.STOCK.STOCK_AI:
                return "ai"
            elif self == stock.STOCK.STOCK_AIB-CL:
                return "aib-cl"
            elif self == stock.STOCK.STOCK_AIC:
                return "aic"
            elif self == stock.STOCK.STOCK_AIEQ:
                return "aieq"
            elif self == stock.STOCK.STOCK_AIF:
                return "aif"
            elif self == stock.STOCK.STOCK_AIG-WS:
                return "aig-ws"
            elif self == stock.STOCK.STOCK_AIG:
                return "aig"
            elif self == stock.STOCK.STOCK_AIMC:
                return "aimc"
            elif self == stock.STOCK.STOCK_AIMT:
                return "aimt"
            elif self == stock.STOCK.STOCK_AIN:
                return "ain"
            elif self == stock.STOCK.STOCK_AINC:
                return "ainc"
            elif self == stock.STOCK.STOCK_AINV:
                return "ainv"
            elif self == stock.STOCK.STOCK_AIR:
                return "air"
            elif self == stock.STOCK.STOCK_AIRG:
                return "airg"
            elif self == stock.STOCK.STOCK_AIRI:
                return "airi"
            elif self == stock.STOCK.STOCK_AIRT:
                return "airt"
            elif self == stock.STOCK.STOCK_AIT:
                return "ait"
            elif self == stock.STOCK.STOCK_AIV:
                return "aiv"
            elif self == stock.STOCK.STOCK_AIV_A:
                return "aiv_a"
            elif self == stock.STOCK.STOCK_AIW:
                return "aiw"
            elif self == stock.STOCK.STOCK_AIY:
                return "aiy"
            elif self == stock.STOCK.STOCK_AIZ:
                return "aiz"
            elif self == stock.STOCK.STOCK_AI_B:
                return "ai_b"
            elif self == stock.STOCK.STOCK_AJG:
                return "ajg"
            elif self == stock.STOCK.STOCK_AJRD:
                return "ajrd"
            elif self == stock.STOCK.STOCK_AJX:
                return "ajx"
            elif self == stock.STOCK.STOCK_AJXA:
                return "ajxa"
            elif self == stock.STOCK.STOCK_AKAM:
                return "akam"
            elif self == stock.STOCK.STOCK_AKAO:
                return "akao"
            elif self == stock.STOCK.STOCK_AKBA:
                return "akba"
            elif self == stock.STOCK.STOCK_AKCA:
                return "akca"
            elif self == stock.STOCK.STOCK_AKER:
                return "aker"
            elif self == stock.STOCK.STOCK_AKG:
                return "akg"
            elif self == stock.STOCK.STOCK_AKO-A:
                return "ako-a"
            elif self == stock.STOCK.STOCK_AKO-B:
                return "ako-b"
            elif self == stock.STOCK.STOCK_AKP:
                return "akp"
            elif self == stock.STOCK.STOCK_AKR:
                return "akr"
            elif self == stock.STOCK.STOCK_AKRX:
                return "akrx"
            elif self == stock.STOCK.STOCK_AKS:
                return "aks"
            elif self == stock.STOCK.STOCK_AKTS:
                return "akts"
            elif self == stock.STOCK.STOCK_AKTX:
                return "aktx"
            elif self == stock.STOCK.STOCK_AL:
                return "al"
            elif self == stock.STOCK.STOCK_ALB:
                return "alb"
            elif self == stock.STOCK.STOCK_ALBO:
                return "albo"
            elif self == stock.STOCK.STOCK_ALCO:
                return "alco"
            elif self == stock.STOCK.STOCK_ALDR:
                return "aldr"
            elif self == stock.STOCK.STOCK_ALDW:
                return "aldw"
            elif self == stock.STOCK.STOCK_ALDX:
                return "aldx"
            elif self == stock.STOCK.STOCK_ALE:
                return "ale"
            elif self == stock.STOCK.STOCK_ALEX:
                return "alex"
            elif self == stock.STOCK.STOCK_ALFI:
                return "alfi"
            elif self == stock.STOCK.STOCK_ALG:
                return "alg"
            elif self == stock.STOCK.STOCK_ALGN:
                return "algn"
            elif self == stock.STOCK.STOCK_ALGT:
                return "algt"
            elif self == stock.STOCK.STOCK_ALIM:
                return "alim"
            elif self == stock.STOCK.STOCK_ALJJ:
                return "aljj"
            elif self == stock.STOCK.STOCK_ALK:
                return "alk"
            elif self == stock.STOCK.STOCK_ALKS:
                return "alks"
            elif self == stock.STOCK.STOCK_ALL:
                return "all"
            elif self == stock.STOCK.STOCK_ALLE:
                return "alle"
            elif self == stock.STOCK.STOCK_ALLT:
                return "allt"
            elif self == stock.STOCK.STOCK_ALLY:
                return "ally"
            elif self == stock.STOCK.STOCK_ALLY_A:
                return "ally_a"
            elif self == stock.STOCK.STOCK_ALL_A:
                return "all_a"
            elif self == stock.STOCK.STOCK_ALL_B:
                return "all_b"
            elif self == stock.STOCK.STOCK_ALL_C:
                return "all_c"
            elif self == stock.STOCK.STOCK_ALL_D:
                return "all_d"
            elif self == stock.STOCK.STOCK_ALL_E:
                return "all_e"
            elif self == stock.STOCK.STOCK_ALL_F:
                return "all_f"
            elif self == stock.STOCK.STOCK_ALN:
                return "aln"
            elif self == stock.STOCK.STOCK_ALNA:
                return "alna"
            elif self == stock.STOCK.STOCK_ALNY:
                return "alny"
            elif self == stock.STOCK.STOCK_ALO:
                return "alo"
            elif self == stock.STOCK.STOCK_ALOG:
                return "alog"
            elif self == stock.STOCK.STOCK_ALOT:
                return "alot"
            elif self == stock.STOCK.STOCK_ALPN:
                return "alpn"
            elif self == stock.STOCK.STOCK_ALP_O-CL:
                return "alp_o-cl"
            elif self == stock.STOCK.STOCK_ALP_Q:
                return "alp_q"
            elif self == stock.STOCK.STOCK_ALQA:
                return "alqa"
            elif self == stock.STOCK.STOCK_ALRM:
                return "alrm"
            elif self == stock.STOCK.STOCK_ALRN:
                return "alrn"
            elif self == stock.STOCK.STOCK_ALSK:
                return "alsk"
            elif self == stock.STOCK.STOCK_ALSN:
                return "alsn"
            elif self == stock.STOCK.STOCK_ALT:
                return "alt"
            elif self == stock.STOCK.STOCK_ALTR:
                return "altr"
            elif self == stock.STOCK.STOCK_ALTY:
                return "alty"
            elif self == stock.STOCK.STOCK_ALV:
                return "alv"
            elif self == stock.STOCK.STOCK_ALX:
                return "alx"
            elif self == stock.STOCK.STOCK_ALXN:
                return "alxn"
            elif self == stock.STOCK.STOCK_AM:
                return "am"
            elif self == stock.STOCK.STOCK_AMAG:
                return "amag"
            elif self == stock.STOCK.STOCK_AMAT:
                return "amat"
            elif self == stock.STOCK.STOCK_AMBA:
                return "amba"
            elif self == stock.STOCK.STOCK_AMBC:
                return "ambc"
            elif self == stock.STOCK.STOCK_AMBCW:
                return "ambcw"
            elif self == stock.STOCK.STOCK_AMBR:
                return "ambr"
            elif self == stock.STOCK.STOCK_AMC:
                return "amc"
            elif self == stock.STOCK.STOCK_AMCA:
                return "amca"
            elif self == stock.STOCK.STOCK_AMCN:
                return "amcn"
            elif self == stock.STOCK.STOCK_AMCX:
                return "amcx"
            elif self == stock.STOCK.STOCK_AMD:
                return "amd"
            elif self == stock.STOCK.STOCK_AMDA:
                return "amda"
            elif self == stock.STOCK.STOCK_AME:
                return "ame"
            elif self == stock.STOCK.STOCK_AMED:
                return "amed"
            elif self == stock.STOCK.STOCK_AMFW:
                return "amfw"
            elif self == stock.STOCK.STOCK_AMG:
                return "amg"
            elif self == stock.STOCK.STOCK_AMGN:
                return "amgn"
            elif self == stock.STOCK.STOCK_AMGP:
                return "amgp"
            elif self == stock.STOCK.STOCK_AMH:
                return "amh"
            elif self == stock.STOCK.STOCK_AMH_C:
                return "amh_c"
            elif self == stock.STOCK.STOCK_AMH_D:
                return "amh_d"
            elif self == stock.STOCK.STOCK_AMH_E:
                return "amh_e"
            elif self == stock.STOCK.STOCK_AMH_F:
                return "amh_f"
            elif self == stock.STOCK.STOCK_AMH_G:
                return "amh_g"
            elif self == stock.STOCK.STOCK_AMID:
                return "amid"
            elif self == stock.STOCK.STOCK_AMKR:
                return "amkr"
            elif self == stock.STOCK.STOCK_AMLX:
                return "amlx"
            elif self == stock.STOCK.STOCK_AMMA:
                return "amma"
            elif self == stock.STOCK.STOCK_AMN:
                return "amn"
            elif self == stock.STOCK.STOCK_AMNB:
                return "amnb"
            elif self == stock.STOCK.STOCK_AMOT:
                return "amot"
            elif self == stock.STOCK.STOCK_AMOV:
                return "amov"
            elif self == stock.STOCK.STOCK_AMP:
                return "amp"
            elif self == stock.STOCK.STOCK_AMPE:
                return "ampe"
            elif self == stock.STOCK.STOCK_AMPH:
                return "amph"
            elif self == stock.STOCK.STOCK_AMRB:
                return "amrb"
            elif self == stock.STOCK.STOCK_AMRC:
                return "amrc"
            elif self == stock.STOCK.STOCK_AMRH:
                return "amrh"
            elif self == stock.STOCK.STOCK_AMRHW:
                return "amrhw"
            elif self == stock.STOCK.STOCK_AMRK:
                return "amrk"
            elif self == stock.STOCK.STOCK_AMRN:
                return "amrn"
            elif self == stock.STOCK.STOCK_AMRS:
                return "amrs"
            elif self == stock.STOCK.STOCK_AMS:
                return "ams"
            elif self == stock.STOCK.STOCK_AMSC:
                return "amsc"
            elif self == stock.STOCK.STOCK_AMSF:
                return "amsf"
            elif self == stock.STOCK.STOCK_AMSWA:
                return "amswa"
            elif self == stock.STOCK.STOCK_AMT:
                return "amt"
            elif self == stock.STOCK.STOCK_AMTD:
                return "amtd"
            elif self == stock.STOCK.STOCK_AMTX:
                return "amtx"
            elif self == stock.STOCK.STOCK_AMT_B:
                return "amt_b"
            elif self == stock.STOCK.STOCK_AMWD:
                return "amwd"
            elif self == stock.STOCK.STOCK_AMX:
                return "amx"
            elif self == stock.STOCK.STOCK_AMZA:
                return "amza"
            elif self == stock.STOCK.STOCK_AMZN:
                return "amzn"
            elif self == stock.STOCK.STOCK_AN:
                return "an"
            elif self == stock.STOCK.STOCK_ANAB:
                return "anab"
            elif self == stock.STOCK.STOCK_ANAT:
                return "anat"
            elif self == stock.STOCK.STOCK_ANCB:
                return "ancb"
            elif self == stock.STOCK.STOCK_ANCX:
                return "ancx"
            elif self == stock.STOCK.STOCK_ANDA:
                return "anda"
            elif self == stock.STOCK.STOCK_ANDAR:
                return "andar"
            elif self == stock.STOCK.STOCK_ANDAU:
                return "andau"
            elif self == stock.STOCK.STOCK_ANDAW:
                return "andaw"
            elif self == stock.STOCK.STOCK_ANDE:
                return "ande"
            elif self == stock.STOCK.STOCK_ANDV:
                return "andv"
            elif self == stock.STOCK.STOCK_ANDX:
                return "andx"
            elif self == stock.STOCK.STOCK_ANET:
                return "anet"
            elif self == stock.STOCK.STOCK_ANF:
                return "anf"
            elif self == stock.STOCK.STOCK_ANFI:
                return "anfi"
            elif self == stock.STOCK.STOCK_ANGI:
                return "angi"
            elif self == stock.STOCK.STOCK_ANGO:
                return "ango"
            elif self == stock.STOCK.STOCK_ANH:
                return "anh"
            elif self == stock.STOCK.STOCK_ANH_A:
                return "anh_a"
            elif self == stock.STOCK.STOCK_ANH_B:
                return "anh_b"
            elif self == stock.STOCK.STOCK_ANH_C:
                return "anh_c"
            elif self == stock.STOCK.STOCK_ANIK:
                return "anik"
            elif self == stock.STOCK.STOCK_ANIP:
                return "anip"
            elif self == stock.STOCK.STOCK_ANSS:
                return "anss"
            elif self == stock.STOCK.STOCK_ANTH:
                return "anth"
            elif self == stock.STOCK.STOCK_ANTM:
                return "antm"
            elif self == stock.STOCK.STOCK_ANTX:
                return "antx"
            elif self == stock.STOCK.STOCK_ANW:
                return "anw"
            elif self == stock.STOCK.STOCK_ANY:
                return "any"
            elif self == stock.STOCK.STOCK_AOBC:
                return "aobc"
            elif self == stock.STOCK.STOCK_AOD:
                return "aod"
            elif self == stock.STOCK.STOCK_AOI:
                return "aoi"
            elif self == stock.STOCK.STOCK_AON:
                return "aon"
            elif self == stock.STOCK.STOCK_AOS:
                return "aos"
            elif self == stock.STOCK.STOCK_AOSL:
                return "aosl"
            elif self == stock.STOCK.STOCK_AOXG:
                return "aoxg"
            elif self == stock.STOCK.STOCK_AP:
                return "ap"
            elif self == stock.STOCK.STOCK_APA:
                return "apa"
            elif self == stock.STOCK.STOCK_APAM:
                return "apam"
            elif self == stock.STOCK.STOCK_APB:
                return "apb"
            elif self == stock.STOCK.STOCK_APC:
                return "apc"
            elif self == stock.STOCK.STOCK_APD:
                return "apd"
            elif self == stock.STOCK.STOCK_APDN:
                return "apdn"
            elif self == stock.STOCK.STOCK_APDNW:
                return "apdnw"
            elif self == stock.STOCK.STOCK_APEI:
                return "apei"
            elif self == stock.STOCK.STOCK_APEN:
                return "apen"
            elif self == stock.STOCK.STOCK_APF:
                return "apf"
            elif self == stock.STOCK.STOCK_APH:
                return "aph"
            elif self == stock.STOCK.STOCK_APHB:
                return "aphb"
            elif self == stock.STOCK.STOCK_APLE:
                return "aple"
            elif self == stock.STOCK.STOCK_APLP:
                return "aplp"
            elif self == stock.STOCK.STOCK_APLS:
                return "apls"
            elif self == stock.STOCK.STOCK_APO:
                return "apo"
            elif self == stock.STOCK.STOCK_APOG:
                return "apog"
            elif self == stock.STOCK.STOCK_APOP:
                return "apop"
            elif self == stock.STOCK.STOCK_APOPW:
                return "apopw"
            elif self == stock.STOCK.STOCK_APO_A:
                return "apo_a"
            elif self == stock.STOCK.STOCK_APPF:
                return "appf"
            elif self == stock.STOCK.STOCK_APPN:
                return "appn"
            elif self == stock.STOCK.STOCK_APPS:
                return "apps"
            elif self == stock.STOCK.STOCK_APRI:
                return "apri"
            elif self == stock.STOCK.STOCK_APRN:
                return "aprn"
            elif self == stock.STOCK.STOCK_APT:
                return "apt"
            elif self == stock.STOCK.STOCK_APTI:
                return "apti"
            elif self == stock.STOCK.STOCK_APTO:
                return "apto"
            elif self == stock.STOCK.STOCK_APTS:
                return "apts"
            elif self == stock.STOCK.STOCK_APU:
                return "apu"
            elif self == stock.STOCK.STOCK_APVO:
                return "apvo"
            elif self == stock.STOCK.STOCK_APWC:
                return "apwc"
            elif self == stock.STOCK.STOCK_AQ:
                return "aq"
            elif self == stock.STOCK.STOCK_AQB:
                return "aqb"
            elif self == stock.STOCK.STOCK_AQMS:
                return "aqms"
            elif self == stock.STOCK.STOCK_AQN:
                return "aqn"
            elif self == stock.STOCK.STOCK_AQUA:
                return "aqua"
            elif self == stock.STOCK.STOCK_AQXP:
                return "aqxp"
            elif self == stock.STOCK.STOCK_AR:
                return "ar"
            elif self == stock.STOCK.STOCK_ARA:
                return "ara"
            elif self == stock.STOCK.STOCK_ARAY:
                return "aray"
            elif self == stock.STOCK.STOCK_ARC:
                return "arc"
            elif self == stock.STOCK.STOCK_ARCB:
                return "arcb"
            elif self == stock.STOCK.STOCK_ARCC:
                return "arcc"
            elif self == stock.STOCK.STOCK_ARCH:
                return "arch"
            elif self == stock.STOCK.STOCK_ARCI:
                return "arci"
            elif self == stock.STOCK.STOCK_ARCM:
                return "arcm"
            elif self == stock.STOCK.STOCK_ARCO:
                return "arco"
            elif self == stock.STOCK.STOCK_ARCW:
                return "arcw"
            elif self == stock.STOCK.STOCK_ARCX:
                return "arcx"
            elif self == stock.STOCK.STOCK_ARD:
                return "ard"
            elif self == stock.STOCK.STOCK_ARDC:
                return "ardc"
            elif self == stock.STOCK.STOCK_ARDM:
                return "ardm"
            elif self == stock.STOCK.STOCK_ARDX:
                return "ardx"
            elif self == stock.STOCK.STOCK_ARE:
                return "are"
            elif self == stock.STOCK.STOCK_ARES:
                return "ares"
            elif self == stock.STOCK.STOCK_ARES_A:
                return "ares_a"
            elif self == stock.STOCK.STOCK_AREX:
                return "arex"
            elif self == stock.STOCK.STOCK_ARE_D:
                return "are_d"
            elif self == stock.STOCK.STOCK_ARGS:
                return "args"
            elif self == stock.STOCK.STOCK_ARGX:
                return "argx"
            elif self == stock.STOCK.STOCK_ARH_C:
                return "arh_c"
            elif self == stock.STOCK.STOCK_ARI:
                return "ari"
            elif self == stock.STOCK.STOCK_ARII:
                return "arii"
            elif self == stock.STOCK.STOCK_ARI_C:
                return "ari_c"
            elif self == stock.STOCK.STOCK_ARKG:
                return "arkg"
            elif self == stock.STOCK.STOCK_ARKK:
                return "arkk"
            elif self == stock.STOCK.STOCK_ARKQ:
                return "arkq"
            elif self == stock.STOCK.STOCK_ARKR:
                return "arkr"
            elif self == stock.STOCK.STOCK_ARKW:
                return "arkw"
            elif self == stock.STOCK.STOCK_ARL:
                return "arl"
            elif self == stock.STOCK.STOCK_ARLP:
                return "arlp"
            elif self == stock.STOCK.STOCK_ARLZ:
                return "arlz"
            elif self == stock.STOCK.STOCK_ARMK:
                return "armk"
            elif self == stock.STOCK.STOCK_ARNA:
                return "arna"
            elif self == stock.STOCK.STOCK_ARNC:
                return "arnc"
            elif self == stock.STOCK.STOCK_ARNC_:
                return "arnc_"
            elif self == stock.STOCK.STOCK_ARNC_B:
                return "arnc_b"
            elif self == stock.STOCK.STOCK_AROC:
                return "aroc"
            elif self == stock.STOCK.STOCK_AROW:
                return "arow"
            elif self == stock.STOCK.STOCK_ARQL:
                return "arql"
            elif self == stock.STOCK.STOCK_ARR:
                return "arr"
            elif self == stock.STOCK.STOCK_ARRS:
                return "arrs"
            elif self == stock.STOCK.STOCK_ARRY:
                return "arry"
            elif self == stock.STOCK.STOCK_ARR_A:
                return "arr_a"
            elif self == stock.STOCK.STOCK_ARR_B:
                return "arr_b"
            elif self == stock.STOCK.STOCK_ARTNA:
                return "artna"
            elif self == stock.STOCK.STOCK_ARTW:
                return "artw"
            elif self == stock.STOCK.STOCK_ARTX:
                return "artx"
            elif self == stock.STOCK.STOCK_ARW:
                return "arw"
            elif self == stock.STOCK.STOCK_ARWR:
                return "arwr"
            elif self == stock.STOCK.STOCK_ASA:
                return "asa"
            elif self == stock.STOCK.STOCK_ASB-WS:
                return "asb-ws"
            elif self == stock.STOCK.STOCK_ASB:
                return "asb"
            elif self == stock.STOCK.STOCK_ASB_C:
                return "asb_c"
            elif self == stock.STOCK.STOCK_ASB_D:
                return "asb_d"
            elif self == stock.STOCK.STOCK_ASC:
                return "asc"
            elif self == stock.STOCK.STOCK_ASCMA:
                return "ascma"
            elif self == stock.STOCK.STOCK_ASET:
                return "aset"
            elif self == stock.STOCK.STOCK_ASFI:
                return "asfi"
            elif self == stock.STOCK.STOCK_ASG:
                return "asg"
            elif self == stock.STOCK.STOCK_ASGN:
                return "asgn"
            elif self == stock.STOCK.STOCK_ASH:
                return "ash"
            elif self == stock.STOCK.STOCK_ASHX:
                return "ashx"
            elif self == stock.STOCK.STOCK_ASIX:
                return "asix"
            elif self == stock.STOCK.STOCK_ASM:
                return "asm"
            elif self == stock.STOCK.STOCK_ASMB:
                return "asmb"
            elif self == stock.STOCK.STOCK_ASML:
                return "asml"
            elif self == stock.STOCK.STOCK_ASNA:
                return "asna"
            elif self == stock.STOCK.STOCK_ASND:
                return "asnd"
            elif self == stock.STOCK.STOCK_ASNS:
                return "asns"
            elif self == stock.STOCK.STOCK_ASPN:
                return "aspn"
            elif self == stock.STOCK.STOCK_ASPS:
                return "asps"
            elif self == stock.STOCK.STOCK_ASPU:
                return "aspu"
            elif self == stock.STOCK.STOCK_ASR:
                return "asr"
            elif self == stock.STOCK.STOCK_ASRV:
                return "asrv"
            elif self == stock.STOCK.STOCK_ASRVP:
                return "asrvp"
            elif self == stock.STOCK.STOCK_AST:
                return "ast"
            elif self == stock.STOCK.STOCK_ASTC:
                return "astc"
            elif self == stock.STOCK.STOCK_ASTE:
                return "aste"
            elif self == stock.STOCK.STOCK_ASUR:
                return "asur"
            elif self == stock.STOCK.STOCK_ASV:
                return "asv"
            elif self == stock.STOCK.STOCK_ASX:
                return "asx"
            elif self == stock.STOCK.STOCK_ASYS:
                return "asys"
            elif self == stock.STOCK.STOCK_AT:
                return "at"
            elif self == stock.STOCK.STOCK_ATAC:
                return "atac"
            elif self == stock.STOCK.STOCK_ATACR:
                return "atacr"
            elif self == stock.STOCK.STOCK_ATACU:
                return "atacu"
            elif self == stock.STOCK.STOCK_ATAI:
                return "atai"
            elif self == stock.STOCK.STOCK_ATAX:
                return "atax"
            elif self == stock.STOCK.STOCK_ATEC:
                return "atec"
            elif self == stock.STOCK.STOCK_ATEN:
                return "aten"
            elif self == stock.STOCK.STOCK_ATGE:
                return "atge"
            elif self == stock.STOCK.STOCK_ATH:
                return "ath"
            elif self == stock.STOCK.STOCK_ATHM:
                return "athm"
            elif self == stock.STOCK.STOCK_ATHN:
                return "athn"
            elif self == stock.STOCK.STOCK_ATHX:
                return "athx"
            elif self == stock.STOCK.STOCK_ATI:
                return "ati"
            elif self == stock.STOCK.STOCK_ATKR:
                return "atkr"
            elif self == stock.STOCK.STOCK_ATLC:
                return "atlc"
            elif self == stock.STOCK.STOCK_ATLO:
                return "atlo"
            elif self == stock.STOCK.STOCK_ATNI:
                return "atni"
            elif self == stock.STOCK.STOCK_ATNM:
                return "atnm"
            elif self == stock.STOCK.STOCK_ATNX:
                return "atnx"
            elif self == stock.STOCK.STOCK_ATO:
                return "ato"
            elif self == stock.STOCK.STOCK_ATOM:
                return "atom"
            elif self == stock.STOCK.STOCK_ATOS:
                return "atos"
            elif self == stock.STOCK.STOCK_ATR:
                return "atr"
            elif self == stock.STOCK.STOCK_ATRA:
                return "atra"
            elif self == stock.STOCK.STOCK_ATRC:
                return "atrc"
            elif self == stock.STOCK.STOCK_ATRI:
                return "atri"
            elif self == stock.STOCK.STOCK_ATRO:
                return "atro"
            elif self == stock.STOCK.STOCK_ATRS:
                return "atrs"
            elif self == stock.STOCK.STOCK_ATSG:
                return "atsg"
            elif self == stock.STOCK.STOCK_ATTO:
                return "atto"
            elif self == stock.STOCK.STOCK_ATTU:
                return "attu"
            elif self == stock.STOCK.STOCK_ATU:
                return "atu"
            elif self == stock.STOCK.STOCK_ATUS:
                return "atus"
            elif self == stock.STOCK.STOCK_ATV:
                return "atv"
            elif self == stock.STOCK.STOCK_ATVI:
                return "atvi"
            elif self == stock.STOCK.STOCK_ATXI:
                return "atxi"
            elif self == stock.STOCK.STOCK_AU:
                return "au"
            elif self == stock.STOCK.STOCK_AUBN:
                return "aubn"
            elif self == stock.STOCK.STOCK_AUDC:
                return "audc"
            elif self == stock.STOCK.STOCK_AUG:
                return "aug"
            elif self == stock.STOCK.STOCK_AUMN:
                return "aumn"
            elif self == stock.STOCK.STOCK_AUO:
                return "auo"
            elif self == stock.STOCK.STOCK_AUPH:
                return "auph"
            elif self == stock.STOCK.STOCK_AUTO:
                return "auto"
            elif self == stock.STOCK.STOCK_AUY:
                return "auy"
            elif self == stock.STOCK.STOCK_AVA:
                return "ava"
            elif self == stock.STOCK.STOCK_AVAL:
                return "aval"
            elif self == stock.STOCK.STOCK_AVAV:
                return "avav"
            elif self == stock.STOCK.STOCK_AVB:
                return "avb"
            elif self == stock.STOCK.STOCK_AVD:
                return "avd"
            elif self == stock.STOCK.STOCK_AVDL:
                return "avdl"
            elif self == stock.STOCK.STOCK_AVEO:
                return "aveo"
            elif self == stock.STOCK.STOCK_AVGO:
                return "avgo"
            elif self == stock.STOCK.STOCK_AVGR:
                return "avgr"
            elif self == stock.STOCK.STOCK_AVH:
                return "avh"
            elif self == stock.STOCK.STOCK_AVHI:
                return "avhi"
            elif self == stock.STOCK.STOCK_AVID:
                return "avid"
            elif self == stock.STOCK.STOCK_AVIR:
                return "avir"
            elif self == stock.STOCK.STOCK_AVK:
                return "avk"
            elif self == stock.STOCK.STOCK_AVNW:
                return "avnw"
            elif self == stock.STOCK.STOCK_AVP:
                return "avp"
            elif self == stock.STOCK.STOCK_AVT:
                return "avt"
            elif self == stock.STOCK.STOCK_AVX:
                return "avx"
            elif self == stock.STOCK.STOCK_AVXL:
                return "avxl"
            elif self == stock.STOCK.STOCK_AVXS:
                return "avxs"
            elif self == stock.STOCK.STOCK_AVY:
                return "avy"
            elif self == stock.STOCK.STOCK_AWF:
                return "awf"
            elif self == stock.STOCK.STOCK_AWI:
                return "awi"
            elif self == stock.STOCK.STOCK_AWK:
                return "awk"
            elif self == stock.STOCK.STOCK_AWP:
                return "awp"
            elif self == stock.STOCK.STOCK_AWR:
                return "awr"
            elif self == stock.STOCK.STOCK_AWRE:
                return "awre"
            elif self == stock.STOCK.STOCK_AWX:
                return "awx"
            elif self == stock.STOCK.STOCK_AXAS:
                return "axas"
            elif self == stock.STOCK.STOCK_AXDX:
                return "axdx"
            elif self == stock.STOCK.STOCK_AXE:
                return "axe"
            elif self == stock.STOCK.STOCK_AXGN:
                return "axgn"
            elif self == stock.STOCK.STOCK_AXL:
                return "axl"
            elif self == stock.STOCK.STOCK_AXON:
                return "axon"
            elif self == stock.STOCK.STOCK_AXP:
                return "axp"
            elif self == stock.STOCK.STOCK_AXR:
                return "axr"
            elif self == stock.STOCK.STOCK_AXS:
                return "axs"
            elif self == stock.STOCK.STOCK_AXSM:
                return "axsm"
            elif self == stock.STOCK.STOCK_AXS_D:
                return "axs_d"
            elif self == stock.STOCK.STOCK_AXS_E:
                return "axs_e"
            elif self == stock.STOCK.STOCK_AXTA:
                return "axta"
            elif self == stock.STOCK.STOCK_AXTI:
                return "axti"
            elif self == stock.STOCK.STOCK_AXU:
                return "axu"
            elif self == stock.STOCK.STOCK_AYI:
                return "ayi"
            elif self == stock.STOCK.STOCK_AYR:
                return "ayr"
            elif self == stock.STOCK.STOCK_AYTU:
                return "aytu"
            elif self == stock.STOCK.STOCK_AYX:
                return "ayx"
            elif self == stock.STOCK.STOCK_AZN:
                return "azn"
            elif self == stock.STOCK.STOCK_AZO:
                return "azo"
            elif self == stock.STOCK.STOCK_AZPN:
                return "azpn"
            elif self == stock.STOCK.STOCK_AZRE:
                return "azre"
            elif self == stock.STOCK.STOCK_AZRX:
                return "azrx"
            elif self == stock.STOCK.STOCK_AZUL:
                return "azul"
            elif self == stock.STOCK.STOCK_AZZ:
                return "azz"
            elif self == stock.STOCK.STOCK_B:
                return "b"
            elif self == stock.STOCK.STOCK_BA:
                return "ba"
            elif self == stock.STOCK.STOCK_BAA:
                return "baa"
            elif self == stock.STOCK.STOCK_BABA:
                return "baba"
            elif self == stock.STOCK.STOCK_BABY:
                return "baby"
            elif self == stock.STOCK.STOCK_BAC-WS-A:
                return "bac-ws-a"
            elif self == stock.STOCK.STOCK_BAC-WS-B:
                return "bac-ws-b"
            elif self == stock.STOCK.STOCK_BAC:
                return "bac"
            elif self == stock.STOCK.STOCK_BAC_A:
                return "bac_a"
            elif self == stock.STOCK.STOCK_BAC_C:
                return "bac_c"
            elif self == stock.STOCK.STOCK_BAC_D:
                return "bac_d"
            elif self == stock.STOCK.STOCK_BAC_E:
                return "bac_e"
            elif self == stock.STOCK.STOCK_BAC_I:
                return "bac_i"
            elif self == stock.STOCK.STOCK_BAC_L:
                return "bac_l"
            elif self == stock.STOCK.STOCK_BAC_W:
                return "bac_w"
            elif self == stock.STOCK.STOCK_BAC_Y:
                return "bac_y"
            elif self == stock.STOCK.STOCK_BAF:
                return "baf"
            elif self == stock.STOCK.STOCK_BAH:
                return "bah"
            elif self == stock.STOCK.STOCK_BAK:
                return "bak"
            elif self == stock.STOCK.STOCK_BAM:
                return "bam"
            elif self == stock.STOCK.STOCK_BANC:
                return "banc"
            elif self == stock.STOCK.STOCK_BANC_C:
                return "banc_c"
            elif self == stock.STOCK.STOCK_BANC_D:
                return "banc_d"
            elif self == stock.STOCK.STOCK_BANC_E:
                return "banc_e"
            elif self == stock.STOCK.STOCK_BAND:
                return "band"
            elif self == stock.STOCK.STOCK_BANF:
                return "banf"
            elif self == stock.STOCK.STOCK_BANFP:
                return "banfp"
            elif self == stock.STOCK.STOCK_BANR:
                return "banr"
            elif self == stock.STOCK.STOCK_BANX:
                return "banx"
            elif self == stock.STOCK.STOCK_BAP:
                return "bap"
            elif self == stock.STOCK.STOCK_BAR:
                return "bar"
            elif self == stock.STOCK.STOCK_BAS:
                return "bas"
            elif self == stock.STOCK.STOCK_BASI:
                return "basi"
            elif self == stock.STOCK.STOCK_BATRA:
                return "batra"
            elif self == stock.STOCK.STOCK_BATRK:
                return "batrk"
            elif self == stock.STOCK.STOCK_BAX:
                return "bax"
            elif self == stock.STOCK.STOCK_BB:
                return "bb"
            elif self == stock.STOCK.STOCK_BBBY:
                return "bbby"
            elif self == stock.STOCK.STOCK_BBC:
                return "bbc"
            elif self == stock.STOCK.STOCK_BBD:
                return "bbd"
            elif self == stock.STOCK.STOCK_BBDO:
                return "bbdo"
            elif self == stock.STOCK.STOCK_BBF:
                return "bbf"
            elif self == stock.STOCK.STOCK_BBG:
                return "bbg"
            elif self == stock.STOCK.STOCK_BBGI:
                return "bbgi"
            elif self == stock.STOCK.STOCK_BBK:
                return "bbk"
            elif self == stock.STOCK.STOCK_BBL:
                return "bbl"
            elif self == stock.STOCK.STOCK_BBN:
                return "bbn"
            elif self == stock.STOCK.STOCK_BBOX:
                return "bbox"
            elif self == stock.STOCK.STOCK_BBRG:
                return "bbrg"
            elif self == stock.STOCK.STOCK_BBRX:
                return "bbrx"
            elif self == stock.STOCK.STOCK_BBSI:
                return "bbsi"
            elif self == stock.STOCK.STOCK_BBT:
                return "bbt"
            elif self == stock.STOCK.STOCK_BBT_D:
                return "bbt_d"
            elif self == stock.STOCK.STOCK_BBT_E:
                return "bbt_e"
            elif self == stock.STOCK.STOCK_BBT_F:
                return "bbt_f"
            elif self == stock.STOCK.STOCK_BBT_G:
                return "bbt_g"
            elif self == stock.STOCK.STOCK_BBT_H:
                return "bbt_h"
            elif self == stock.STOCK.STOCK_BBU:
                return "bbu"
            elif self == stock.STOCK.STOCK_BBVA:
                return "bbva"
            elif self == stock.STOCK.STOCK_BBW:
                return "bbw"
            elif self == stock.STOCK.STOCK_BBX:
                return "bbx"
            elif self == stock.STOCK.STOCK_BBY:
                return "bby"
            elif self == stock.STOCK.STOCK_BC:
                return "bc"
            elif self == stock.STOCK.STOCK_BCAC:
                return "bcac"
            elif self == stock.STOCK.STOCK_BCACR:
                return "bcacr"
            elif self == stock.STOCK.STOCK_BCACU:
                return "bcacu"
            elif self == stock.STOCK.STOCK_BCACW:
                return "bcacw"
            elif self == stock.STOCK.STOCK_BCBP:
                return "bcbp"
            elif self == stock.STOCK.STOCK_BCC:
                return "bcc"
            elif self == stock.STOCK.STOCK_BCD:
                return "bcd"
            elif self == stock.STOCK.STOCK_BCE:
                return "bce"
            elif self == stock.STOCK.STOCK_BCEI:
                return "bcei"
            elif self == stock.STOCK.STOCK_BCH:
                return "bch"
            elif self == stock.STOCK.STOCK_BCI:
                return "bci"
            elif self == stock.STOCK.STOCK_BCLI:
                return "bcli"
            elif self == stock.STOCK.STOCK_BCO:
                return "bco"
            elif self == stock.STOCK.STOCK_BCOM:
                return "bcom"
            elif self == stock.STOCK.STOCK_BCOR:
                return "bcor"
            elif self == stock.STOCK.STOCK_BCOV:
                return "bcov"
            elif self == stock.STOCK.STOCK_BCPC:
                return "bcpc"
            elif self == stock.STOCK.STOCK_BCR:
                return "bcr"
            elif self == stock.STOCK.STOCK_BCRH:
                return "bcrh"
            elif self == stock.STOCK.STOCK_BCRX:
                return "bcrx"
            elif self == stock.STOCK.STOCK_BCS:
                return "bcs"
            elif self == stock.STOCK.STOCK_BCS_D:
                return "bcs_d"
            elif self == stock.STOCK.STOCK_BCTF:
                return "bctf"
            elif self == stock.STOCK.STOCK_BCV:
                return "bcv"
            elif self == stock.STOCK.STOCK_BCV_A:
                return "bcv_a"
            elif self == stock.STOCK.STOCK_BCX:
                return "bcx"
            elif self == stock.STOCK.STOCK_BDC:
                return "bdc"
            elif self == stock.STOCK.STOCK_BDCZ:
                return "bdcz"
            elif self == stock.STOCK.STOCK_BDC_B:
                return "bdc_b"
            elif self == stock.STOCK.STOCK_BDGE:
                return "bdge"
            elif self == stock.STOCK.STOCK_BDJ:
                return "bdj"
            elif self == stock.STOCK.STOCK_BDL:
                return "bdl"
            elif self == stock.STOCK.STOCK_BDN:
                return "bdn"
            elif self == stock.STOCK.STOCK_BDR:
                return "bdr"
            elif self == stock.STOCK.STOCK_BDSI:
                return "bdsi"
            elif self == stock.STOCK.STOCK_BDX:
                return "bdx"
            elif self == stock.STOCK.STOCK_BDXA:
                return "bdxa"
            elif self == stock.STOCK.STOCK_BEAT:
                return "beat"
            elif self == stock.STOCK.STOCK_BEBE:
                return "bebe"
            elif self == stock.STOCK.STOCK_BECN:
                return "becn"
            elif self == stock.STOCK.STOCK_BEDU:
                return "bedu"
            elif self == stock.STOCK.STOCK_BEF:
                return "bef"
            elif self == stock.STOCK.STOCK_BEL:
                return "bel"
            elif self == stock.STOCK.STOCK_BELFA:
                return "belfa"
            elif self == stock.STOCK.STOCK_BELFB:
                return "belfb"
            elif self == stock.STOCK.STOCK_BEMO:
                return "bemo"
            elif self == stock.STOCK.STOCK_BEN:
                return "ben"
            elif self == stock.STOCK.STOCK_BEP:
                return "bep"
            elif self == stock.STOCK.STOCK_BERN:
                return "bern"
            elif self == stock.STOCK.STOCK_BERY:
                return "bery"
            elif self == stock.STOCK.STOCK_BETR:
                return "betr"
            elif self == stock.STOCK.STOCK_BF-A:
                return "bf-a"
            elif self == stock.STOCK.STOCK_BF-B:
                return "bf-b"
            elif self == stock.STOCK.STOCK_BFAM:
                return "bfam"
            elif self == stock.STOCK.STOCK_BFIN:
                return "bfin"
            elif self == stock.STOCK.STOCK_BFIT:
                return "bfit"
            elif self == stock.STOCK.STOCK_BFK:
                return "bfk"
            elif self == stock.STOCK.STOCK_BFO:
                return "bfo"
            elif self == stock.STOCK.STOCK_BFR:
                return "bfr"
            elif self == stock.STOCK.STOCK_BFS:
                return "bfs"
            elif self == stock.STOCK.STOCK_BFS_C:
                return "bfs_c"
            elif self == stock.STOCK.STOCK_BFY:
                return "bfy"
            elif self == stock.STOCK.STOCK_BFZ:
                return "bfz"
            elif self == stock.STOCK.STOCK_BG:
                return "bg"
            elif self == stock.STOCK.STOCK_BGB:
                return "bgb"
            elif self == stock.STOCK.STOCK_BGC:
                return "bgc"
            elif self == stock.STOCK.STOCK_BGCA:
                return "bgca"
            elif self == stock.STOCK.STOCK_BGCP:
                return "bgcp"
            elif self == stock.STOCK.STOCK_BGFV:
                return "bgfv"
            elif self == stock.STOCK.STOCK_BGG:
                return "bgg"
            elif self == stock.STOCK.STOCK_BGH:
                return "bgh"
            elif self == stock.STOCK.STOCK_BGI:
                return "bgi"
            elif self == stock.STOCK.STOCK_BGIO:
                return "bgio"
            elif self == stock.STOCK.STOCK_BGNE:
                return "bgne"
            elif self == stock.STOCK.STOCK_BGR:
                return "bgr"
            elif self == stock.STOCK.STOCK_BGS:
                return "bgs"
            elif self == stock.STOCK.STOCK_BGSF:
                return "bgsf"
            elif self == stock.STOCK.STOCK_BGT:
                return "bgt"
            elif self == stock.STOCK.STOCK_BGX:
                return "bgx"
            elif self == stock.STOCK.STOCK_BGY:
                return "bgy"
            elif self == stock.STOCK.STOCK_BH:
                return "bh"
            elif self == stock.STOCK.STOCK_BHAC:
                return "bhac"
            elif self == stock.STOCK.STOCK_BHACR:
                return "bhacr"
            elif self == stock.STOCK.STOCK_BHACU:
                return "bhacu"
            elif self == stock.STOCK.STOCK_BHACW:
                return "bhacw"
            elif self == stock.STOCK.STOCK_BHB:
                return "bhb"
            elif self == stock.STOCK.STOCK_BHBK:
                return "bhbk"
            elif self == stock.STOCK.STOCK_BHE:
                return "bhe"
            elif self == stock.STOCK.STOCK_BHF:
                return "bhf"
            elif self == stock.STOCK.STOCK_BHGE:
                return "bhge"
            elif self == stock.STOCK.STOCK_BHK:
                return "bhk"
            elif self == stock.STOCK.STOCK_BHLB:
                return "bhlb"
            elif self == stock.STOCK.STOCK_BHP:
                return "bhp"
            elif self == stock.STOCK.STOCK_BHV:
                return "bhv"
            elif self == stock.STOCK.STOCK_BHVN:
                return "bhvn"
            elif self == stock.STOCK.STOCK_BIBL:
                return "bibl"
            elif self == stock.STOCK.STOCK_BID:
                return "bid"
            elif self == stock.STOCK.STOCK_BIDU:
                return "bidu"
            elif self == stock.STOCK.STOCK_BIF:
                return "bif"
            elif self == stock.STOCK.STOCK_BIG:
                return "big"
            elif self == stock.STOCK.STOCK_BIIB:
                return "biib"
            elif self == stock.STOCK.STOCK_BIO-B:
                return "bio-b"
            elif self == stock.STOCK.STOCK_BIO:
                return "bio"
            elif self == stock.STOCK.STOCK_BIOA:
                return "bioa"
            elif self == stock.STOCK.STOCK_BIOC:
                return "bioc"
            elif self == stock.STOCK.STOCK_BIOL:
                return "biol"
            elif self == stock.STOCK.STOCK_BIOS:
                return "bios"
            elif self == stock.STOCK.STOCK_BIP:
                return "bip"
            elif self == stock.STOCK.STOCK_BIT:
                return "bit"
            elif self == stock.STOCK.STOCK_BITA:
                return "bita"
            elif self == stock.STOCK.STOCK_BIVV:
                return "bivv"
            elif self == stock.STOCK.STOCK_BJRI:
                return "bjri"
            elif self == stock.STOCK.STOCK_BJZ:
                return "bjz"
            elif self == stock.STOCK.STOCK_BK:
                return "bk"
            elif self == stock.STOCK.STOCK_BKCC:
                return "bkcc"
            elif self == stock.STOCK.STOCK_BKD:
                return "bkd"
            elif self == stock.STOCK.STOCK_BKE:
                return "bke"
            elif self == stock.STOCK.STOCK_BKEP:
                return "bkep"
            elif self == stock.STOCK.STOCK_BKEPP:
                return "bkepp"
            elif self == stock.STOCK.STOCK_BKH:
                return "bkh"
            elif self == stock.STOCK.STOCK_BKHU:
                return "bkhu"
            elif self == stock.STOCK.STOCK_BKI:
                return "bki"
            elif self == stock.STOCK.STOCK_BKJ:
                return "bkj"
            elif self == stock.STOCK.STOCK_BKK:
                return "bkk"
            elif self == stock.STOCK.STOCK_BKMU:
                return "bkmu"
            elif self == stock.STOCK.STOCK_BKN:
                return "bkn"
            elif self == stock.STOCK.STOCK_BKS:
                return "bks"
            elif self == stock.STOCK.STOCK_BKSC:
                return "bksc"
            elif self == stock.STOCK.STOCK_BKT:
                return "bkt"
            elif self == stock.STOCK.STOCK_BKU:
                return "bku"
            elif self == stock.STOCK.STOCK_BKYI:
                return "bkyi"
            elif self == stock.STOCK.STOCK_BK_C:
                return "bk_c"
            elif self == stock.STOCK.STOCK_BL:
                return "bl"
            elif self == stock.STOCK.STOCK_BLBD:
                return "blbd"
            elif self == stock.STOCK.STOCK_BLCM:
                return "blcm"
            elif self == stock.STOCK.STOCK_BLD:
                return "bld"
            elif self == stock.STOCK.STOCK_BLDP:
                return "bldp"
            elif self == stock.STOCK.STOCK_BLDR:
                return "bldr"
            elif self == stock.STOCK.STOCK_BLE:
                return "ble"
            elif self == stock.STOCK.STOCK_BLES:
                return "bles"
            elif self == stock.STOCK.STOCK_BLFS:
                return "blfs"
            elif self == stock.STOCK.STOCK_BLH:
                return "blh"
            elif self == stock.STOCK.STOCK_BLHY:
                return "blhy"
            elif self == stock.STOCK.STOCK_BLIN:
                return "blin"
            elif self == stock.STOCK.STOCK_BLJ:
                return "blj"
            elif self == stock.STOCK.STOCK_BLK:
                return "blk"
            elif self == stock.STOCK.STOCK_BLKB:
                return "blkb"
            elif self == stock.STOCK.STOCK_BLL:
                return "bll"
            elif self == stock.STOCK.STOCK_BLMN:
                return "blmn"
            elif self == stock.STOCK.STOCK_BLMT:
                return "blmt"
            elif self == stock.STOCK.STOCK_BLPH:
                return "blph"
            elif self == stock.STOCK.STOCK_BLRX:
                return "blrx"
            elif self == stock.STOCK.STOCK_BLUE:
                return "blue"
            elif self == stock.STOCK.STOCK_BLVD:
                return "blvd"
            elif self == stock.STOCK.STOCK_BLVDU:
                return "blvdu"
            elif self == stock.STOCK.STOCK_BLVDW:
                return "blvdw"
            elif self == stock.STOCK.STOCK_BLW:
                return "blw"
            elif self == stock.STOCK.STOCK_BLX:
                return "blx"
            elif self == stock.STOCK.STOCK_BMA:
                return "bma"
            elif self == stock.STOCK.STOCK_BMCH:
                return "bmch"
            elif self == stock.STOCK.STOCK_BME:
                return "bme"
            elif self == stock.STOCK.STOCK_BMI:
                return "bmi"
            elif self == stock.STOCK.STOCK_BMLA:
                return "bmla"
            elif self == stock.STOCK.STOCK_BMLP:
                return "bmlp"
            elif self == stock.STOCK.STOCK_BML_G:
                return "bml_g"
            elif self == stock.STOCK.STOCK_BML_H:
                return "bml_h"
            elif self == stock.STOCK.STOCK_BML_I:
                return "bml_i"
            elif self == stock.STOCK.STOCK_BML_J:
                return "bml_j"
            elif self == stock.STOCK.STOCK_BML_L:
                return "bml_l"
            elif self == stock.STOCK.STOCK_BMO:
                return "bmo"
            elif self == stock.STOCK.STOCK_BMRA:
                return "bmra"
            elif self == stock.STOCK.STOCK_BMRC:
                return "bmrc"
            elif self == stock.STOCK.STOCK_BMRN:
                return "bmrn"
            elif self == stock.STOCK.STOCK_BMS:
                return "bms"
            elif self == stock.STOCK.STOCK_BMTC:
                return "bmtc"
            elif self == stock.STOCK.STOCK_BMY:
                return "bmy"
            elif self == stock.STOCK.STOCK_BNCL:
                return "bncl"
            elif self == stock.STOCK.STOCK_BNDC:
                return "bndc"
            elif self == stock.STOCK.STOCK_BNED:
                return "bned"
            elif self == stock.STOCK.STOCK_BNFT:
                return "bnft"
            elif self == stock.STOCK.STOCK_BNJ:
                return "bnj"
            elif self == stock.STOCK.STOCK_BNS:
                return "bns"
            elif self == stock.STOCK.STOCK_BNSO:
                return "bnso"
            elif self == stock.STOCK.STOCK_BNTC:
                return "bntc"
            elif self == stock.STOCK.STOCK_BNTCW:
                return "bntcw"
            elif self == stock.STOCK.STOCK_BNY:
                return "bny"
            elif self == stock.STOCK.STOCK_BOBE:
                return "bobe"
            elif self == stock.STOCK.STOCK_BOCH:
                return "boch"
            elif self == stock.STOCK.STOCK_BOE:
                return "boe"
            elif self == stock.STOCK.STOCK_BOFI:
                return "bofi"
            elif self == stock.STOCK.STOCK_BOFIL:
                return "bofil"
            elif self == stock.STOCK.STOCK_BOH:
                return "boh"
            elif self == stock.STOCK.STOCK_BOJA:
                return "boja"
            elif self == stock.STOCK.STOCK_BOKF:
                return "bokf"
            elif self == stock.STOCK.STOCK_BOKFL:
                return "bokfl"
            elif self == stock.STOCK.STOCK_BOLD:
                return "bold"
            elif self == stock.STOCK.STOCK_BOLT:
                return "bolt"
            elif self == stock.STOCK.STOCK_BOMN:
                return "bomn"
            elif self == stock.STOCK.STOCK_BONT:
                return "bont"
            elif self == stock.STOCK.STOCK_BOOM:
                return "boom"
            elif self == stock.STOCK.STOCK_BOOT:
                return "boot"
            elif self == stock.STOCK.STOCK_BORN:
                return "born"
            elif self == stock.STOCK.STOCK_BOSC:
                return "bosc"
            elif self == stock.STOCK.STOCK_BOSS:
                return "boss"
            elif self == stock.STOCK.STOCK_BOTJ:
                return "botj"
            elif self == stock.STOCK.STOCK_BOTZ:
                return "botz"
            elif self == stock.STOCK.STOCK_BOX:
                return "box"
            elif self == stock.STOCK.STOCK_BOXL:
                return "boxl"
            elif self == stock.STOCK.STOCK_BP:
                return "bp"
            elif self == stock.STOCK.STOCK_BPFH:
                return "bpfh"
            elif self == stock.STOCK.STOCK_BPFHP:
                return "bpfhp"
            elif self == stock.STOCK.STOCK_BPFHW:
                return "bpfhw"
            elif self == stock.STOCK.STOCK_BPI:
                return "bpi"
            elif self == stock.STOCK.STOCK_BPK:
                return "bpk"
            elif self == stock.STOCK.STOCK_BPL:
                return "bpl"
            elif self == stock.STOCK.STOCK_BPMC:
                return "bpmc"
            elif self == stock.STOCK.STOCK_BPMP:
                return "bpmp"
            elif self == stock.STOCK.STOCK_BPMX:
                return "bpmx"
            elif self == stock.STOCK.STOCK_BPOP:
                return "bpop"
            elif self == stock.STOCK.STOCK_BPOPM:
                return "bpopm"
            elif self == stock.STOCK.STOCK_BPOPN:
                return "bpopn"
            elif self == stock.STOCK.STOCK_BPRN:
                return "bprn"
            elif self == stock.STOCK.STOCK_BPT:
                return "bpt"
            elif self == stock.STOCK.STOCK_BPTH:
                return "bpth"
            elif self == stock.STOCK.STOCK_BPY:
                return "bpy"
            elif self == stock.STOCK.STOCK_BQH:
                return "bqh"
            elif self == stock.STOCK.STOCK_BR:
                return "br"
            elif self == stock.STOCK.STOCK_BRAC:
                return "brac"
            elif self == stock.STOCK.STOCK_BRACR:
                return "bracr"
            elif self == stock.STOCK.STOCK_BRACU:
                return "bracu"
            elif self == stock.STOCK.STOCK_BRACW:
                return "bracw"
            elif self == stock.STOCK.STOCK_BRC:
                return "brc"
            elif self == stock.STOCK.STOCK_BRCD:
                return "brcd"
            elif self == stock.STOCK.STOCK_BREW:
                return "brew"
            elif self == stock.STOCK.STOCK_BRFS:
                return "brfs"
            elif self == stock.STOCK.STOCK_BRG:
                return "brg"
            elif self == stock.STOCK.STOCK_BRGL:
                return "brgl"
            elif self == stock.STOCK.STOCK_BRG_A:
                return "brg_a"
            elif self == stock.STOCK.STOCK_BRG_C:
                return "brg_c"
            elif self == stock.STOCK.STOCK_BRG_D:
                return "brg_d"
            elif self == stock.STOCK.STOCK_BRID:
                return "brid"
            elif self == stock.STOCK.STOCK_BRK-A:
                return "brk-a"
            elif self == stock.STOCK.STOCK_BRK-B:
                return "brk-b"
            elif self == stock.STOCK.STOCK_BRKL:
                return "brkl"
            elif self == stock.STOCK.STOCK_BRKR:
                return "brkr"
            elif self == stock.STOCK.STOCK_BRKS:
                return "brks"
            elif self == stock.STOCK.STOCK_BRN:
                return "brn"
            elif self == stock.STOCK.STOCK_BRO:
                return "bro"
            elif self == stock.STOCK.STOCK_BRQS:
                return "brqs"
            elif self == stock.STOCK.STOCK_BRQSW:
                return "brqsw"
            elif self == stock.STOCK.STOCK_BRS:
                return "brs"
            elif self == stock.STOCK.STOCK_BRSS:
                return "brss"
            elif self == stock.STOCK.STOCK_BRT:
                return "brt"
            elif self == stock.STOCK.STOCK_BRX:
                return "brx"
            elif self == stock.STOCK.STOCK_BSAC:
                return "bsac"
            elif self == stock.STOCK.STOCK_BSBR:
                return "bsbr"
            elif self == stock.STOCK.STOCK_BSCP:
                return "bscp"
            elif self == stock.STOCK.STOCK_BSCQ:
                return "bscq"
            elif self == stock.STOCK.STOCK_BSCR:
                return "bscr"
            elif self == stock.STOCK.STOCK_BSD:
                return "bsd"
            elif self == stock.STOCK.STOCK_BSE:
                return "bse"
            elif self == stock.STOCK.STOCK_BSET:
                return "bset"
            elif self == stock.STOCK.STOCK_BSF:
                return "bsf"
            elif self == stock.STOCK.STOCK_BSFT:
                return "bsft"
            elif self == stock.STOCK.STOCK_BSJN:
                return "bsjn"
            elif self == stock.STOCK.STOCK_BSJO:
                return "bsjo"
            elif self == stock.STOCK.STOCK_BSJP:
                return "bsjp"
            elif self == stock.STOCK.STOCK_BSL:
                return "bsl"
            elif self == stock.STOCK.STOCK_BSM:
                return "bsm"
            elif self == stock.STOCK.STOCK_BSMX:
                return "bsmx"
            elif self == stock.STOCK.STOCK_BSPM:
                return "bspm"
            elif self == stock.STOCK.STOCK_BSQR:
                return "bsqr"
            elif self == stock.STOCK.STOCK_BSRR:
                return "bsrr"
            elif self == stock.STOCK.STOCK_BST:
                return "bst"
            elif self == stock.STOCK.STOCK_BSTC:
                return "bstc"
            elif self == stock.STOCK.STOCK_BSTI:
                return "bsti"
            elif self == stock.STOCK.STOCK_BSWN:
                return "bswn"
            elif self == stock.STOCK.STOCK_BSX:
                return "bsx"
            elif self == stock.STOCK.STOCK_BT:
                return "bt"
            elif self == stock.STOCK.STOCK_BTA:
                return "bta"
            elif self == stock.STOCK.STOCK_BTE:
                return "bte"
            elif self == stock.STOCK.STOCK_BTEC:
                return "btec"
            elif self == stock.STOCK.STOCK_BTG:
                return "btg"
            elif self == stock.STOCK.STOCK_BTI:
                return "bti"
            elif self == stock.STOCK.STOCK_BTN:
                return "btn"
            elif self == stock.STOCK.STOCK_BTO:
                return "bto"
            elif self == stock.STOCK.STOCK_BTT:
                return "btt"
            elif self == stock.STOCK.STOCK_BTU:
                return "btu"
            elif self == stock.STOCK.STOCK_BTU_:
                return "btu_"
            elif self == stock.STOCK.STOCK_BTX-WS:
                return "btx-ws"
            elif self == stock.STOCK.STOCK_BTX:
                return "btx"
            elif self == stock.STOCK.STOCK_BTZ:
                return "btz"
            elif self == stock.STOCK.STOCK_BUD:
                return "bud"
            elif self == stock.STOCK.STOCK_BUFF:
                return "buff"
            elif self == stock.STOCK.STOCK_BUI:
                return "bui"
            elif self == stock.STOCK.STOCK_BUR:
                return "bur"
            elif self == stock.STOCK.STOCK_BURL:
                return "burl"
            elif self == stock.STOCK.STOCK_BUSE:
                return "buse"
            elif self == stock.STOCK.STOCK_BUZ:
                return "buz"
            elif self == stock.STOCK.STOCK_BV:
                return "bv"
            elif self == stock.STOCK.STOCK_BVAL:
                return "bval"
            elif self == stock.STOCK.STOCK_BVN:
                return "bvn"
            elif self == stock.STOCK.STOCK_BVSN:
                return "bvsn"
            elif self == stock.STOCK.STOCK_BVX:
                return "bvx"
            elif self == stock.STOCK.STOCK_BVXV:
                return "bvxv"
            elif self == stock.STOCK.STOCK_BVXVW:
                return "bvxvw"
            elif self == stock.STOCK.STOCK_BW:
                return "bw"
            elif self == stock.STOCK.STOCK_BWA:
                return "bwa"
            elif self == stock.STOCK.STOCK_BWEN:
                return "bwen"
            elif self == stock.STOCK.STOCK_BWFG:
                return "bwfg"
            elif self == stock.STOCK.STOCK_BWG:
                return "bwg"
            elif self == stock.STOCK.STOCK_BWINA:
                return "bwina"
            elif self == stock.STOCK.STOCK_BWINB:
                return "bwinb"
            elif self == stock.STOCK.STOCK_BWL-A:
                return "bwl-a"
            elif self == stock.STOCK.STOCK_BWLD:
                return "bwld"
            elif self == stock.STOCK.STOCK_BWP:
                return "bwp"
            elif self == stock.STOCK.STOCK_BWXT:
                return "bwxt"
            elif self == stock.STOCK.STOCK_BX:
                return "bx"
            elif self == stock.STOCK.STOCK_BXC:
                return "bxc"
            elif self == stock.STOCK.STOCK_BXE:
                return "bxe"
            elif self == stock.STOCK.STOCK_BXG:
                return "bxg"
            elif self == stock.STOCK.STOCK_BXMT:
                return "bxmt"
            elif self == stock.STOCK.STOCK_BXMX:
                return "bxmx"
            elif self == stock.STOCK.STOCK_BXP:
                return "bxp"
            elif self == stock.STOCK.STOCK_BXP_B:
                return "bxp_b"
            elif self == stock.STOCK.STOCK_BXS:
                return "bxs"
            elif self == stock.STOCK.STOCK_BY:
                return "by"
            elif self == stock.STOCK.STOCK_BYBK:
                return "bybk"
            elif self == stock.STOCK.STOCK_BYD:
                return "byd"
            elif self == stock.STOCK.STOCK_BYFC:
                return "byfc"
            elif self == stock.STOCK.STOCK_BYM:
                return "bym"
            elif self == stock.STOCK.STOCK_BYSI:
                return "bysi"
            elif self == stock.STOCK.STOCK_BZH:
                return "bzh"
            elif self == stock.STOCK.STOCK_BZM:
                return "bzm"
            elif self == stock.STOCK.STOCK_BZUN:
                return "bzun"
            elif self == stock.STOCK.STOCK_C-WS-A:
                return "c-ws-a"
            elif self == stock.STOCK.STOCK_C:
                return "c"
            elif self == stock.STOCK.STOCK_CA:
                return "ca"
            elif self == stock.STOCK.STOCK_CAA:
                return "caa"
            elif self == stock.STOCK.STOCK_CAAS:
                return "caas"
            elif self == stock.STOCK.STOCK_CABO:
                return "cabo"
            elif self == stock.STOCK.STOCK_CAC:
                return "cac"
            elif self == stock.STOCK.STOCK_CACC:
                return "cacc"
            elif self == stock.STOCK.STOCK_CACG:
                return "cacg"
            elif self == stock.STOCK.STOCK_CACI:
                return "caci"
            elif self == stock.STOCK.STOCK_CADC:
                return "cadc"
            elif self == stock.STOCK.STOCK_CADE:
                return "cade"
            elif self == stock.STOCK.STOCK_CAE:
                return "cae"
            elif self == stock.STOCK.STOCK_CAF:
                return "caf"
            elif self == stock.STOCK.STOCK_CAFD:
                return "cafd"
            elif self == stock.STOCK.STOCK_CAG:
                return "cag"
            elif self == stock.STOCK.STOCK_CAH:
                return "cah"
            elif self == stock.STOCK.STOCK_CAI:
                return "cai"
            elif self == stock.STOCK.STOCK_CAJ:
                return "caj"
            elif self == stock.STOCK.STOCK_CAKE:
                return "cake"
            elif self == stock.STOCK.STOCK_CAL:
                return "cal"
            elif self == stock.STOCK.STOCK_CALA:
                return "cala"
            elif self == stock.STOCK.STOCK_CALD:
                return "cald"
            elif self == stock.STOCK.STOCK_CALF:
                return "calf"
            elif self == stock.STOCK.STOCK_CALI:
                return "cali"
            elif self == stock.STOCK.STOCK_CALL:
                return "call"
            elif self == stock.STOCK.STOCK_CALM:
                return "calm"
            elif self == stock.STOCK.STOCK_CALX:
                return "calx"
            elif self == stock.STOCK.STOCK_CAMP:
                return "camp"
            elif self == stock.STOCK.STOCK_CAMT:
                return "camt"
            elif self == stock.STOCK.STOCK_CANF:
                return "canf"
            elif self == stock.STOCK.STOCK_CAPL:
                return "capl"
            elif self == stock.STOCK.STOCK_CAPR:
                return "capr"
            elif self == stock.STOCK.STOCK_CAR:
                return "car"
            elif self == stock.STOCK.STOCK_CARA:
                return "cara"
            elif self == stock.STOCK.STOCK_CARB:
                return "carb"
            elif self == stock.STOCK.STOCK_CARG:
                return "carg"
            elif self == stock.STOCK.STOCK_CARO:
                return "caro"
            elif self == stock.STOCK.STOCK_CARS:
                return "cars"
            elif self == stock.STOCK.STOCK_CART:
                return "cart"
            elif self == stock.STOCK.STOCK_CARV:
                return "carv"
            elif self == stock.STOCK.STOCK_CASC:
                return "casc"
            elif self == stock.STOCK.STOCK_CASH:
                return "cash"
            elif self == stock.STOCK.STOCK_CASI:
                return "casi"
            elif self == stock.STOCK.STOCK_CASM:
                return "casm"
            elif self == stock.STOCK.STOCK_CASS:
                return "cass"
            elif self == stock.STOCK.STOCK_CASY:
                return "casy"
            elif self == stock.STOCK.STOCK_CAT:
                return "cat"
            elif self == stock.STOCK.STOCK_CATB:
                return "catb"
            elif self == stock.STOCK.STOCK_CATC:
                return "catc"
            elif self == stock.STOCK.STOCK_CATH:
                return "cath"
            elif self == stock.STOCK.STOCK_CATM:
                return "catm"
            elif self == stock.STOCK.STOCK_CATO:
                return "cato"
            elif self == stock.STOCK.STOCK_CATS:
                return "cats"
            elif self == stock.STOCK.STOCK_CATY:
                return "caty"
            elif self == stock.STOCK.STOCK_CATYW:
                return "catyw"
            elif self == stock.STOCK.STOCK_CAVM:
                return "cavm"
            elif self == stock.STOCK.STOCK_CAW:
                return "caw"
            elif self == stock.STOCK.STOCK_CB:
                return "cb"
            elif self == stock.STOCK.STOCK_CBA:
                return "cba"
            elif self == stock.STOCK.STOCK_CBAK:
                return "cbak"
            elif self == stock.STOCK.STOCK_CBAN:
                return "cban"
            elif self == stock.STOCK.STOCK_CBAY:
                return "cbay"
            elif self == stock.STOCK.STOCK_CBB:
                return "cbb"
            elif self == stock.STOCK.STOCK_CBB_B:
                return "cbb_b"
            elif self == stock.STOCK.STOCK_CBD:
                return "cbd"
            elif self == stock.STOCK.STOCK_CBF:
                return "cbf"
            elif self == stock.STOCK.STOCK_CBFV:
                return "cbfv"
            elif self == stock.STOCK.STOCK_CBG:
                return "cbg"
            elif self == stock.STOCK.STOCK_CBH:
                return "cbh"
            elif self == stock.STOCK.STOCK_CBI:
                return "cbi"
            elif self == stock.STOCK.STOCK_CBIO:
                return "cbio"
            elif self == stock.STOCK.STOCK_CBK:
                return "cbk"
            elif self == stock.STOCK.STOCK_CBL:
                return "cbl"
            elif self == stock.STOCK.STOCK_CBLI:
                return "cbli"
            elif self == stock.STOCK.STOCK_CBL_D:
                return "cbl_d"
            elif self == stock.STOCK.STOCK_CBL_E:
                return "cbl_e"
            elif self == stock.STOCK.STOCK_CBM:
                return "cbm"
            elif self == stock.STOCK.STOCK_CBMG:
                return "cbmg"
            elif self == stock.STOCK.STOCK_CBMX:
                return "cbmx"
            elif self == stock.STOCK.STOCK_CBMXW:
                return "cbmxw"
            elif self == stock.STOCK.STOCK_CBO:
                return "cbo"
            elif self == stock.STOCK.STOCK_CBOE:
                return "cboe"
            elif self == stock.STOCK.STOCK_CBPO:
                return "cbpo"
            elif self == stock.STOCK.STOCK_CBPX:
                return "cbpx"
            elif self == stock.STOCK.STOCK_CBRL:
                return "cbrl"
            elif self == stock.STOCK.STOCK_CBS-A:
                return "cbs-a"
            elif self == stock.STOCK.STOCK_CBS:
                return "cbs"
            elif self == stock.STOCK.STOCK_CBSH:
                return "cbsh"
            elif self == stock.STOCK.STOCK_CBSHP:
                return "cbshp"
            elif self == stock.STOCK.STOCK_CBT:
                return "cbt"
            elif self == stock.STOCK.STOCK_CBTX:
                return "cbtx"
            elif self == stock.STOCK.STOCK_CBU:
                return "cbu"
            elif self == stock.STOCK.STOCK_CBX:
                return "cbx"
            elif self == stock.STOCK.STOCK_CBZ:
                return "cbz"
            elif self == stock.STOCK.STOCK_CC:
                return "cc"
            elif self == stock.STOCK.STOCK_CCA:
                return "cca"
            elif self == stock.STOCK.STOCK_CCBG:
                return "ccbg"
            elif self == stock.STOCK.STOCK_CCC:
                return "ccc"
            elif self == stock.STOCK.STOCK_CCCL:
                return "cccl"
            elif self == stock.STOCK.STOCK_CCCR:
                return "cccr"
            elif self == stock.STOCK.STOCK_CCD:
                return "ccd"
            elif self == stock.STOCK.STOCK_CCE:
                return "cce"
            elif self == stock.STOCK.STOCK_CCF:
                return "ccf"
            elif self == stock.STOCK.STOCK_CCI:
                return "cci"
            elif self == stock.STOCK.STOCK_CCIH:
                return "ccih"
            elif self == stock.STOCK.STOCK_CCI_A:
                return "cci_a"
            elif self == stock.STOCK.STOCK_CCJ:
                return "ccj"
            elif self == stock.STOCK.STOCK_CCK:
                return "cck"
            elif self == stock.STOCK.STOCK_CCL:
                return "ccl"
            elif self == stock.STOCK.STOCK_CCLP:
                return "cclp"
            elif self == stock.STOCK.STOCK_CCM:
                return "ccm"
            elif self == stock.STOCK.STOCK_CCMP:
                return "ccmp"
            elif self == stock.STOCK.STOCK_CCNE:
                return "ccne"
            elif self == stock.STOCK.STOCK_CCO:
                return "cco"
            elif self == stock.STOCK.STOCK_CCOI:
                return "ccoi"
            elif self == stock.STOCK.STOCK_CCOR:
                return "ccor"
            elif self == stock.STOCK.STOCK_CCRC:
                return "ccrc"
            elif self == stock.STOCK.STOCK_CCRN:
                return "ccrn"
            elif self == stock.STOCK.STOCK_CCS:
                return "ccs"
            elif self == stock.STOCK.STOCK_CCU:
                return "ccu"
            elif self == stock.STOCK.STOCK_CCUR:
                return "ccur"
            elif self == stock.STOCK.STOCK_CCV-CL:
                return "ccv-cl"
            elif self == stock.STOCK.STOCK_CCV:
                return "ccv"
            elif self == stock.STOCK.STOCK_CCXI:
                return "ccxi"
            elif self == stock.STOCK.STOCK_CCZ:
                return "ccz"
            elif self == stock.STOCK.STOCK_CDC:
                return "cdc"
            elif self == stock.STOCK.STOCK_CDE:
                return "cde"
            elif self == stock.STOCK.STOCK_CDEV:
                return "cdev"
            elif self == stock.STOCK.STOCK_CDK:
                return "cdk"
            elif self == stock.STOCK.STOCK_CDL:
                return "cdl"
            elif self == stock.STOCK.STOCK_CDNA:
                return "cdna"
            elif self == stock.STOCK.STOCK_CDNS:
                return "cdns"
            elif self == stock.STOCK.STOCK_CDOR:
                return "cdor"
            elif self == stock.STOCK.STOCK_CDR:
                return "cdr"
            elif self == stock.STOCK.STOCK_CDR_B:
                return "cdr_b"
            elif self == stock.STOCK.STOCK_CDR_C:
                return "cdr_c"
            elif self == stock.STOCK.STOCK_CDTI:
                return "cdti"
            elif self == stock.STOCK.STOCK_CDTX:
                return "cdtx"
            elif self == stock.STOCK.STOCK_CDW:
                return "cdw"
            elif self == stock.STOCK.STOCK_CDXC:
                return "cdxc"
            elif self == stock.STOCK.STOCK_CDXS:
                return "cdxs"
            elif self == stock.STOCK.STOCK_CDZI:
                return "cdzi"
            elif self == stock.STOCK.STOCK_CE:
                return "ce"
            elif self == stock.STOCK.STOCK_CEA:
                return "cea"
            elif self == stock.STOCK.STOCK_CECE:
                return "cece"
            elif self == stock.STOCK.STOCK_CECO:
                return "ceco"
            elif self == stock.STOCK.STOCK_CEE:
                return "cee"
            elif self == stock.STOCK.STOCK_CEF:
                return "cef"
            elif self == stock.STOCK.STOCK_CEFS:
                return "cefs"
            elif self == stock.STOCK.STOCK_CEI:
                return "cei"
            elif self == stock.STOCK.STOCK_CEL:
                return "cel"
            elif self == stock.STOCK.STOCK_CELC:
                return "celc"
            elif self == stock.STOCK.STOCK_CELG:
                return "celg"
            elif self == stock.STOCK.STOCK_CELGZ:
                return "celgz"
            elif self == stock.STOCK.STOCK_CELH:
                return "celh"
            elif self == stock.STOCK.STOCK_CELP:
                return "celp"
            elif self == stock.STOCK.STOCK_CEM:
                return "cem"
            elif self == stock.STOCK.STOCK_CEMB:
                return "cemb"
            elif self == stock.STOCK.STOCK_CEMI:
                return "cemi"
            elif self == stock.STOCK.STOCK_CEN:
                return "cen"
            elif self == stock.STOCK.STOCK_CENT:
                return "cent"
            elif self == stock.STOCK.STOCK_CENTA:
                return "centa"
            elif self == stock.STOCK.STOCK_CENX:
                return "cenx"
            elif self == stock.STOCK.STOCK_CEO:
                return "ceo"
            elif self == stock.STOCK.STOCK_CEQP:
                return "ceqp"
            elif self == stock.STOCK.STOCK_CERC:
                return "cerc"
            elif self == stock.STOCK.STOCK_CERCW:
                return "cercw"
            elif self == stock.STOCK.STOCK_CERN:
                return "cern"
            elif self == stock.STOCK.STOCK_CERS:
                return "cers"
            elif self == stock.STOCK.STOCK_CET:
                return "cet"
            elif self == stock.STOCK.STOCK_CETV:
                return "cetv"
            elif self == stock.STOCK.STOCK_CETX:
                return "cetx"
            elif self == stock.STOCK.STOCK_CETXP:
                return "cetxp"
            elif self == stock.STOCK.STOCK_CETXW:
                return "cetxw"
            elif self == stock.STOCK.STOCK_CEV:
                return "cev"
            elif self == stock.STOCK.STOCK_CEVA:
                return "ceva"
            elif self == stock.STOCK.STOCK_CEY:
                return "cey"
            elif self == stock.STOCK.STOCK_CEZ:
                return "cez"
            elif self == stock.STOCK.STOCK_CF:
                return "cf"
            elif self == stock.STOCK.STOCK_CFA:
                return "cfa"
            elif self == stock.STOCK.STOCK_CFBI:
                return "cfbi"
            elif self == stock.STOCK.STOCK_CFBK:
                return "cfbk"
            elif self == stock.STOCK.STOCK_CFCO:
                return "cfco"
            elif self == stock.STOCK.STOCK_CFCOU:
                return "cfcou"
            elif self == stock.STOCK.STOCK_CFCOW:
                return "cfcow"
            elif self == stock.STOCK.STOCK_CFC_B:
                return "cfc_b"
            elif self == stock.STOCK.STOCK_CFFI:
                return "cffi"
            elif self == stock.STOCK.STOCK_CFFN:
                return "cffn"
            elif self == stock.STOCK.STOCK_CFG:
                return "cfg"
            elif self == stock.STOCK.STOCK_CFMS:
                return "cfms"
            elif self == stock.STOCK.STOCK_CFNB:
                return "cfnb"
            elif self == stock.STOCK.STOCK_CFO:
                return "cfo"
            elif self == stock.STOCK.STOCK_CFR:
                return "cfr"
            elif self == stock.STOCK.STOCK_CFRX:
                return "cfrx"
            elif self == stock.STOCK.STOCK_CFR_A:
                return "cfr_a"
            elif self == stock.STOCK.STOCK_CFX:
                return "cfx"
            elif self == stock.STOCK.STOCK_CG:
                return "cg"
            elif self == stock.STOCK.STOCK_CGA:
                return "cga"
            elif self == stock.STOCK.STOCK_CGBD:
                return "cgbd"
            elif self == stock.STOCK.STOCK_CGEN:
                return "cgen"
            elif self == stock.STOCK.STOCK_CGG:
                return "cgg"
            elif self == stock.STOCK.STOCK_CGI:
                return "cgi"
            elif self == stock.STOCK.STOCK_CGIX:
                return "cgix"
            elif self == stock.STOCK.STOCK_CGNT:
                return "cgnt"
            elif self == stock.STOCK.STOCK_CGNX:
                return "cgnx"
            elif self == stock.STOCK.STOCK_CGO:
                return "cgo"
            elif self == stock.STOCK.STOCK_CH:
                return "ch"
            elif self == stock.STOCK.STOCK_CHA:
                return "cha"
            elif self == stock.STOCK.STOCK_CHAD:
                return "chad"
            elif self == stock.STOCK.STOCK_CHCI:
                return "chci"
            elif self == stock.STOCK.STOCK_CHCO:
                return "chco"
            elif self == stock.STOCK.STOCK_CHCT:
                return "chct"
            elif self == stock.STOCK.STOCK_CHD:
                return "chd"
            elif self == stock.STOCK.STOCK_CHDN:
                return "chdn"
            elif self == stock.STOCK.STOCK_CHE:
                return "che"
            elif self == stock.STOCK.STOCK_CHEF:
                return "chef"
            elif self == stock.STOCK.STOCK_CHEK:
                return "chek"
            elif self == stock.STOCK.STOCK_CHEKW:
                return "chekw"
            elif self == stock.STOCK.STOCK_CHFC:
                return "chfc"
            elif self == stock.STOCK.STOCK_CHFN:
                return "chfn"
            elif self == stock.STOCK.STOCK_CHFS:
                return "chfs"
            elif self == stock.STOCK.STOCK_CHGG:
                return "chgg"
            elif self == stock.STOCK.STOCK_CHGX:
                return "chgx"
            elif self == stock.STOCK.STOCK_CHH:
                return "chh"
            elif self == stock.STOCK.STOCK_CHI:
                return "chi"
            elif self == stock.STOCK.STOCK_CHK:
                return "chk"
            elif self == stock.STOCK.STOCK_CHKE:
                return "chke"
            elif self == stock.STOCK.STOCK_CHKP:
                return "chkp"
            elif self == stock.STOCK.STOCK_CHKR:
                return "chkr"
            elif self == stock.STOCK.STOCK_CHK_D:
                return "chk_d"
            elif self == stock.STOCK.STOCK_CHL:
                return "chl"
            elif self == stock.STOCK.STOCK_CHMA:
                return "chma"
            elif self == stock.STOCK.STOCK_CHMG:
                return "chmg"
            elif self == stock.STOCK.STOCK_CHMI:
                return "chmi"
            elif self == stock.STOCK.STOCK_CHMI_A:
                return "chmi_a"
            elif self == stock.STOCK.STOCK_CHN:
                return "chn"
            elif self == stock.STOCK.STOCK_CHNR:
                return "chnr"
            elif self == stock.STOCK.STOCK_CHRS:
                return "chrs"
            elif self == stock.STOCK.STOCK_CHRW:
                return "chrw"
            elif self == stock.STOCK.STOCK_CHS:
                return "chs"
            elif self == stock.STOCK.STOCK_CHSCL:
                return "chscl"
            elif self == stock.STOCK.STOCK_CHSCM:
                return "chscm"
            elif self == stock.STOCK.STOCK_CHSCN:
                return "chscn"
            elif self == stock.STOCK.STOCK_CHSCO:
                return "chsco"
            elif self == stock.STOCK.STOCK_CHSCP:
                return "chscp"
            elif self == stock.STOCK.STOCK_CHSP:
                return "chsp"
            elif self == stock.STOCK.STOCK_CHT:
                return "cht"
            elif self == stock.STOCK.STOCK_CHTR:
                return "chtr"
            elif self == stock.STOCK.STOCK_CHU:
                return "chu"
            elif self == stock.STOCK.STOCK_CHUBA:
                return "chuba"
            elif self == stock.STOCK.STOCK_CHUBK:
                return "chubk"
            elif self == stock.STOCK.STOCK_CHUY:
                return "chuy"
            elif self == stock.STOCK.STOCK_CHW:
                return "chw"
            elif self == stock.STOCK.STOCK_CHY:
                return "chy"
            elif self == stock.STOCK.STOCK_CI:
                return "ci"
            elif self == stock.STOCK.STOCK_CIA:
                return "cia"
            elif self == stock.STOCK.STOCK_CIB:
                return "cib"
            elif self == stock.STOCK.STOCK_CIBR:
                return "cibr"
            elif self == stock.STOCK.STOCK_CIC-U:
                return "cic-u"
            elif self == stock.STOCK.STOCK_CIC-WS:
                return "cic-ws"
            elif self == stock.STOCK.STOCK_CIC:
                return "cic"
            elif self == stock.STOCK.STOCK_CID:
                return "cid"
            elif self == stock.STOCK.STOCK_CIDM:
                return "cidm"
            elif self == stock.STOCK.STOCK_CIE:
                return "cie"
            elif self == stock.STOCK.STOCK_CIEN:
                return "cien"
            elif self == stock.STOCK.STOCK_CIF:
                return "cif"
            elif self == stock.STOCK.STOCK_CIFS:
                return "cifs"
            elif self == stock.STOCK.STOCK_CIG-C:
                return "cig-c"
            elif self == stock.STOCK.STOCK_CIG:
                return "cig"
            elif self == stock.STOCK.STOCK_CIGI:
                return "cigi"
            elif self == stock.STOCK.STOCK_CII:
                return "cii"
            elif self == stock.STOCK.STOCK_CIK:
                return "cik"
            elif self == stock.STOCK.STOCK_CIL:
                return "cil"
            elif self == stock.STOCK.STOCK_CIM:
                return "cim"
            elif self == stock.STOCK.STOCK_CIM_A:
                return "cim_a"
            elif self == stock.STOCK.STOCK_CIM_B:
                return "cim_b"
            elif self == stock.STOCK.STOCK_CINF:
                return "cinf"
            elif self == stock.STOCK.STOCK_CINR:
                return "cinr"
            elif self == stock.STOCK.STOCK_CIO:
                return "cio"
            elif self == stock.STOCK.STOCK_CIO_A:
                return "cio_a"
            elif self == stock.STOCK.STOCK_CIR:
                return "cir"
            elif self == stock.STOCK.STOCK_CISN-WS:
                return "cisn-ws"
            elif self == stock.STOCK.STOCK_CISN:
                return "cisn"
            elif self == stock.STOCK.STOCK_CIT:
                return "cit"
            elif self == stock.STOCK.STOCK_CIVB:
                return "civb"
            elif self == stock.STOCK.STOCK_CIVBP:
                return "civbp"
            elif self == stock.STOCK.STOCK_CIVI:
                return "civi"
            elif self == stock.STOCK.STOCK_CIX:
                return "cix"
            elif self == stock.STOCK.STOCK_CIZ:
                return "ciz"
            elif self == stock.STOCK.STOCK_CIZN:
                return "cizn"
            elif self == stock.STOCK.STOCK_CJ:
                return "cj"
            elif self == stock.STOCK.STOCK_CJJD:
                return "cjjd"
            elif self == stock.STOCK.STOCK_CKH:
                return "ckh"
            elif self == stock.STOCK.STOCK_CKPT:
                return "ckpt"
            elif self == stock.STOCK.STOCK_CKX:
                return "ckx"
            elif self == stock.STOCK.STOCK_CL:
                return "cl"
            elif self == stock.STOCK.STOCK_CLAR:
                return "clar"
            elif self == stock.STOCK.STOCK_CLB:
                return "clb"
            elif self == stock.STOCK.STOCK_CLBS:
                return "clbs"
            elif self == stock.STOCK.STOCK_CLCT:
                return "clct"
            elif self == stock.STOCK.STOCK_CLD:
                return "cld"
            elif self == stock.STOCK.STOCK_CLDC:
                return "cldc"
            elif self == stock.STOCK.STOCK_CLDR:
                return "cldr"
            elif self == stock.STOCK.STOCK_CLDT:
                return "cldt"
            elif self == stock.STOCK.STOCK_CLDX:
                return "cldx"
            elif self == stock.STOCK.STOCK_CLF:
                return "clf"
            elif self == stock.STOCK.STOCK_CLFD:
                return "clfd"
            elif self == stock.STOCK.STOCK_CLGX:
                return "clgx"
            elif self == stock.STOCK.STOCK_CLH:
                return "clh"
            elif self == stock.STOCK.STOCK_CLI:
                return "cli"
            elif self == stock.STOCK.STOCK_CLIR:
                return "clir"
            elif self == stock.STOCK.STOCK_CLIRW:
                return "clirw"
            elif self == stock.STOCK.STOCK_CLLS:
                return "clls"
            elif self == stock.STOCK.STOCK_CLM:
                return "clm"
            elif self == stock.STOCK.STOCK_CLMT:
                return "clmt"
            elif self == stock.STOCK.STOCK_CLNE:
                return "clne"
            elif self == stock.STOCK.STOCK_CLNS:
                return "clns"
            elif self == stock.STOCK.STOCK_CLNS_B:
                return "clns_b"
            elif self == stock.STOCK.STOCK_CLNS_C-CL:
                return "clns_c-cl"
            elif self == stock.STOCK.STOCK_CLNS_D:
                return "clns_d"
            elif self == stock.STOCK.STOCK_CLNS_E:
                return "clns_e"
            elif self == stock.STOCK.STOCK_CLNS_G:
                return "clns_g"
            elif self == stock.STOCK.STOCK_CLNS_H:
                return "clns_h"
            elif self == stock.STOCK.STOCK_CLNS_I:
                return "clns_i"
            elif self == stock.STOCK.STOCK_CLNS_J:
                return "clns_j"
            elif self == stock.STOCK.STOCK_CLNT:
                return "clnt"
            elif self == stock.STOCK.STOCK_CLPR:
                return "clpr"
            elif self == stock.STOCK.STOCK_CLR:
                return "clr"
            elif self == stock.STOCK.STOCK_CLRB:
                return "clrb"
            elif self == stock.STOCK.STOCK_CLRBW:
                return "clrbw"
            elif self == stock.STOCK.STOCK_CLRBZ:
                return "clrbz"
            elif self == stock.STOCK.STOCK_CLRO:
                return "clro"
            elif self == stock.STOCK.STOCK_CLS:
                return "cls"
            elif self == stock.STOCK.STOCK_CLSD:
                return "clsd"
            elif self == stock.STOCK.STOCK_CLSN:
                return "clsn"
            elif self == stock.STOCK.STOCK_CLTL:
                return "cltl"
            elif self == stock.STOCK.STOCK_CLUB:
                return "club"
            elif self == stock.STOCK.STOCK_CLVS:
                return "clvs"
            elif self == stock.STOCK.STOCK_CLW:
                return "clw"
            elif self == stock.STOCK.STOCK_CLWT:
                return "clwt"
            elif self == stock.STOCK.STOCK_CLX:
                return "clx"
            elif self == stock.STOCK.STOCK_CLXT:
                return "clxt"
            elif self == stock.STOCK.STOCK_CLYH:
                return "clyh"
            elif self == stock.STOCK.STOCK_CM:
                return "cm"
            elif self == stock.STOCK.STOCK_CMA-WS:
                return "cma-ws"
            elif self == stock.STOCK.STOCK_CMA:
                return "cma"
            elif self == stock.STOCK.STOCK_CMC:
                return "cmc"
            elif self == stock.STOCK.STOCK_CMCL:
                return "cmcl"
            elif self == stock.STOCK.STOCK_CMCM:
                return "cmcm"
            elif self == stock.STOCK.STOCK_CMCO:
                return "cmco"
            elif self == stock.STOCK.STOCK_CMCSA:
                return "cmcsa"
            elif self == stock.STOCK.STOCK_CMCT:
                return "cmct"
            elif self == stock.STOCK.STOCK_CMD:
                return "cmd"
            elif self == stock.STOCK.STOCK_CME:
                return "cme"
            elif self == stock.STOCK.STOCK_CMFN:
                return "cmfn"
            elif self == stock.STOCK.STOCK_CMG:
                return "cmg"
            elif self == stock.STOCK.STOCK_CMI:
                return "cmi"
            elif self == stock.STOCK.STOCK_CMLS:
                return "cmls"
            elif self == stock.STOCK.STOCK_CMO:
                return "cmo"
            elif self == stock.STOCK.STOCK_CMO_E:
                return "cmo_e"
            elif self == stock.STOCK.STOCK_CMP:
                return "cmp"
            elif self == stock.STOCK.STOCK_CMPR:
                return "cmpr"
            elif self == stock.STOCK.STOCK_CMRE:
                return "cmre"
            elif self == stock.STOCK.STOCK_CMRE_B:
                return "cmre_b"
            elif self == stock.STOCK.STOCK_CMRE_C:
                return "cmre_c"
            elif self == stock.STOCK.STOCK_CMRE_D:
                return "cmre_d"
            elif self == stock.STOCK.STOCK_CMRX:
                return "cmrx"
            elif self == stock.STOCK.STOCK_CMS:
                return "cms"
            elif self == stock.STOCK.STOCK_CMSS:
                return "cmss"
            elif self == stock.STOCK.STOCK_CMSSR:
                return "cmssr"
            elif self == stock.STOCK.STOCK_CMSSU:
                return "cmssu"
            elif self == stock.STOCK.STOCK_CMSSW:
                return "cmssw"
            elif self == stock.STOCK.STOCK_CMS_B:
                return "cms_b"
            elif self == stock.STOCK.STOCK_CMT:
                return "cmt"
            elif self == stock.STOCK.STOCK_CMTA:
                return "cmta"
            elif self == stock.STOCK.STOCK_CMTL:
                return "cmtl"
            elif self == stock.STOCK.STOCK_CMU:
                return "cmu"
            elif self == stock.STOCK.STOCK_CNA:
                return "cna"
            elif self == stock.STOCK.STOCK_CNAC:
                return "cnac"
            elif self == stock.STOCK.STOCK_CNACR:
                return "cnacr"
            elif self == stock.STOCK.STOCK_CNACU:
                return "cnacu"
            elif self == stock.STOCK.STOCK_CNACW:
                return "cnacw"
            elif self == stock.STOCK.STOCK_CNAT:
                return "cnat"
            elif self == stock.STOCK.STOCK_CNBKA:
                return "cnbka"
            elif self == stock.STOCK.STOCK_CNC:
                return "cnc"
            elif self == stock.STOCK.STOCK_CNCE:
                return "cnce"
            elif self == stock.STOCK.STOCK_CNCR:
                return "cncr"
            elif self == stock.STOCK.STOCK_CNDF:
                return "cndf"
            elif self == stock.STOCK.STOCK_CNDT:
                return "cndt"
            elif self == stock.STOCK.STOCK_CNET:
                return "cnet"
            elif self == stock.STOCK.STOCK_CNFR:
                return "cnfr"
            elif self == stock.STOCK.STOCK_CNHI:
                return "cnhi"
            elif self == stock.STOCK.STOCK_CNHX:
                return "cnhx"
            elif self == stock.STOCK.STOCK_CNI:
                return "cni"
            elif self == stock.STOCK.STOCK_CNIT:
                return "cnit"
            elif self == stock.STOCK.STOCK_CNK:
                return "cnk"
            elif self == stock.STOCK.STOCK_CNMD:
                return "cnmd"
            elif self == stock.STOCK.STOCK_CNNX:
                return "cnnx"
            elif self == stock.STOCK.STOCK_CNO:
                return "cno"
            elif self == stock.STOCK.STOCK_CNOB:
                return "cnob"
            elif self == stock.STOCK.STOCK_CNP:
                return "cnp"
            elif self == stock.STOCK.STOCK_CNQ:
                return "cnq"
            elif self == stock.STOCK.STOCK_CNS:
                return "cns"
            elif self == stock.STOCK.STOCK_CNSF:
                return "cnsf"
            elif self == stock.STOCK.STOCK_CNSL:
                return "cnsl"
            elif self == stock.STOCK.STOCK_CNTF:
                return "cntf"
            elif self == stock.STOCK.STOCK_CNTY:
                return "cnty"
            elif self == stock.STOCK.STOCK_CNX:
                return "cnx"
            elif self == stock.STOCK.STOCK_CNXC:
                return "cnxc"
            elif self == stock.STOCK.STOCK_CNXN:
                return "cnxn"
            elif self == stock.STOCK.STOCK_CNXR:
                return "cnxr"
            elif self == stock.STOCK.STOCK_CNYA:
                return "cnya"
            elif self == stock.STOCK.STOCK_CO:
                return "co"
            elif self == stock.STOCK.STOCK_COBZ:
                return "cobz"
            elif self == stock.STOCK.STOCK_CODA:
                return "coda"
            elif self == stock.STOCK.STOCK_CODI:
                return "codi"
            elif self == stock.STOCK.STOCK_CODI_A:
                return "codi_a"
            elif self == stock.STOCK.STOCK_CODX:
                return "codx"
            elif self == stock.STOCK.STOCK_COE:
                return "coe"
            elif self == stock.STOCK.STOCK_COF-WS:
                return "cof-ws"
            elif self == stock.STOCK.STOCK_COF:
                return "cof"
            elif self == stock.STOCK.STOCK_COF_C:
                return "cof_c"
            elif self == stock.STOCK.STOCK_COF_D:
                return "cof_d"
            elif self == stock.STOCK.STOCK_COF_F:
                return "cof_f"
            elif self == stock.STOCK.STOCK_COF_G:
                return "cof_g"
            elif self == stock.STOCK.STOCK_COF_H:
                return "cof_h"
            elif self == stock.STOCK.STOCK_COF_P:
                return "cof_p"
            elif self == stock.STOCK.STOCK_COG:
                return "cog"
            elif self == stock.STOCK.STOCK_COGT:
                return "cogt"
            elif self == stock.STOCK.STOCK_COHN:
                return "cohn"
            elif self == stock.STOCK.STOCK_COHR:
                return "cohr"
            elif self == stock.STOCK.STOCK_COHU:
                return "cohu"
            elif self == stock.STOCK.STOCK_COKE:
                return "coke"
            elif self == stock.STOCK.STOCK_COL:
                return "col"
            elif self == stock.STOCK.STOCK_COLB:
                return "colb"
            elif self == stock.STOCK.STOCK_COLL:
                return "coll"
            elif self == stock.STOCK.STOCK_COLM:
                return "colm"
            elif self == stock.STOCK.STOCK_COM:
                return "com"
            elif self == stock.STOCK.STOCK_COMB:
                return "comb"
            elif self == stock.STOCK.STOCK_COMG:
                return "comg"
            elif self == stock.STOCK.STOCK_COMM:
                return "comm"
            elif self == stock.STOCK.STOCK_CONE:
                return "cone"
            elif self == stock.STOCK.STOCK_CONN:
                return "conn"
            elif self == stock.STOCK.STOCK_COO:
                return "coo"
            elif self == stock.STOCK.STOCK_COOL:
                return "cool"
            elif self == stock.STOCK.STOCK_COP:
                return "cop"
            elif self == stock.STOCK.STOCK_COR:
                return "cor"
            elif self == stock.STOCK.STOCK_CORE:
                return "core"
            elif self == stock.STOCK.STOCK_CORI:
                return "cori"
            elif self == stock.STOCK.STOCK_CORR:
                return "corr"
            elif self == stock.STOCK.STOCK_CORR_A:
                return "corr_a"
            elif self == stock.STOCK.STOCK_CORT:
                return "cort"
            elif self == stock.STOCK.STOCK_COR_A-CL:
                return "cor_a-cl"
            elif self == stock.STOCK.STOCK_COR_A:
                return "cor_a"
            elif self == stock.STOCK.STOCK_COST:
                return "cost"
            elif self == stock.STOCK.STOCK_COT:
                return "cot"
            elif self == stock.STOCK.STOCK_COTV:
                return "cotv"
            elif self == stock.STOCK.STOCK_COTY:
                return "coty"
            elif self == stock.STOCK.STOCK_COUP:
                return "coup"
            elif self == stock.STOCK.STOCK_COWN:
                return "cown"
            elif self == stock.STOCK.STOCK_COWNL:
                return "cownl"
            elif self == stock.STOCK.STOCK_COWZ:
                return "cowz"
            elif self == stock.STOCK.STOCK_CP:
                return "cp"
            elif self == stock.STOCK.STOCK_CPA:
                return "cpa"
            elif self == stock.STOCK.STOCK_CPAC:
                return "cpac"
            elif self == stock.STOCK.STOCK_CPAH:
                return "cpah"
            elif self == stock.STOCK.STOCK_CPB:
                return "cpb"
            elif self == stock.STOCK.STOCK_CPE:
                return "cpe"
            elif self == stock.STOCK.STOCK_CPE_A:
                return "cpe_a"
            elif self == stock.STOCK.STOCK_CPF:
                return "cpf"
            elif self == stock.STOCK.STOCK_CPG:
                return "cpg"
            elif self == stock.STOCK.STOCK_CPHC:
                return "cphc"
            elif self == stock.STOCK.STOCK_CPHI:
                return "cphi"
            elif self == stock.STOCK.STOCK_CPIX:
                return "cpix"
            elif self == stock.STOCK.STOCK_CPK:
                return "cpk"
            elif self == stock.STOCK.STOCK_CPL:
                return "cpl"
            elif self == stock.STOCK.STOCK_CPLA:
                return "cpla"
            elif self == stock.STOCK.STOCK_CPLP:
                return "cplp"
            elif self == stock.STOCK.STOCK_CPN:
                return "cpn"
            elif self == stock.STOCK.STOCK_CPRT:
                return "cprt"
            elif self == stock.STOCK.STOCK_CPRX:
                return "cprx"
            elif self == stock.STOCK.STOCK_CPS:
                return "cps"
            elif self == stock.STOCK.STOCK_CPSH:
                return "cpsh"
            elif self == stock.STOCK.STOCK_CPSI:
                return "cpsi"
            elif self == stock.STOCK.STOCK_CPSS:
                return "cpss"
            elif self == stock.STOCK.STOCK_CPST:
                return "cpst"
            elif self == stock.STOCK.STOCK_CPT:
                return "cpt"
            elif self == stock.STOCK.STOCK_CPTA:
                return "cpta"
            elif self == stock.STOCK.STOCK_CPTAG:
                return "cptag"
            elif self == stock.STOCK.STOCK_CPTAL:
                return "cptal"
            elif self == stock.STOCK.STOCK_CQH:
                return "cqh"
            elif self == stock.STOCK.STOCK_CQP:
                return "cqp"
            elif self == stock.STOCK.STOCK_CR:
                return "cr"
            elif self == stock.STOCK.STOCK_CRAI:
                return "crai"
            elif self == stock.STOCK.STOCK_CRAK:
                return "crak"
            elif self == stock.STOCK.STOCK_CRAY:
                return "cray"
            elif self == stock.STOCK.STOCK_CRBP:
                return "crbp"
            elif self == stock.STOCK.STOCK_CRC:
                return "crc"
            elif self == stock.STOCK.STOCK_CRCM:
                return "crcm"
            elif self == stock.STOCK.STOCK_CRD-A:
                return "crd-a"
            elif self == stock.STOCK.STOCK_CRD-B:
                return "crd-b"
            elif self == stock.STOCK.STOCK_CREE:
                return "cree"
            elif self == stock.STOCK.STOCK_CREG:
                return "creg"
            elif self == stock.STOCK.STOCK_CRESY:
                return "cresy"
            elif self == stock.STOCK.STOCK_CRF:
                return "crf"
            elif self == stock.STOCK.STOCK_CRH:
                return "crh"
            elif self == stock.STOCK.STOCK_CRHM:
                return "crhm"
            elif self == stock.STOCK.STOCK_CRI:
                return "cri"
            elif self == stock.STOCK.STOCK_CRIS:
                return "cris"
            elif self == stock.STOCK.STOCK_CRK:
                return "crk"
            elif self == stock.STOCK.STOCK_CRL:
                return "crl"
            elif self == stock.STOCK.STOCK_CRM:
                return "crm"
            elif self == stock.STOCK.STOCK_CRMD:
                return "crmd"
            elif self == stock.STOCK.STOCK_CRME:
                return "crme"
            elif self == stock.STOCK.STOCK_CRMT:
                return "crmt"
            elif self == stock.STOCK.STOCK_CRNT:
                return "crnt"
            elif self == stock.STOCK.STOCK_CROX:
                return "crox"
            elif self == stock.STOCK.STOCK_CRR:
                return "crr"
            elif self == stock.STOCK.STOCK_CRS:
                return "crs"
            elif self == stock.STOCK.STOCK_CRSP:
                return "crsp"
            elif self == stock.STOCK.STOCK_CRT:
                return "crt"
            elif self == stock.STOCK.STOCK_CRTN:
                return "crtn"
            elif self == stock.STOCK.STOCK_CRTO:
                return "crto"
            elif self == stock.STOCK.STOCK_CRUS:
                return "crus"
            elif self == stock.STOCK.STOCK_CRVL:
                return "crvl"
            elif self == stock.STOCK.STOCK_CRVP:
                return "crvp"
            elif self == stock.STOCK.STOCK_CRVS:
                return "crvs"
            elif self == stock.STOCK.STOCK_CRWS:
                return "crws"
            elif self == stock.STOCK.STOCK_CRY:
                return "cry"
            elif self == stock.STOCK.STOCK_CRZO:
                return "crzo"
            elif self == stock.STOCK.STOCK_CS:
                return "cs"
            elif self == stock.STOCK.STOCK_CSA:
                return "csa"
            elif self == stock.STOCK.STOCK_CSB:
                return "csb"
            elif self == stock.STOCK.STOCK_CSBK:
                return "csbk"
            elif self == stock.STOCK.STOCK_CSBR:
                return "csbr"
            elif self == stock.STOCK.STOCK_CSCO:
                return "csco"
            elif self == stock.STOCK.STOCK_CSF:
                return "csf"
            elif self == stock.STOCK.STOCK_CSFL:
                return "csfl"
            elif self == stock.STOCK.STOCK_CSGP:
                return "csgp"
            elif self == stock.STOCK.STOCK_CSGS:
                return "csgs"
            elif self == stock.STOCK.STOCK_CSII:
                return "csii"
            elif self == stock.STOCK.STOCK_CSIQ:
                return "csiq"
            elif self == stock.STOCK.STOCK_CSL:
                return "csl"
            elif self == stock.STOCK.STOCK_CSLT:
                return "cslt"
            elif self == stock.STOCK.STOCK_CSML:
                return "csml"
            elif self == stock.STOCK.STOCK_CSOD:
                return "csod"
            elif self == stock.STOCK.STOCK_CSPI:
                return "cspi"
            elif self == stock.STOCK.STOCK_CSQ:
                return "csq"
            elif self == stock.STOCK.STOCK_CSRA:
                return "csra"
            elif self == stock.STOCK.STOCK_CSS:
                return "css"
            elif self == stock.STOCK.STOCK_CSSE:
                return "csse"
            elif self == stock.STOCK.STOCK_CSTE:
                return "cste"
            elif self == stock.STOCK.STOCK_CSTM:
                return "cstm"
            elif self == stock.STOCK.STOCK_CSTR:
                return "cstr"
            elif self == stock.STOCK.STOCK_CSU:
                return "csu"
            elif self == stock.STOCK.STOCK_CSV:
                return "csv"
            elif self == stock.STOCK.STOCK_CSWC:
                return "cswc"
            elif self == stock.STOCK.STOCK_CSWI:
                return "cswi"
            elif self == stock.STOCK.STOCK_CSX:
                return "csx"
            elif self == stock.STOCK.STOCK_CTAA:
                return "ctaa"
            elif self == stock.STOCK.STOCK_CTAS:
                return "ctas"
            elif self == stock.STOCK.STOCK_CTB:
                return "ctb"
            elif self == stock.STOCK.STOCK_CTBB:
                return "ctbb"
            elif self == stock.STOCK.STOCK_CTBI:
                return "ctbi"
            elif self == stock.STOCK.STOCK_CTDD:
                return "ctdd"
            elif self == stock.STOCK.STOCK_CTEK:
                return "ctek"
            elif self == stock.STOCK.STOCK_CTG:
                return "ctg"
            elif self == stock.STOCK.STOCK_CTHR:
                return "cthr"
            elif self == stock.STOCK.STOCK_CTIB:
                return "ctib"
            elif self == stock.STOCK.STOCK_CTIC:
                return "ctic"
            elif self == stock.STOCK.STOCK_CTL:
                return "ctl"
            elif self == stock.STOCK.STOCK_CTLT:
                return "ctlt"
            elif self == stock.STOCK.STOCK_CTMX:
                return "ctmx"
            elif self == stock.STOCK.STOCK_CTO:
                return "cto"
            elif self == stock.STOCK.STOCK_CTR:
                return "ctr"
            elif self == stock.STOCK.STOCK_CTRE:
                return "ctre"
            elif self == stock.STOCK.STOCK_CTRL:
                return "ctrl"
            elif self == stock.STOCK.STOCK_CTRN:
                return "ctrn"
            elif self == stock.STOCK.STOCK_CTRP:
                return "ctrp"
            elif self == stock.STOCK.STOCK_CTRV:
                return "ctrv"
            elif self == stock.STOCK.STOCK_CTS:
                return "cts"
            elif self == stock.STOCK.STOCK_CTSH:
                return "ctsh"
            elif self == stock.STOCK.STOCK_CTSO:
                return "ctso"
            elif self == stock.STOCK.STOCK_CTT:
                return "ctt"
            elif self == stock.STOCK.STOCK_CTU:
                return "ctu"
            elif self == stock.STOCK.STOCK_CTV:
                return "ctv"
            elif self == stock.STOCK.STOCK_CTW:
                return "ctw"
            elif self == stock.STOCK.STOCK_CTWS:
                return "ctws"
            elif self == stock.STOCK.STOCK_CTX:
                return "ctx"
            elif self == stock.STOCK.STOCK_CTXR:
                return "ctxr"
            elif self == stock.STOCK.STOCK_CTXRW:
                return "ctxrw"
            elif self == stock.STOCK.STOCK_CTXS:
                return "ctxs"
            elif self == stock.STOCK.STOCK_CTY:
                return "cty"
            elif self == stock.STOCK.STOCK_CTZ:
                return "ctz"
            elif self == stock.STOCK.STOCK_CUB:
                return "cub"
            elif self == stock.STOCK.STOCK_CUBA:
                return "cuba"
            elif self == stock.STOCK.STOCK_CUBE:
                return "cube"
            elif self == stock.STOCK.STOCK_CUBI:
                return "cubi"
            elif self == stock.STOCK.STOCK_CUBI_C:
                return "cubi_c"
            elif self == stock.STOCK.STOCK_CUBI_D:
                return "cubi_d"
            elif self == stock.STOCK.STOCK_CUBI_E:
                return "cubi_e"
            elif self == stock.STOCK.STOCK_CUBI_F:
                return "cubi_f"
            elif self == stock.STOCK.STOCK_CUBN:
                return "cubn"
            elif self == stock.STOCK.STOCK_CUBS:
                return "cubs"
            elif self == stock.STOCK.STOCK_CUDA:
                return "cuda"
            elif self == stock.STOCK.STOCK_CUI:
                return "cui"
            elif self == stock.STOCK.STOCK_CUK:
                return "cuk"
            elif self == stock.STOCK.STOCK_CULP:
                return "culp"
            elif self == stock.STOCK.STOCK_CUMB:
                return "cumb"
            elif self == stock.STOCK.STOCK_CUNB:
                return "cunb"
            elif self == stock.STOCK.STOCK_CUO:
                return "cuo"
            elif self == stock.STOCK.STOCK_CUR:
                return "cur"
            elif self == stock.STOCK.STOCK_CUTR:
                return "cutr"
            elif self == stock.STOCK.STOCK_CUZ:
                return "cuz"
            elif self == stock.STOCK.STOCK_CVA:
                return "cva"
            elif self == stock.STOCK.STOCK_CVBF:
                return "cvbf"
            elif self == stock.STOCK.STOCK_CVCO:
                return "cvco"
            elif self == stock.STOCK.STOCK_CVCY:
                return "cvcy"
            elif self == stock.STOCK.STOCK_CVE:
                return "cve"
            elif self == stock.STOCK.STOCK_CVEO:
                return "cveo"
            elif self == stock.STOCK.STOCK_CVG:
                return "cvg"
            elif self == stock.STOCK.STOCK_CVGI:
                return "cvgi"
            elif self == stock.STOCK.STOCK_CVGW:
                return "cvgw"
            elif self == stock.STOCK.STOCK_CVI:
                return "cvi"
            elif self == stock.STOCK.STOCK_CVLT:
                return "cvlt"
            elif self == stock.STOCK.STOCK_CVLY:
                return "cvly"
            elif self == stock.STOCK.STOCK_CVM-WS:
                return "cvm-ws"
            elif self == stock.STOCK.STOCK_CVM:
                return "cvm"
            elif self == stock.STOCK.STOCK_CVNA:
                return "cvna"
            elif self == stock.STOCK.STOCK_CVO:
                return "cvo"
            elif self == stock.STOCK.STOCK_CVR:
                return "cvr"
            elif self == stock.STOCK.STOCK_CVRR:
                return "cvrr"
            elif self == stock.STOCK.STOCK_CVRS:
                return "cvrs"
            elif self == stock.STOCK.STOCK_CVS:
                return "cvs"
            elif self == stock.STOCK.STOCK_CVTI:
                return "cvti"
            elif self == stock.STOCK.STOCK_CVU:
                return "cvu"
            elif self == stock.STOCK.STOCK_CVV:
                return "cvv"
            elif self == stock.STOCK.STOCK_CVX:
                return "cvx"
            elif self == stock.STOCK.STOCK_CW:
                return "cw"
            elif self == stock.STOCK.STOCK_CWAI:
                return "cwai"
            elif self == stock.STOCK.STOCK_CWAY:
                return "cway"
            elif self == stock.STOCK.STOCK_CWBC:
                return "cwbc"
            elif self == stock.STOCK.STOCK_CWCO:
                return "cwco"
            elif self == stock.STOCK.STOCK_CWEB:
                return "cweb"
            elif self == stock.STOCK.STOCK_CWH:
                return "cwh"
            elif self == stock.STOCK.STOCK_CWS:
                return "cws"
            elif self == stock.STOCK.STOCK_CWST:
                return "cwst"
            elif self == stock.STOCK.STOCK_CWT:
                return "cwt"
            elif self == stock.STOCK.STOCK_CX:
                return "cx"
            elif self == stock.STOCK.STOCK_CXDC:
                return "cxdc"
            elif self == stock.STOCK.STOCK_CXE:
                return "cxe"
            elif self == stock.STOCK.STOCK_CXH:
                return "cxh"
            elif self == stock.STOCK.STOCK_CXO:
                return "cxo"
            elif self == stock.STOCK.STOCK_CXP:
                return "cxp"
            elif self == stock.STOCK.STOCK_CXRX:
                return "cxrx"
            elif self == stock.STOCK.STOCK_CXSE:
                return "cxse"
            elif self == stock.STOCK.STOCK_CXW:
                return "cxw"
            elif self == stock.STOCK.STOCK_CY:
                return "cy"
            elif self == stock.STOCK.STOCK_CYAD:
                return "cyad"
            elif self == stock.STOCK.STOCK_CYAN:
                return "cyan"
            elif self == stock.STOCK.STOCK_CYBE:
                return "cybe"
            elif self == stock.STOCK.STOCK_CYBR:
                return "cybr"
            elif self == stock.STOCK.STOCK_CYCC:
                return "cycc"
            elif self == stock.STOCK.STOCK_CYCCP:
                return "cyccp"
            elif self == stock.STOCK.STOCK_CYD:
                return "cyd"
            elif self == stock.STOCK.STOCK_CYH:
                return "cyh"
            elif self == stock.STOCK.STOCK_CYHHZ:
                return "cyhhz"
            elif self == stock.STOCK.STOCK_CYOU:
                return "cyou"
            elif self == stock.STOCK.STOCK_CYRN:
                return "cyrn"
            elif self == stock.STOCK.STOCK_CYRX:
                return "cyrx"
            elif self == stock.STOCK.STOCK_CYRXW:
                return "cyrxw"
            elif self == stock.STOCK.STOCK_CYS:
                return "cys"
            elif self == stock.STOCK.STOCK_CYS_A:
                return "cys_a"
            elif self == stock.STOCK.STOCK_CYS_B:
                return "cys_b"
            elif self == stock.STOCK.STOCK_CYTK:
                return "cytk"
            elif self == stock.STOCK.STOCK_CYTR:
                return "cytr"
            elif self == stock.STOCK.STOCK_CYTX:
                return "cytx"
            elif self == stock.STOCK.STOCK_CYTXW:
                return "cytxw"
            elif self == stock.STOCK.STOCK_CZFC:
                return "czfc"
            elif self == stock.STOCK.STOCK_CZNC:
                return "cznc"
            elif self == stock.STOCK.STOCK_CZR:
                return "czr"
            elif self == stock.STOCK.STOCK_CZWI:
                return "czwi"
            elif self == stock.STOCK.STOCK_CZZ:
                return "czz"
            elif self == stock.STOCK.STOCK_C_C:
                return "c_c"
            elif self == stock.STOCK.STOCK_C_J:
                return "c_j"
            elif self == stock.STOCK.STOCK_C_K:
                return "c_k"
            elif self == stock.STOCK.STOCK_C_L:
                return "c_l"
            elif self == stock.STOCK.STOCK_C_N:
                return "c_n"
            elif self == stock.STOCK.STOCK_C_P:
                return "c_p"
            elif self == stock.STOCK.STOCK_C_S:
                return "c_s"
            elif self == stock.STOCK.STOCK_D:
                return "d"
            elif self == stock.STOCK.STOCK_DAC:
                return "dac"
            elif self == stock.STOCK.STOCK_DAIO:
                return "daio"
            elif self == stock.STOCK.STOCK_DAKT:
                return "dakt"
            elif self == stock.STOCK.STOCK_DAL:
                return "dal"
            elif self == stock.STOCK.STOCK_DALT:
                return "dalt"
            elif self == stock.STOCK.STOCK_DAN:
                return "dan"
            elif self == stock.STOCK.STOCK_DAR:
                return "dar"
            elif self == stock.STOCK.STOCK_DARE:
                return "dare"
            elif self == stock.STOCK.STOCK_DATA:
                return "data"
            elif self == stock.STOCK.STOCK_DAVE:
                return "dave"
            elif self == stock.STOCK.STOCK_DAX:
                return "dax"
            elif self == stock.STOCK.STOCK_DB:
                return "db"
            elif self == stock.STOCK.STOCK_DBD:
                return "dbd"
            elif self == stock.STOCK.STOCK_DBES:
                return "dbes"
            elif self == stock.STOCK.STOCK_DBIT:
                return "dbit"
            elif self == stock.STOCK.STOCK_DBL:
                return "dbl"
            elif self == stock.STOCK.STOCK_DBRT:
                return "dbrt"
            elif self == stock.STOCK.STOCK_DBVT:
                return "dbvt"
            elif self == stock.STOCK.STOCK_DCF:
                return "dcf"
            elif self == stock.STOCK.STOCK_DCI:
                return "dci"
            elif self == stock.STOCK.STOCK_DCIX:
                return "dcix"
            elif self == stock.STOCK.STOCK_DCM:
                return "dcm"
            elif self == stock.STOCK.STOCK_DCO:
                return "dco"
            elif self == stock.STOCK.STOCK_DCOM:
                return "dcom"
            elif self == stock.STOCK.STOCK_DCP:
                return "dcp"
            elif self == stock.STOCK.STOCK_DCPH:
                return "dcph"
            elif self == stock.STOCK.STOCK_DCT:
                return "dct"
            elif self == stock.STOCK.STOCK_DCUD:
                return "dcud"
            elif self == stock.STOCK.STOCK_DD:
                return "dd"
            elif self == stock.STOCK.STOCK_DDBI:
                return "ddbi"
            elif self == stock.STOCK.STOCK_DDC:
                return "ddc"
            elif self == stock.STOCK.STOCK_DDD:
                return "ddd"
            elif self == stock.STOCK.STOCK_DDE:
                return "dde"
            elif self == stock.STOCK.STOCK_DDEZ:
                return "ddez"
            elif self == stock.STOCK.STOCK_DDF:
                return "ddf"
            elif self == stock.STOCK.STOCK_DDJP:
                return "ddjp"
            elif self == stock.STOCK.STOCK_DDLS:
                return "ddls"
            elif self == stock.STOCK.STOCK_DDR:
                return "ddr"
            elif self == stock.STOCK.STOCK_DDR_A:
                return "ddr_a"
            elif self == stock.STOCK.STOCK_DDR_J:
                return "ddr_j"
            elif self == stock.STOCK.STOCK_DDR_K:
                return "ddr_k"
            elif self == stock.STOCK.STOCK_DDS:
                return "dds"
            elif self == stock.STOCK.STOCK_DDT:
                return "ddt"
            elif self == stock.STOCK.STOCK_DDWM:
                return "ddwm"
            elif self == stock.STOCK.STOCK_DD_A:
                return "dd_a"
            elif self == stock.STOCK.STOCK_DD_B:
                return "dd_b"
            elif self == stock.STOCK.STOCK_DE:
                return "de"
            elif self == stock.STOCK.STOCK_DEA:
                return "dea"
            elif self == stock.STOCK.STOCK_DECK:
                return "deck"
            elif self == stock.STOCK.STOCK_DEEF:
                return "deef"
            elif self == stock.STOCK.STOCK_DEFA:
                return "defa"
            elif self == stock.STOCK.STOCK_DEI:
                return "dei"
            elif self == stock.STOCK.STOCK_DEL:
                return "del"
            elif self == stock.STOCK.STOCK_DELT:
                return "delt"
            elif self == stock.STOCK.STOCK_DELTW:
                return "deltw"
            elif self == stock.STOCK.STOCK_DEMG:
                return "demg"
            elif self == stock.STOCK.STOCK_DEMS:
                return "dems"
            elif self == stock.STOCK.STOCK_DENN:
                return "denn"
            elif self == stock.STOCK.STOCK_DEO:
                return "deo"
            elif self == stock.STOCK.STOCK_DEPO:
                return "depo"
            elif self == stock.STOCK.STOCK_DERM:
                return "derm"
            elif self == stock.STOCK.STOCK_DESC:
                return "desc"
            elif self == stock.STOCK.STOCK_DESP:
                return "desp"
            elif self == stock.STOCK.STOCK_DEST:
                return "dest"
            elif self == stock.STOCK.STOCK_DEUS:
                return "deus"
            elif self == stock.STOCK.STOCK_DEWJ:
                return "dewj"
            elif self == stock.STOCK.STOCK_DEX:
                return "dex"
            elif self == stock.STOCK.STOCK_DEZU:
                return "dezu"
            elif self == stock.STOCK.STOCK_DF:
                return "df"
            elif self == stock.STOCK.STOCK_DFBG:
                return "dfbg"
            elif self == stock.STOCK.STOCK_DFEN:
                return "dfen"
            elif self == stock.STOCK.STOCK_DFFN:
                return "dffn"
            elif self == stock.STOCK.STOCK_DFIN:
                return "dfin"
            elif self == stock.STOCK.STOCK_DFND:
                return "dfnd"
            elif self == stock.STOCK.STOCK_DFNL:
                return "dfnl"
            elif self == stock.STOCK.STOCK_DFP:
                return "dfp"
            elif self == stock.STOCK.STOCK_DFRG:
                return "dfrg"
            elif self == stock.STOCK.STOCK_DFS:
                return "dfs"
            elif self == stock.STOCK.STOCK_DFS_B-CL:
                return "dfs_b-cl"
            elif self == stock.STOCK.STOCK_DFS_B:
                return "dfs_b"
            elif self == stock.STOCK.STOCK_DFVL:
                return "dfvl"
            elif self == stock.STOCK.STOCK_DFVS:
                return "dfvs"
            elif self == stock.STOCK.STOCK_DG:
                return "dg"
            elif self == stock.STOCK.STOCK_DGICA:
                return "dgica"
            elif self == stock.STOCK.STOCK_DGICB:
                return "dgicb"
            elif self == stock.STOCK.STOCK_DGII:
                return "dgii"
            elif self == stock.STOCK.STOCK_DGLT:
                return "dglt"
            elif self == stock.STOCK.STOCK_DGLY:
                return "dgly"
            elif self == stock.STOCK.STOCK_DGSE:
                return "dgse"
            elif self == stock.STOCK.STOCK_DGX:
                return "dgx"
            elif self == stock.STOCK.STOCK_DHDG:
                return "dhdg"
            elif self == stock.STOCK.STOCK_DHF:
                return "dhf"
            elif self == stock.STOCK.STOCK_DHG:
                return "dhg"
            elif self == stock.STOCK.STOCK_DHI:
                return "dhi"
            elif self == stock.STOCK.STOCK_DHIL:
                return "dhil"
            elif self == stock.STOCK.STOCK_DHR:
                return "dhr"
            elif self == stock.STOCK.STOCK_DHT:
                return "dht"
            elif self == stock.STOCK.STOCK_DHVW:
                return "dhvw"
            elif self == stock.STOCK.STOCK_DHX:
                return "dhx"
            elif self == stock.STOCK.STOCK_DHXM:
                return "dhxm"
            elif self == stock.STOCK.STOCK_DHY:
                return "dhy"
            elif self == stock.STOCK.STOCK_DIAL:
                return "dial"
            elif self == stock.STOCK.STOCK_DIAX:
                return "diax"
            elif self == stock.STOCK.STOCK_DIN:
                return "din"
            elif self == stock.STOCK.STOCK_DIOD:
                return "diod"
            elif self == stock.STOCK.STOCK_DIS:
                return "dis"
            elif self == stock.STOCK.STOCK_DISCA:
                return "disca"
            elif self == stock.STOCK.STOCK_DISCB:
                return "discb"
            elif self == stock.STOCK.STOCK_DISCK:
                return "disck"
            elif self == stock.STOCK.STOCK_DISH:
                return "dish"
            elif self == stock.STOCK.STOCK_DIT:
                return "dit"
            elif self == stock.STOCK.STOCK_DIVA:
                return "diva"
            elif self == stock.STOCK.STOCK_DIVB:
                return "divb"
            elif self == stock.STOCK.STOCK_DIVO:
                return "divo"
            elif self == stock.STOCK.STOCK_DIVY:
                return "divy"
            elif self == stock.STOCK.STOCK_DJCO:
                return "djco"
            elif self == stock.STOCK.STOCK_DJD:
                return "djd"
            elif self == stock.STOCK.STOCK_DK:
                return "dk"
            elif self == stock.STOCK.STOCK_DKL:
                return "dkl"
            elif self == stock.STOCK.STOCK_DKS:
                return "dks"
            elif self == stock.STOCK.STOCK_DKT:
                return "dkt"
            elif self == stock.STOCK.STOCK_DL:
                return "dl"
            elif self == stock.STOCK.STOCK_DLA:
                return "dla"
            elif self == stock.STOCK.STOCK_DLB:
                return "dlb"
            elif self == stock.STOCK.STOCK_DLBL:
                return "dlbl"
            elif self == stock.STOCK.STOCK_DLBR:
                return "dlbr"
            elif self == stock.STOCK.STOCK_DLBS:
                return "dlbs"
            elif self == stock.STOCK.STOCK_DLHC:
                return "dlhc"
            elif self == stock.STOCK.STOCK_DLNG:
                return "dlng"
            elif self == stock.STOCK.STOCK_DLNG_A:
                return "dlng_a"
            elif self == stock.STOCK.STOCK_DLPH:
                return "dlph"
            elif self == stock.STOCK.STOCK_DLR:
                return "dlr"
            elif self == stock.STOCK.STOCK_DLR_C:
                return "dlr_c"
            elif self == stock.STOCK.STOCK_DLR_G:
                return "dlr_g"
            elif self == stock.STOCK.STOCK_DLR_H:
                return "dlr_h"
            elif self == stock.STOCK.STOCK_DLR_I:
                return "dlr_i"
            elif self == stock.STOCK.STOCK_DLR_J:
                return "dlr_j"
            elif self == stock.STOCK.STOCK_DLTH:
                return "dlth"
            elif self == stock.STOCK.STOCK_DLTR:
                return "dltr"
            elif self == stock.STOCK.STOCK_DLX:
                return "dlx"
            elif self == stock.STOCK.STOCK_DM:
                return "dm"
            elif self == stock.STOCK.STOCK_DMB:
                return "dmb"
            elif self == stock.STOCK.STOCK_DMF:
                return "dmf"
            elif self == stock.STOCK.STOCK_DMLP:
                return "dmlp"
            elif self == stock.STOCK.STOCK_DMO:
                return "dmo"
            elif self == stock.STOCK.STOCK_DMPI:
                return "dmpi"
            elif self == stock.STOCK.STOCK_DMRC:
                return "dmrc"
            elif self == stock.STOCK.STOCK_DMRI:
                return "dmri"
            elif self == stock.STOCK.STOCK_DMRL:
                return "dmrl"
            elif self == stock.STOCK.STOCK_DMTX:
                return "dmtx"
            elif self == stock.STOCK.STOCK_DNB:
                return "dnb"
            elif self == stock.STOCK.STOCK_DNBF:
                return "dnbf"
            elif self == stock.STOCK.STOCK_DNI:
                return "dni"
            elif self == stock.STOCK.STOCK_DNKN:
                return "dnkn"
            elif self == stock.STOCK.STOCK_DNN:
                return "dnn"
            elif self == stock.STOCK.STOCK_DNOW:
                return "dnow"
            elif self == stock.STOCK.STOCK_DNP:
                return "dnp"
            elif self == stock.STOCK.STOCK_DNR:
                return "dnr"
            elif self == stock.STOCK.STOCK_DO:
                return "do"
            elif self == stock.STOCK.STOCK_DOC:
                return "doc"
            elif self == stock.STOCK.STOCK_DOOR:
                return "door"
            elif self == stock.STOCK.STOCK_DORM:
                return "dorm"
            elif self == stock.STOCK.STOCK_DOTA:
                return "dota"
            elif self == stock.STOCK.STOCK_DOTAR:
                return "dotar"
            elif self == stock.STOCK.STOCK_DOTAU:
                return "dotau"
            elif self == stock.STOCK.STOCK_DOTAW:
                return "dotaw"
            elif self == stock.STOCK.STOCK_DOV:
                return "dov"
            elif self == stock.STOCK.STOCK_DOVA:
                return "dova"
            elif self == stock.STOCK.STOCK_DOX:
                return "dox"
            elif self == stock.STOCK.STOCK_DPG:
                return "dpg"
            elif self == stock.STOCK.STOCK_DPLO:
                return "dplo"
            elif self == stock.STOCK.STOCK_DPS:
                return "dps"
            elif self == stock.STOCK.STOCK_DPST:
                return "dpst"
            elif self == stock.STOCK.STOCK_DPW:
                return "dpw"
            elif self == stock.STOCK.STOCK_DPZ:
                return "dpz"
            elif self == stock.STOCK.STOCK_DQ:
                return "dq"
            elif self == stock.STOCK.STOCK_DRAD:
                return "drad"
            elif self == stock.STOCK.STOCK_DRD:
                return "drd"
            elif self == stock.STOCK.STOCK_DRE:
                return "dre"
            elif self == stock.STOCK.STOCK_DRH:
                return "drh"
            elif self == stock.STOCK.STOCK_DRI:
                return "dri"
            elif self == stock.STOCK.STOCK_DRIO:
                return "drio"
            elif self == stock.STOCK.STOCK_DRIOW:
                return "driow"
            elif self == stock.STOCK.STOCK_DRNA:
                return "drna"
            elif self == stock.STOCK.STOCK_DRQ:
                return "drq"
            elif self == stock.STOCK.STOCK_DRRX:
                return "drrx"
            elif self == stock.STOCK.STOCK_DRUA:
                return "drua"
            elif self == stock.STOCK.STOCK_DRYS:
                return "drys"
            elif self == stock.STOCK.STOCK_DS:
                return "ds"
            elif self == stock.STOCK.STOCK_DSE:
                return "dse"
            elif self == stock.STOCK.STOCK_DSGX:
                return "dsgx"
            elif self == stock.STOCK.STOCK_DSKE:
                return "dske"
            elif self == stock.STOCK.STOCK_DSKEW:
                return "dskew"
            elif self == stock.STOCK.STOCK_DSL:
                return "dsl"
            elif self == stock.STOCK.STOCK_DSM:
                return "dsm"
            elif self == stock.STOCK.STOCK_DSPG:
                return "dspg"
            elif self == stock.STOCK.STOCK_DSS:
                return "dss"
            elif self == stock.STOCK.STOCK_DST:
                return "dst"
            elif self == stock.STOCK.STOCK_DSU:
                return "dsu"
            elif self == stock.STOCK.STOCK_DSW:
                return "dsw"
            elif self == stock.STOCK.STOCK_DSWL:
                return "dswl"
            elif self == stock.STOCK.STOCK_DSX:
                return "dsx"
            elif self == stock.STOCK.STOCK_DSXN:
                return "dsxn"
            elif self == stock.STOCK.STOCK_DSX_B:
                return "dsx_b"
            elif self == stock.STOCK.STOCK_DS_B:
                return "ds_b"
            elif self == stock.STOCK.STOCK_DS_C:
                return "ds_c"
            elif self == stock.STOCK.STOCK_DS_D:
                return "ds_d"
            elif self == stock.STOCK.STOCK_DTE:
                return "dte"
            elif self == stock.STOCK.STOCK_DTEA:
                return "dtea"
            elif self == stock.STOCK.STOCK_DTF:
                return "dtf"
            elif self == stock.STOCK.STOCK_DTJ:
                return "dtj"
            elif self == stock.STOCK.STOCK_DTK:
                return "dtk"
            elif self == stock.STOCK.STOCK_DTLA_:
                return "dtla_"
            elif self == stock.STOCK.STOCK_DTQ:
                return "dtq"
            elif self == stock.STOCK.STOCK_DTRM:
                return "dtrm"
            elif self == stock.STOCK.STOCK_DTUL:
                return "dtul"
            elif self == stock.STOCK.STOCK_DTUS:
                return "dtus"
            elif self == stock.STOCK.STOCK_DTV:
                return "dtv"
            elif self == stock.STOCK.STOCK_DTY:
                return "dty"
            elif self == stock.STOCK.STOCK_DTYL:
                return "dtyl"
            elif self == stock.STOCK.STOCK_DTYS:
                return "dtys"
            elif self == stock.STOCK.STOCK_DUC:
                return "duc"
            elif self == stock.STOCK.STOCK_DUK:
                return "duk"
            elif self == stock.STOCK.STOCK_DUKH:
                return "dukh"
            elif self == stock.STOCK.STOCK_DUSA:
                return "dusa"
            elif self == stock.STOCK.STOCK_DUSL:
                return "dusl"
            elif self == stock.STOCK.STOCK_DVA:
                return "dva"
            elif self == stock.STOCK.STOCK_DVAX:
                return "dvax"
            elif self == stock.STOCK.STOCK_DVCR:
                return "dvcr"
            elif self == stock.STOCK.STOCK_DVD:
                return "dvd"
            elif self == stock.STOCK.STOCK_DVEM:
                return "dvem"
            elif self == stock.STOCK.STOCK_DVMT:
                return "dvmt"
            elif self == stock.STOCK.STOCK_DVN:
                return "dvn"
            elif self == stock.STOCK.STOCK_DVP:
                return "dvp"
            elif self == stock.STOCK.STOCK_DWAC:
                return "dwac"
            elif self == stock.STOCK.STOCK_DWAQ:
                return "dwaq"
            elif self == stock.STOCK.STOCK_DWAS:
                return "dwas"
            elif self == stock.STOCK.STOCK_DWAT:
                return "dwat"
            elif self == stock.STOCK.STOCK_DWCH:
                return "dwch"
            elif self == stock.STOCK.STOCK_DWDP:
                return "dwdp"
            elif self == stock.STOCK.STOCK_DWFI:
                return "dwfi"
            elif self == stock.STOCK.STOCK_DWIN:
                return "dwin"
            elif self == stock.STOCK.STOCK_DWLD:
                return "dwld"
            elif self == stock.STOCK.STOCK_DWLV:
                return "dwlv"
            elif self == stock.STOCK.STOCK_DWPP:
                return "dwpp"
            elif self == stock.STOCK.STOCK_DWSN:
                return "dwsn"
            elif self == stock.STOCK.STOCK_DWT:
                return "dwt"
            elif self == stock.STOCK.STOCK_DWTR:
                return "dwtr"
            elif self == stock.STOCK.STOCK_DX:
                return "dx"
            elif self == stock.STOCK.STOCK_DXB:
                return "dxb"
            elif self == stock.STOCK.STOCK_DXC:
                return "dxc"
            elif self == stock.STOCK.STOCK_DXCM:
                return "dxcm"
            elif self == stock.STOCK.STOCK_DXLG:
                return "dxlg"
            elif self == stock.STOCK.STOCK_DXPE:
                return "dxpe"
            elif self == stock.STOCK.STOCK_DXR:
                return "dxr"
            elif self == stock.STOCK.STOCK_DXTR:
                return "dxtr"
            elif self == stock.STOCK.STOCK_DXUS:
                return "dxus"
            elif self == stock.STOCK.STOCK_DXYN:
                return "dxyn"
            elif self == stock.STOCK.STOCK_DX_A:
                return "dx_a"
            elif self == stock.STOCK.STOCK_DX_B:
                return "dx_b"
            elif self == stock.STOCK.STOCK_DY:
                return "dy"
            elif self == stock.STOCK.STOCK_DYB:
                return "dyb"
            elif self == stock.STOCK.STOCK_DYLS:
                return "dyls"
            elif self == stock.STOCK.STOCK_DYN-WS-A:
                return "dyn-ws-a"
            elif self == stock.STOCK.STOCK_DYN:
                return "dyn"
            elif self == stock.STOCK.STOCK_DYNC:
                return "dync"
            elif self == stock.STOCK.STOCK_DYNT:
                return "dynt"
            elif self == stock.STOCK.STOCK_DYN_A:
                return "dyn_a"
            elif self == stock.STOCK.STOCK_DYSL:
                return "dysl"
            elif self == stock.STOCK.STOCK_DZSI:
                return "dzsi"
            elif self == stock.STOCK.STOCK_E:
                return "e"
            elif self == stock.STOCK.STOCK_EA:
                return "ea"
            elif self == stock.STOCK.STOCK_EAB:
                return "eab"
            elif self == stock.STOCK.STOCK_EACQ:
                return "eacq"
            elif self == stock.STOCK.STOCK_EACQU:
                return "eacqu"
            elif self == stock.STOCK.STOCK_EACQW:
                return "eacqw"
            elif self == stock.STOCK.STOCK_EAD:
                return "ead"
            elif self == stock.STOCK.STOCK_EAE:
                return "eae"
            elif self == stock.STOCK.STOCK_EAGL:
                return "eagl"
            elif self == stock.STOCK.STOCK_EAGLU:
                return "eaglu"
            elif self == stock.STOCK.STOCK_EAGLW:
                return "eaglw"
            elif self == stock.STOCK.STOCK_EAI:
                return "eai"
            elif self == stock.STOCK.STOCK_EARN:
                return "earn"
            elif self == stock.STOCK.STOCK_EARS:
                return "ears"
            elif self == stock.STOCK.STOCK_EAT:
                return "eat"
            elif self == stock.STOCK.STOCK_EBAY:
                return "ebay"
            elif self == stock.STOCK.STOCK_EBAYL:
                return "ebayl"
            elif self == stock.STOCK.STOCK_EBF:
                return "ebf"
            elif self == stock.STOCK.STOCK_EBIO:
                return "ebio"
            elif self == stock.STOCK.STOCK_EBIX:
                return "ebix"
            elif self == stock.STOCK.STOCK_EBMT:
                return "ebmt"
            elif self == stock.STOCK.STOCK_EBR-B:
                return "ebr-b"
            elif self == stock.STOCK.STOCK_EBR:
                return "ebr"
            elif self == stock.STOCK.STOCK_EBS:
                return "ebs"
            elif self == stock.STOCK.STOCK_EBSB:
                return "ebsb"
            elif self == stock.STOCK.STOCK_EBTC:
                return "ebtc"
            elif self == stock.STOCK.STOCK_EC:
                return "ec"
            elif self == stock.STOCK.STOCK_ECA:
                return "eca"
            elif self == stock.STOCK.STOCK_ECC:
                return "ecc"
            elif self == stock.STOCK.STOCK_ECCA:
                return "ecca"
            elif self == stock.STOCK.STOCK_ECCB:
                return "eccb"
            elif self == stock.STOCK.STOCK_ECCY:
                return "eccy"
            elif self == stock.STOCK.STOCK_ECCZ:
                return "eccz"
            elif self == stock.STOCK.STOCK_ECF:
                return "ecf"
            elif self == stock.STOCK.STOCK_ECF_A:
                return "ecf_a"
            elif self == stock.STOCK.STOCK_ECHO:
                return "echo"
            elif self == stock.STOCK.STOCK_ECL:
                return "ecl"
            elif self == stock.STOCK.STOCK_ECOL:
                return "ecol"
            elif self == stock.STOCK.STOCK_ECOM:
                return "ecom"
            elif self == stock.STOCK.STOCK_ECPG:
                return "ecpg"
            elif self == stock.STOCK.STOCK_ECR:
                return "ecr"
            elif self == stock.STOCK.STOCK_ECT:
                return "ect"
            elif self == stock.STOCK.STOCK_ECYT:
                return "ecyt"
            elif self == stock.STOCK.STOCK_ED:
                return "ed"
            elif self == stock.STOCK.STOCK_EDAP:
                return "edap"
            elif self == stock.STOCK.STOCK_EDBI:
                return "edbi"
            elif self == stock.STOCK.STOCK_EDD:
                return "edd"
            elif self == stock.STOCK.STOCK_EDF:
                return "edf"
            elif self == stock.STOCK.STOCK_EDGE:
                return "edge"
            elif self == stock.STOCK.STOCK_EDGW:
                return "edgw"
            elif self == stock.STOCK.STOCK_EDI:
                return "edi"
            elif self == stock.STOCK.STOCK_EDIT:
                return "edit"
            elif self == stock.STOCK.STOCK_EDN:
                return "edn"
            elif self == stock.STOCK.STOCK_EDOM:
                return "edom"
            elif self == stock.STOCK.STOCK_EDOW:
                return "edow"
            elif self == stock.STOCK.STOCK_EDR:
                return "edr"
            elif self == stock.STOCK.STOCK_EDU:
                return "edu"
            elif self == stock.STOCK.STOCK_EDUC:
                return "educ"
            elif self == stock.STOCK.STOCK_EE:
                return "ee"
            elif self == stock.STOCK.STOCK_EEA:
                return "eea"
            elif self == stock.STOCK.STOCK_EEFT:
                return "eeft"
            elif self == stock.STOCK.STOCK_EEI:
                return "eei"
            elif self == stock.STOCK.STOCK_EEMO:
                return "eemo"
            elif self == stock.STOCK.STOCK_EEMX:
                return "eemx"
            elif self == stock.STOCK.STOCK_EEP:
                return "eep"
            elif self == stock.STOCK.STOCK_EEQ:
                return "eeq"
            elif self == stock.STOCK.STOCK_EEX:
                return "eex"
            elif self == stock.STOCK.STOCK_EFAS:
                return "efas"
            elif self == stock.STOCK.STOCK_EFAX:
                return "efax"
            elif self == stock.STOCK.STOCK_EFBI:
                return "efbi"
            elif self == stock.STOCK.STOCK_EFC:
                return "efc"
            elif self == stock.STOCK.STOCK_EFF:
                return "eff"
            elif self == stock.STOCK.STOCK_EFII:
                return "efii"
            elif self == stock.STOCK.STOCK_EFL:
                return "efl"
            elif self == stock.STOCK.STOCK_EFNL:
                return "efnl"
            elif self == stock.STOCK.STOCK_EFOI:
                return "efoi"
            elif self == stock.STOCK.STOCK_EFR:
                return "efr"
            elif self == stock.STOCK.STOCK_EFSC:
                return "efsc"
            elif self == stock.STOCK.STOCK_EFT:
                return "eft"
            elif self == stock.STOCK.STOCK_EFX:
                return "efx"
            elif self == stock.STOCK.STOCK_EGAN:
                return "egan"
            elif self == stock.STOCK.STOCK_EGBN:
                return "egbn"
            elif self == stock.STOCK.STOCK_EGF:
                return "egf"
            elif self == stock.STOCK.STOCK_EGHT:
                return "eght"
            elif self == stock.STOCK.STOCK_EGI:
                return "egi"
            elif self == stock.STOCK.STOCK_EGIF:
                return "egif"
            elif self == stock.STOCK.STOCK_EGL:
                return "egl"
            elif self == stock.STOCK.STOCK_EGLE:
                return "egle"
            elif self == stock.STOCK.STOCK_EGLT:
                return "eglt"
            elif self == stock.STOCK.STOCK_EGN:
                return "egn"
            elif self == stock.STOCK.STOCK_EGO:
                return "ego"
            elif self == stock.STOCK.STOCK_EGOV:
                return "egov"
            elif self == stock.STOCK.STOCK_EGP:
                return "egp"
            elif self == stock.STOCK.STOCK_EGRX:
                return "egrx"
            elif self == stock.STOCK.STOCK_EGY:
                return "egy"
            elif self == stock.STOCK.STOCK_EHI:
                return "ehi"
            elif self == stock.STOCK.STOCK_EHIC:
                return "ehic"
            elif self == stock.STOCK.STOCK_EHR:
                return "ehr"
            elif self == stock.STOCK.STOCK_EHT:
                return "eht"
            elif self == stock.STOCK.STOCK_EHTH:
                return "ehth"
            elif self == stock.STOCK.STOCK_EIA:
                return "eia"
            elif self == stock.STOCK.STOCK_EIG:
                return "eig"
            elif self == stock.STOCK.STOCK_EIGI:
                return "eigi"
            elif self == stock.STOCK.STOCK_EIGR:
                return "eigr"
            elif self == stock.STOCK.STOCK_EIM:
                return "eim"
            elif self == stock.STOCK.STOCK_EIO:
                return "eio"
            elif self == stock.STOCK.STOCK_EIP:
                return "eip"
            elif self == stock.STOCK.STOCK_EIV:
                return "eiv"
            elif self == stock.STOCK.STOCK_EIX:
                return "eix"
            elif self == stock.STOCK.STOCK_EKSO:
                return "ekso"
            elif self == stock.STOCK.STOCK_EL:
                return "el"
            elif self == stock.STOCK.STOCK_ELC:
                return "elc"
            elif self == stock.STOCK.STOCK_ELEC:
                return "elec"
            elif self == stock.STOCK.STOCK_ELECU:
                return "elecu"
            elif self == stock.STOCK.STOCK_ELECW:
                return "elecw"
            elif self == stock.STOCK.STOCK_ELF:
                return "elf"
            elif self == stock.STOCK.STOCK_ELGX:
                return "elgx"
            elif self == stock.STOCK.STOCK_ELJ:
                return "elj"
            elif self == stock.STOCK.STOCK_ELLI:
                return "elli"
            elif self == stock.STOCK.STOCK_ELLO:
                return "ello"
            elif self == stock.STOCK.STOCK_ELMD:
                return "elmd"
            elif self == stock.STOCK.STOCK_ELON:
                return "elon"
            elif self == stock.STOCK.STOCK_ELP:
                return "elp"
            elif self == stock.STOCK.STOCK_ELS:
                return "els"
            elif self == stock.STOCK.STOCK_ELSE:
                return "else"
            elif self == stock.STOCK.STOCK_ELTK:
                return "eltk"
            elif self == stock.STOCK.STOCK_ELU:
                return "elu"
            elif self == stock.STOCK.STOCK_ELVT:
                return "elvt"
            elif self == stock.STOCK.STOCK_ELY:
                return "ely"
            elif self == stock.STOCK.STOCK_EMAN:
                return "eman"
            elif self == stock.STOCK.STOCK_EMBH:
                return "embh"
            elif self == stock.STOCK.STOCK_EMBU:
                return "embu"
            elif self == stock.STOCK.STOCK_EMCF:
                return "emcf"
            elif self == stock.STOCK.STOCK_EMCI:
                return "emci"
            elif self == stock.STOCK.STOCK_EMD:
                return "emd"
            elif self == stock.STOCK.STOCK_EMDV:
                return "emdv"
            elif self == stock.STOCK.STOCK_EME:
                return "eme"
            elif self == stock.STOCK.STOCK_EMES:
                return "emes"
            elif self == stock.STOCK.STOCK_EMF:
                return "emf"
            elif self == stock.STOCK.STOCK_EMGF:
                return "emgf"
            elif self == stock.STOCK.STOCK_EMHY:
                return "emhy"
            elif self == stock.STOCK.STOCK_EMI:
                return "emi"
            elif self == stock.STOCK.STOCK_EMITF:
                return "emitf"
            elif self == stock.STOCK.STOCK_EMJ:
                return "emj"
            elif self == stock.STOCK.STOCK_EMKR:
                return "emkr"
            elif self == stock.STOCK.STOCK_EML:
                return "eml"
            elif self == stock.STOCK.STOCK_EMMS:
                return "emms"
            elif self == stock.STOCK.STOCK_EMN:
                return "emn"
            elif self == stock.STOCK.STOCK_EMO:
                return "emo"
            elif self == stock.STOCK.STOCK_EMP:
                return "emp"
            elif self == stock.STOCK.STOCK_EMQQ:
                return "emqq"
            elif self == stock.STOCK.STOCK_EMR:
                return "emr"
            elif self == stock.STOCK.STOCK_EMSD:
                return "emsd"
            elif self == stock.STOCK.STOCK_EMTL:
                return "emtl"
            elif self == stock.STOCK.STOCK_EMX:
                return "emx"
            elif self == stock.STOCK.STOCK_EMXC:
                return "emxc"
            elif self == stock.STOCK.STOCK_ENB:
                return "enb"
            elif self == stock.STOCK.STOCK_ENBL:
                return "enbl"
            elif self == stock.STOCK.STOCK_ENDP:
                return "endp"
            elif self == stock.STOCK.STOCK_ENFC:
                return "enfc"
            elif self == stock.STOCK.STOCK_ENG:
                return "eng"
            elif self == stock.STOCK.STOCK_ENH_C:
                return "enh_c"
            elif self == stock.STOCK.STOCK_ENIA:
                return "enia"
            elif self == stock.STOCK.STOCK_ENIC:
                return "enic"
            elif self == stock.STOCK.STOCK_ENJ:
                return "enj"
            elif self == stock.STOCK.STOCK_ENLC:
                return "enlc"
            elif self == stock.STOCK.STOCK_ENLK:
                return "enlk"
            elif self == stock.STOCK.STOCK_ENO:
                return "eno"
            elif self == stock.STOCK.STOCK_ENOR:
                return "enor"
            elif self == stock.STOCK.STOCK_ENPH:
                return "enph"
            elif self == stock.STOCK.STOCK_ENR:
                return "enr"
            elif self == stock.STOCK.STOCK_ENRJ:
                return "enrj"
            elif self == stock.STOCK.STOCK_ENS:
                return "ens"
            elif self == stock.STOCK.STOCK_ENSG:
                return "ensg"
            elif self == stock.STOCK.STOCK_ENSV:
                return "ensv"
            elif self == stock.STOCK.STOCK_ENT:
                return "ent"
            elif self == stock.STOCK.STOCK_ENTA:
                return "enta"
            elif self == stock.STOCK.STOCK_ENTG:
                return "entg"
            elif self == stock.STOCK.STOCK_ENTL:
                return "entl"
            elif self == stock.STOCK.STOCK_ENTR:
                return "entr"
            elif self == stock.STOCK.STOCK_ENV:
                return "env"
            elif self == stock.STOCK.STOCK_ENVA:
                return "enva"
            elif self == stock.STOCK.STOCK_ENX:
                return "enx"
            elif self == stock.STOCK.STOCK_ENZ:
                return "enz"
            elif self == stock.STOCK.STOCK_ENZY:
                return "enzy"
            elif self == stock.STOCK.STOCK_EOCC:
                return "eocc"
            elif self == stock.STOCK.STOCK_EOD:
                return "eod"
            elif self == stock.STOCK.STOCK_EOG:
                return "eog"
            elif self == stock.STOCK.STOCK_EOI:
                return "eoi"
            elif self == stock.STOCK.STOCK_EOS:
                return "eos"
            elif self == stock.STOCK.STOCK_EOT:
                return "eot"
            elif self == stock.STOCK.STOCK_EPAM:
                return "epam"
            elif self == stock.STOCK.STOCK_EPAY:
                return "epay"
            elif self == stock.STOCK.STOCK_EPC:
                return "epc"
            elif self == stock.STOCK.STOCK_EPD:
                return "epd"
            elif self == stock.STOCK.STOCK_EPE:
                return "epe"
            elif self == stock.STOCK.STOCK_EPIX:
                return "epix"
            elif self == stock.STOCK.STOCK_EPM:
                return "epm"
            elif self == stock.STOCK.STOCK_EPR:
                return "epr"
            elif self == stock.STOCK.STOCK_EPRF:
                return "eprf"
            elif self == stock.STOCK.STOCK_EPR_C:
                return "epr_c"
            elif self == stock.STOCK.STOCK_EPR_E:
                return "epr_e"
            elif self == stock.STOCK.STOCK_EPR_F:
                return "epr_f"
            elif self == stock.STOCK.STOCK_EPZM:
                return "epzm"
            elif self == stock.STOCK.STOCK_EP_C:
                return "ep_c"
            elif self == stock.STOCK.STOCK_EQBK:
                return "eqbk"
            elif self == stock.STOCK.STOCK_EQC:
                return "eqc"
            elif self == stock.STOCK.STOCK_EQCO:
                return "eqco"
            elif self == stock.STOCK.STOCK_EQC_D:
                return "eqc_d"
            elif self == stock.STOCK.STOCK_EQFN:
                return "eqfn"
            elif self == stock.STOCK.STOCK_EQGP:
                return "eqgp"
            elif self == stock.STOCK.STOCK_EQIX:
                return "eqix"
            elif self == stock.STOCK.STOCK_EQM:
                return "eqm"
            elif self == stock.STOCK.STOCK_EQR:
                return "eqr"
            elif self == stock.STOCK.STOCK_EQRR:
                return "eqrr"
            elif self == stock.STOCK.STOCK_EQS:
                return "eqs"
            elif self == stock.STOCK.STOCK_EQT:
                return "eqt"
            elif self == stock.STOCK.STOCK_ERA:
                return "era"
            elif self == stock.STOCK.STOCK_ERC:
                return "erc"
            elif self == stock.STOCK.STOCK_ERF:
                return "erf"
            elif self == stock.STOCK.STOCK_ERGF:
                return "ergf"
            elif self == stock.STOCK.STOCK_ERH:
                return "erh"
            elif self == stock.STOCK.STOCK_ERI:
                return "eri"
            elif self == stock.STOCK.STOCK_ERIC:
                return "eric"
            elif self == stock.STOCK.STOCK_ERIE:
                return "erie"
            elif self == stock.STOCK.STOCK_ERII:
                return "erii"
            elif self == stock.STOCK.STOCK_ERJ:
                return "erj"
            elif self == stock.STOCK.STOCK_ERM:
                return "erm"
            elif self == stock.STOCK.STOCK_ERN:
                return "ern"
            elif self == stock.STOCK.STOCK_EROS:
                return "eros"
            elif self == stock.STOCK.STOCK_ERYP:
                return "eryp"
            elif self == stock.STOCK.STOCK_ES:
                return "es"
            elif self == stock.STOCK.STOCK_ESBA:
                return "esba"
            elif self == stock.STOCK.STOCK_ESBK:
                return "esbk"
            elif self == stock.STOCK.STOCK_ESCA:
                return "esca"
            elif self == stock.STOCK.STOCK_ESDI:
                return "esdi"
            elif self == stock.STOCK.STOCK_ESDIW:
                return "esdiw"
            elif self == stock.STOCK.STOCK_ESE:
                return "ese"
            elif self == stock.STOCK.STOCK_ESEA:
                return "esea"
            elif self == stock.STOCK.STOCK_ESES:
                return "eses"
            elif self == stock.STOCK.STOCK_ESG:
                return "esg"
            elif self == stock.STOCK.STOCK_ESGD:
                return "esgd"
            elif self == stock.STOCK.STOCK_ESGE:
                return "esge"
            elif self == stock.STOCK.STOCK_ESGF:
                return "esgf"
            elif self == stock.STOCK.STOCK_ESGG:
                return "esgg"
            elif self == stock.STOCK.STOCK_ESGL:
                return "esgl"
            elif self == stock.STOCK.STOCK_ESGN:
                return "esgn"
            elif self == stock.STOCK.STOCK_ESGR:
                return "esgr"
            elif self == stock.STOCK.STOCK_ESGS:
                return "esgs"
            elif self == stock.STOCK.STOCK_ESGU:
                return "esgu"
            elif self == stock.STOCK.STOCK_ESGW:
                return "esgw"
            elif self == stock.STOCK.STOCK_ESIO:
                return "esio"
            elif self == stock.STOCK.STOCK_ESL:
                return "esl"
            elif self == stock.STOCK.STOCK_ESLT:
                return "eslt"
            elif self == stock.STOCK.STOCK_ESNC:
                return "esnc"
            elif self == stock.STOCK.STOCK_ESND:
                return "esnd"
            elif self == stock.STOCK.STOCK_ESNT:
                return "esnt"
            elif self == stock.STOCK.STOCK_ESP:
                return "esp"
            elif self == stock.STOCK.STOCK_ESPR:
                return "espr"
            elif self == stock.STOCK.STOCK_ESQ:
                return "esq"
            elif self == stock.STOCK.STOCK_ESRT:
                return "esrt"
            elif self == stock.STOCK.STOCK_ESRX:
                return "esrx"
            elif self == stock.STOCK.STOCK_ESS:
                return "ess"
            elif self == stock.STOCK.STOCK_ESSA:
                return "essa"
            elif self == stock.STOCK.STOCK_ESTE:
                return "este"
            elif self == stock.STOCK.STOCK_ESV:
                return "esv"
            elif self == stock.STOCK.STOCK_ESXB:
                return "esxb"
            elif self == stock.STOCK.STOCK_ETB:
                return "etb"
            elif self == stock.STOCK.STOCK_ETE:
                return "ete"
            elif self == stock.STOCK.STOCK_ETFC:
                return "etfc"
            elif self == stock.STOCK.STOCK_ETG:
                return "etg"
            elif self == stock.STOCK.STOCK_ETH:
                return "eth"
            elif self == stock.STOCK.STOCK_ETHO:
                return "etho"
            elif self == stock.STOCK.STOCK_ETJ:
                return "etj"
            elif self == stock.STOCK.STOCK_ETM:
                return "etm"
            elif self == stock.STOCK.STOCK_ETMW:
                return "etmw"
            elif self == stock.STOCK.STOCK_ETN:
                return "etn"
            elif self == stock.STOCK.STOCK_ETO:
                return "eto"
            elif self == stock.STOCK.STOCK_ETP:
                return "etp"
            elif self == stock.STOCK.STOCK_ETR:
                return "etr"
            elif self == stock.STOCK.STOCK_ETSY:
                return "etsy"
            elif self == stock.STOCK.STOCK_ETV:
                return "etv"
            elif self == stock.STOCK.STOCK_ETW:
                return "etw"
            elif self == stock.STOCK.STOCK_ETX:
                return "etx"
            elif self == stock.STOCK.STOCK_ETY:
                return "ety"
            elif self == stock.STOCK.STOCK_EUDV:
                return "eudv"
            elif self == stock.STOCK.STOCK_EUFL:
                return "eufl"
            elif self == stock.STOCK.STOCK_EURN:
                return "eurn"
            elif self == stock.STOCK.STOCK_EURZ:
                return "eurz"
            elif self == stock.STOCK.STOCK_EUXL:
                return "euxl"
            elif self == stock.STOCK.STOCK_EV:
                return "ev"
            elif self == stock.STOCK.STOCK_EVA:
                return "eva"
            elif self == stock.STOCK.STOCK_EVAR:
                return "evar"
            elif self == stock.STOCK.STOCK_EVBG:
                return "evbg"
            elif self == stock.STOCK.STOCK_EVBN:
                return "evbn"
            elif self == stock.STOCK.STOCK_EVC:
                return "evc"
            elif self == stock.STOCK.STOCK_EVEP:
                return "evep"
            elif self == stock.STOCK.STOCK_EVF:
                return "evf"
            elif self == stock.STOCK.STOCK_EVG:
                return "evg"
            elif self == stock.STOCK.STOCK_EVGBC:
                return "evgbc"
            elif self == stock.STOCK.STOCK_EVGN:
                return "evgn"
            elif self == stock.STOCK.STOCK_EVH:
                return "evh"
            elif self == stock.STOCK.STOCK_EVHC:
                return "evhc"
            elif self == stock.STOCK.STOCK_EVI:
                return "evi"
            elif self == stock.STOCK.STOCK_EVIX:
                return "evix"
            elif self == stock.STOCK.STOCK_EVJ:
                return "evj"
            elif self == stock.STOCK.STOCK_EVK:
                return "evk"
            elif self == stock.STOCK.STOCK_EVLMC:
                return "evlmc"
            elif self == stock.STOCK.STOCK_EVLV:
                return "evlv"
            elif self == stock.STOCK.STOCK_EVM:
                return "evm"
            elif self == stock.STOCK.STOCK_EVN:
                return "evn"
            elif self == stock.STOCK.STOCK_EVO:
                return "evo"
            elif self == stock.STOCK.STOCK_EVOK:
                return "evok"
            elif self == stock.STOCK.STOCK_EVOL:
                return "evol"
            elif self == stock.STOCK.STOCK_EVP:
                return "evp"
            elif self == stock.STOCK.STOCK_EVR:
                return "evr"
            elif self == stock.STOCK.STOCK_EVRI:
                return "evri"
            elif self == stock.STOCK.STOCK_EVSTC:
                return "evstc"
            elif self == stock.STOCK.STOCK_EVT:
                return "evt"
            elif self == stock.STOCK.STOCK_EVTC:
                return "evtc"
            elif self == stock.STOCK.STOCK_EVV:
                return "evv"
            elif self == stock.STOCK.STOCK_EVY:
                return "evy"
            elif self == stock.STOCK.STOCK_EW:
                return "ew"
            elif self == stock.STOCK.STOCK_EWBC:
                return "ewbc"
            elif self == stock.STOCK.STOCK_EWGS:
                return "ewgs"
            elif self == stock.STOCK.STOCK_EWMC:
                return "ewmc"
            elif self == stock.STOCK.STOCK_EWRE:
                return "ewre"
            elif self == stock.STOCK.STOCK_EWSC:
                return "ewsc"
            elif self == stock.STOCK.STOCK_EWUS:
                return "ewus"
            elif self == stock.STOCK.STOCK_EXA:
                return "exa"
            elif self == stock.STOCK.STOCK_EXAC:
                return "exac"
            elif self == stock.STOCK.STOCK_EXAS:
                return "exas"
            elif self == stock.STOCK.STOCK_EXC:
                return "exc"
            elif self == stock.STOCK.STOCK_EXD:
                return "exd"
            elif self == stock.STOCK.STOCK_EXEL:
                return "exel"
            elif self == stock.STOCK.STOCK_EXFO:
                return "exfo"
            elif self == stock.STOCK.STOCK_EXG:
                return "exg"
            elif self == stock.STOCK.STOCK_EXIV:
                return "exiv"
            elif self == stock.STOCK.STOCK_EXK:
                return "exk"
            elif self == stock.STOCK.STOCK_EXLS:
                return "exls"
            elif self == stock.STOCK.STOCK_EXP:
                return "exp"
            elif self == stock.STOCK.STOCK_EXPD:
                return "expd"
            elif self == stock.STOCK.STOCK_EXPE:
                return "expe"
            elif self == stock.STOCK.STOCK_EXPO:
                return "expo"
            elif self == stock.STOCK.STOCK_EXPR:
                return "expr"
            elif self == stock.STOCK.STOCK_EXR:
                return "exr"
            elif self == stock.STOCK.STOCK_EXTN:
                return "extn"
            elif self == stock.STOCK.STOCK_EXTR:
                return "extr"
            elif self == stock.STOCK.STOCK_EXXI:
                return "exxi"
            elif self == stock.STOCK.STOCK_EYE:
                return "eye"
            elif self == stock.STOCK.STOCK_EYEG:
                return "eyeg"
            elif self == stock.STOCK.STOCK_EYEGW:
                return "eyegw"
            elif self == stock.STOCK.STOCK_EYES:
                return "eyes"
            elif self == stock.STOCK.STOCK_EYESW:
                return "eyesw"
            elif self == stock.STOCK.STOCK_EYLD:
                return "eyld"
            elif self == stock.STOCK.STOCK_EZPW:
                return "ezpw"
            elif self == stock.STOCK.STOCK_EZT:
                return "ezt"
            elif self == stock.STOCK.STOCK_F:
                return "f"
            elif self == stock.STOCK.STOCK_FAAR:
                return "faar"
            elif self == stock.STOCK.STOCK_FAC:
                return "fac"
            elif self == stock.STOCK.STOCK_FAF:
                return "faf"
            elif self == stock.STOCK.STOCK_FALN:
                return "faln"
            elif self == stock.STOCK.STOCK_FANG:
                return "fang"
            elif self == stock.STOCK.STOCK_FANH:
                return "fanh"
            elif self == stock.STOCK.STOCK_FANZ:
                return "fanz"
            elif self == stock.STOCK.STOCK_FARM:
                return "farm"
            elif self == stock.STOCK.STOCK_FARO:
                return "faro"
            elif self == stock.STOCK.STOCK_FAST:
                return "fast"
            elif self == stock.STOCK.STOCK_FAT:
                return "fat"
            elif self == stock.STOCK.STOCK_FATE:
                return "fate"
            elif self == stock.STOCK.STOCK_FAX:
                return "fax"
            elif self == stock.STOCK.STOCK_FB:
                return "fb"
            elif self == stock.STOCK.STOCK_FBC:
                return "fbc"
            elif self == stock.STOCK.STOCK_FBHS:
                return "fbhs"
            elif self == stock.STOCK.STOCK_FBIO:
                return "fbio"
            elif self == stock.STOCK.STOCK_FBIZ:
                return "fbiz"
            elif self == stock.STOCK.STOCK_FBK:
                return "fbk"
            elif self == stock.STOCK.STOCK_FBM:
                return "fbm"
            elif self == stock.STOCK.STOCK_FBMS:
                return "fbms"
            elif self == stock.STOCK.STOCK_FBNC:
                return "fbnc"
            elif self == stock.STOCK.STOCK_FBNK:
                return "fbnk"
            elif self == stock.STOCK.STOCK_FBP:
                return "fbp"
            elif self == stock.STOCK.STOCK_FBR:
                return "fbr"
            elif self == stock.STOCK.STOCK_FBSS:
                return "fbss"
            elif self == stock.STOCK.STOCK_FC:
                return "fc"
            elif self == stock.STOCK.STOCK_FCAL:
                return "fcal"
            elif self == stock.STOCK.STOCK_FCAP:
                return "fcap"
            elif self == stock.STOCK.STOCK_FCAU:
                return "fcau"
            elif self == stock.STOCK.STOCK_FCB:
                return "fcb"
            elif self == stock.STOCK.STOCK_FCBC:
                return "fcbc"
            elif self == stock.STOCK.STOCK_FCCO:
                return "fcco"
            elif self == stock.STOCK.STOCK_FCCY:
                return "fccy"
            elif self == stock.STOCK.STOCK_FCE-A:
                return "fce-a"
            elif self == stock.STOCK.STOCK_FCEF:
                return "fcef"
            elif self == stock.STOCK.STOCK_FCEL:
                return "fcel"
            elif self == stock.STOCK.STOCK_FCF:
                return "fcf"
            elif self == stock.STOCK.STOCK_FCFS:
                return "fcfs"
            elif self == stock.STOCK.STOCK_FCN:
                return "fcn"
            elif self == stock.STOCK.STOCK_FCNCA:
                return "fcnca"
            elif self == stock.STOCK.STOCK_FCO:
                return "fco"
            elif self == stock.STOCK.STOCK_FCPT:
                return "fcpt"
            elif self == stock.STOCK.STOCK_FCRE:
                return "fcre"
            elif self == stock.STOCK.STOCK_FCSC:
                return "fcsc"
            elif self == stock.STOCK.STOCK_FCVT:
                return "fcvt"
            elif self == stock.STOCK.STOCK_FCX:
                return "fcx"
            elif self == stock.STOCK.STOCK_FDBC:
                return "fdbc"
            elif self == stock.STOCK.STOCK_FDC:
                return "fdc"
            elif self == stock.STOCK.STOCK_FDEF:
                return "fdef"
            elif self == stock.STOCK.STOCK_FDEU:
                return "fdeu"
            elif self == stock.STOCK.STOCK_FDLO:
                return "fdlo"
            elif self == stock.STOCK.STOCK_FDMO:
                return "fdmo"
            elif self == stock.STOCK.STOCK_FDP:
                return "fdp"
            elif self == stock.STOCK.STOCK_FDRR:
                return "fdrr"
            elif self == stock.STOCK.STOCK_FDS:
                return "fds"
            elif self == stock.STOCK.STOCK_FDUS:
                return "fdus"
            elif self == stock.STOCK.STOCK_FDVV:
                return "fdvv"
            elif self == stock.STOCK.STOCK_FDX:
                return "fdx"
            elif self == stock.STOCK.STOCK_FE:
                return "fe"
            elif self == stock.STOCK.STOCK_FEDU:
                return "fedu"
            elif self == stock.STOCK.STOCK_FEIM:
                return "feim"
            elif self == stock.STOCK.STOCK_FELE:
                return "fele"
            elif self == stock.STOCK.STOCK_FELP:
                return "felp"
            elif self == stock.STOCK.STOCK_FEN:
                return "fen"
            elif self == stock.STOCK.STOCK_FENC:
                return "fenc"
            elif self == stock.STOCK.STOCK_FENG:
                return "feng"
            elif self == stock.STOCK.STOCK_FET:
                return "fet"
            elif self == stock.STOCK.STOCK_FEYE:
                return "feye"
            elif self == stock.STOCK.STOCK_FF:
                return "ff"
            elif self == stock.STOCK.STOCK_FFBC:
                return "ffbc"
            elif self == stock.STOCK.STOCK_FFBCW:
                return "ffbcw"
            elif self == stock.STOCK.STOCK_FFBW:
                return "ffbw"
            elif self == stock.STOCK.STOCK_FFC:
                return "ffc"
            elif self == stock.STOCK.STOCK_FFG:
                return "ffg"
            elif self == stock.STOCK.STOCK_FFHG:
                return "ffhg"
            elif self == stock.STOCK.STOCK_FFHL:
                return "ffhl"
            elif self == stock.STOCK.STOCK_FFIC:
                return "ffic"
            elif self == stock.STOCK.STOCK_FFIN:
                return "ffin"
            elif self == stock.STOCK.STOCK_FFIU:
                return "ffiu"
            elif self == stock.STOCK.STOCK_FFIV:
                return "ffiv"
            elif self == stock.STOCK.STOCK_FFKT:
                return "ffkt"
            elif self == stock.STOCK.STOCK_FFNW:
                return "ffnw"
            elif self == stock.STOCK.STOCK_FFSG:
                return "ffsg"
            elif self == stock.STOCK.STOCK_FFTG:
                return "fftg"
            elif self == stock.STOCK.STOCK_FFTI:
                return "ffti"
            elif self == stock.STOCK.STOCK_FFTY:
                return "ffty"
            elif self == stock.STOCK.STOCK_FFWM:
                return "ffwm"
            elif self == stock.STOCK.STOCK_FGBI:
                return "fgbi"
            elif self == stock.STOCK.STOCK_FGEN:
                return "fgen"
            elif self == stock.STOCK.STOCK_FGL:
                return "fgl"
            elif self == stock.STOCK.STOCK_FGP:
                return "fgp"
            elif self == stock.STOCK.STOCK_FH:
                return "fh"
            elif self == stock.STOCK.STOCK_FHB:
                return "fhb"
            elif self == stock.STOCK.STOCK_FHN:
                return "fhn"
            elif self == stock.STOCK.STOCK_FHN_A:
                return "fhn_a"
            elif self == stock.STOCK.STOCK_FI:
                return "fi"
            elif self == stock.STOCK.STOCK_FIBK:
                return "fibk"
            elif self == stock.STOCK.STOCK_FIBR:
                return "fibr"
            elif self == stock.STOCK.STOCK_FICO:
                return "fico"
            elif self == stock.STOCK.STOCK_FIEE:
                return "fiee"
            elif self == stock.STOCK.STOCK_FIG:
                return "fig"
            elif self == stock.STOCK.STOCK_FIHD:
                return "fihd"
            elif self == stock.STOCK.STOCK_FII:
                return "fii"
            elif self == stock.STOCK.STOCK_FINL:
                return "finl"
            elif self == stock.STOCK.STOCK_FINX:
                return "finx"
            elif self == stock.STOCK.STOCK_FIS:
                return "fis"
            elif self == stock.STOCK.STOCK_FISI:
                return "fisi"
            elif self == stock.STOCK.STOCK_FISK:
                return "fisk"
            elif self == stock.STOCK.STOCK_FISV:
                return "fisv"
            elif self == stock.STOCK.STOCK_FIT:
                return "fit"
            elif self == stock.STOCK.STOCK_FITB:
                return "fitb"
            elif self == stock.STOCK.STOCK_FITBI:
                return "fitbi"
            elif self == stock.STOCK.STOCK_FIV:
                return "fiv"
            elif self == stock.STOCK.STOCK_FIVE:
                return "five"
            elif self == stock.STOCK.STOCK_FIVN:
                return "fivn"
            elif self == stock.STOCK.STOCK_FIX:
                return "fix"
            elif self == stock.STOCK.STOCK_FIXD:
                return "fixd"
            elif self == stock.STOCK.STOCK_FIZZ:
                return "fizz"
            elif self == stock.STOCK.STOCK_FL:
                return "fl"
            elif self == stock.STOCK.STOCK_FLAT:
                return "flat"
            elif self == stock.STOCK.STOCK_FLAU:
                return "flau"
            elif self == stock.STOCK.STOCK_FLBR:
                return "flbr"
            elif self == stock.STOCK.STOCK_FLC:
                return "flc"
            elif self == stock.STOCK.STOCK_FLCA:
                return "flca"
            elif self == stock.STOCK.STOCK_FLCH:
                return "flch"
            elif self == stock.STOCK.STOCK_FLCO:
                return "flco"
            elif self == stock.STOCK.STOCK_FLDM:
                return "fldm"
            elif self == stock.STOCK.STOCK_FLEU:
                return "fleu"
            elif self == stock.STOCK.STOCK_FLEX:
                return "flex"
            elif self == stock.STOCK.STOCK_FLGB:
                return "flgb"
            elif self == stock.STOCK.STOCK_FLGR:
                return "flgr"
            elif self == stock.STOCK.STOCK_FLGT:
                return "flgt"
            elif self == stock.STOCK.STOCK_FLHK:
                return "flhk"
            elif self == stock.STOCK.STOCK_FLIC:
                return "flic"
            elif self == stock.STOCK.STOCK_FLIO:
                return "flio"
            elif self == stock.STOCK.STOCK_FLIR:
                return "flir"
            elif self == stock.STOCK.STOCK_FLJH:
                return "fljh"
            elif self == stock.STOCK.STOCK_FLJP:
                return "fljp"
            elif self == stock.STOCK.STOCK_FLKR:
                return "flkr"
            elif self == stock.STOCK.STOCK_FLKS:
                return "flks"
            elif self == stock.STOCK.STOCK_FLL:
                return "fll"
            elif self == stock.STOCK.STOCK_FLLV:
                return "fllv"
            elif self == stock.STOCK.STOCK_FLMB:
                return "flmb"
            elif self == stock.STOCK.STOCK_FLMX:
                return "flmx"
            elif self == stock.STOCK.STOCK_FLO:
                return "flo"
            elif self == stock.STOCK.STOCK_FLOW:
                return "flow"
            elif self == stock.STOCK.STOCK_FLQD:
                return "flqd"
            elif self == stock.STOCK.STOCK_FLQE:
                return "flqe"
            elif self == stock.STOCK.STOCK_FLQG:
                return "flqg"
            elif self == stock.STOCK.STOCK_FLQH:
                return "flqh"
            elif self == stock.STOCK.STOCK_FLQL:
                return "flql"
            elif self == stock.STOCK.STOCK_FLQM:
                return "flqm"
            elif self == stock.STOCK.STOCK_FLQS:
                return "flqs"
            elif self == stock.STOCK.STOCK_FLR:
                return "flr"
            elif self == stock.STOCK.STOCK_FLS:
                return "fls"
            elif self == stock.STOCK.STOCK_FLT:
                return "flt"
            elif self == stock.STOCK.STOCK_FLWS:
                return "flws"
            elif self == stock.STOCK.STOCK_FLXN:
                return "flxn"
            elif self == stock.STOCK.STOCK_FLXS:
                return "flxs"
            elif self == stock.STOCK.STOCK_FLY:
                return "fly"
            elif self == stock.STOCK.STOCK_FMAO:
                return "fmao"
            elif self == stock.STOCK.STOCK_FMAX:
                return "fmax"
            elif self == stock.STOCK.STOCK_FMBH:
                return "fmbh"
            elif self == stock.STOCK.STOCK_FMBI:
                return "fmbi"
            elif self == stock.STOCK.STOCK_FMC:
                return "fmc"
            elif self == stock.STOCK.STOCK_FMCI:
                return "fmci"
            elif self == stock.STOCK.STOCK_FMCIR:
                return "fmcir"
            elif self == stock.STOCK.STOCK_FMCIU:
                return "fmciu"
            elif self == stock.STOCK.STOCK_FMCIW:
                return "fmciw"
            elif self == stock.STOCK.STOCK_FMDG:
                return "fmdg"
            elif self == stock.STOCK.STOCK_FMHI:
                return "fmhi"
            elif self == stock.STOCK.STOCK_FMI:
                return "fmi"
            elif self == stock.STOCK.STOCK_FMN:
                return "fmn"
            elif self == stock.STOCK.STOCK_FMNB:
                return "fmnb"
            elif self == stock.STOCK.STOCK_FMO:
                return "fmo"
            elif self == stock.STOCK.STOCK_FMS:
                return "fms"
            elif self == stock.STOCK.STOCK_FMSA:
                return "fmsa"
            elif self == stock.STOCK.STOCK_FMX:
                return "fmx"
            elif self == stock.STOCK.STOCK_FN:
                return "fn"
            elif self == stock.STOCK.STOCK_FNB:
                return "fnb"
            elif self == stock.STOCK.STOCK_FNBG:
                return "fnbg"
            elif self == stock.STOCK.STOCK_FNB_E:
                return "fnb_e"
            elif self == stock.STOCK.STOCK_FNCF:
                return "fncf"
            elif self == stock.STOCK.STOCK_FND:
                return "fnd"
            elif self == stock.STOCK.STOCK_FNF:
                return "fnf"
            elif self == stock.STOCK.STOCK_FNFV:
                return "fnfv"
            elif self == stock.STOCK.STOCK_FNG:
                return "fng"
            elif self == stock.STOCK.STOCK_FNGN:
                return "fngn"
            elif self == stock.STOCK.STOCK_FNHC:
                return "fnhc"
            elif self == stock.STOCK.STOCK_FNJN:
                return "fnjn"
            elif self == stock.STOCK.STOCK_FNKO:
                return "fnko"
            elif self == stock.STOCK.STOCK_FNLC:
                return "fnlc"
            elif self == stock.STOCK.STOCK_FNSR:
                return "fnsr"
            elif self == stock.STOCK.STOCK_FNTE:
                return "fnte"
            elif self == stock.STOCK.STOCK_FNTEU:
                return "fnteu"
            elif self == stock.STOCK.STOCK_FNTEW:
                return "fntew"
            elif self == stock.STOCK.STOCK_FNV:
                return "fnv"
            elif self == stock.STOCK.STOCK_FNWB:
                return "fnwb"
            elif self == stock.STOCK.STOCK_FOANC:
                return "foanc"
            elif self == stock.STOCK.STOCK_FOE:
                return "foe"
            elif self == stock.STOCK.STOCK_FOF:
                return "fof"
            elif self == stock.STOCK.STOCK_FOGO:
                return "fogo"
            elif self == stock.STOCK.STOCK_FOLD:
                return "fold"
            elif self == stock.STOCK.STOCK_FOMX:
                return "fomx"
            elif self == stock.STOCK.STOCK_FONR:
                return "fonr"
            elif self == stock.STOCK.STOCK_FOR:
                return "for"
            elif self == stock.STOCK.STOCK_FORD:
                return "ford"
            elif self == stock.STOCK.STOCK_FORK:
                return "fork"
            elif self == stock.STOCK.STOCK_FORM:
                return "form"
            elif self == stock.STOCK.STOCK_FORR:
                return "forr"
            elif self == stock.STOCK.STOCK_FORTY:
                return "forty"
            elif self == stock.STOCK.STOCK_FOSL:
                return "fosl"
            elif self == stock.STOCK.STOCK_FOX:
                return "fox"
            elif self == stock.STOCK.STOCK_FOXA:
                return "foxa"
            elif self == stock.STOCK.STOCK_FOXF:
                return "foxf"
            elif self == stock.STOCK.STOCK_FPAY:
                return "fpay"
            elif self == stock.STOCK.STOCK_FPEI:
                return "fpei"
            elif self == stock.STOCK.STOCK_FPH:
                return "fph"
            elif self == stock.STOCK.STOCK_FPI:
                return "fpi"
            elif self == stock.STOCK.STOCK_FPI_B:
                return "fpi_b"
            elif self == stock.STOCK.STOCK_FPP-WS:
                return "fpp-ws"
            elif self == stock.STOCK.STOCK_FPP:
                return "fpp"
            elif self == stock.STOCK.STOCK_FPRX:
                return "fprx"
            elif self == stock.STOCK.STOCK_FPT:
                return "fpt"
            elif self == stock.STOCK.STOCK_FQAL:
                return "fqal"
            elif self == stock.STOCK.STOCK_FR:
                return "fr"
            elif self == stock.STOCK.STOCK_FRA:
                return "fra"
            elif self == stock.STOCK.STOCK_FRAC:
                return "frac"
            elif self == stock.STOCK.STOCK_FRAN:
                return "fran"
            elif self == stock.STOCK.STOCK_FRBA:
                return "frba"
            elif self == stock.STOCK.STOCK_FRBK:
                return "frbk"
            elif self == stock.STOCK.STOCK_FRC:
                return "frc"
            elif self == stock.STOCK.STOCK_FRC_C:
                return "frc_c"
            elif self == stock.STOCK.STOCK_FRC_D:
                return "frc_d"
            elif self == stock.STOCK.STOCK_FRC_E:
                return "frc_e"
            elif self == stock.STOCK.STOCK_FRC_F:
                return "frc_f"
            elif self == stock.STOCK.STOCK_FRC_G:
                return "frc_g"
            elif self == stock.STOCK.STOCK_FRC_H:
                return "frc_h"
            elif self == stock.STOCK.STOCK_FRD:
                return "frd"
            elif self == stock.STOCK.STOCK_FRED:
                return "fred"
            elif self == stock.STOCK.STOCK_FRGI:
                return "frgi"
            elif self == stock.STOCK.STOCK_FRME:
                return "frme"
            elif self == stock.STOCK.STOCK_FRO:
                return "fro"
            elif self == stock.STOCK.STOCK_FRPH:
                return "frph"
            elif self == stock.STOCK.STOCK_FRPT:
                return "frpt"
            elif self == stock.STOCK.STOCK_FRSH:
                return "frsh"
            elif self == stock.STOCK.STOCK_FRSX:
                return "frsx"
            elif self == stock.STOCK.STOCK_FRT:
                return "frt"
            elif self == stock.STOCK.STOCK_FRTA:
                return "frta"
            elif self == stock.STOCK.STOCK_FRT_C:
                return "frt_c"
            elif self == stock.STOCK.STOCK_FSAC:
                return "fsac"
            elif self == stock.STOCK.STOCK_FSACU:
                return "fsacu"
            elif self == stock.STOCK.STOCK_FSACW:
                return "fsacw"
            elif self == stock.STOCK.STOCK_FSAM:
                return "fsam"
            elif self == stock.STOCK.STOCK_FSB:
                return "fsb"
            elif self == stock.STOCK.STOCK_FSBC:
                return "fsbc"
            elif self == stock.STOCK.STOCK_FSBK:
                return "fsbk"
            elif self == stock.STOCK.STOCK_FSBW:
                return "fsbw"
            elif self == stock.STOCK.STOCK_FSCT:
                return "fsct"
            elif self == stock.STOCK.STOCK_FSFG:
                return "fsfg"
            elif self == stock.STOCK.STOCK_FSI:
                return "fsi"
            elif self == stock.STOCK.STOCK_FSIC:
                return "fsic"
            elif self == stock.STOCK.STOCK_FSLR:
                return "fslr"
            elif self == stock.STOCK.STOCK_FSM:
                return "fsm"
            elif self == stock.STOCK.STOCK_FSNN:
                return "fsnn"
            elif self == stock.STOCK.STOCK_FSP:
                return "fsp"
            elif self == stock.STOCK.STOCK_FSS:
                return "fss"
            elif self == stock.STOCK.STOCK_FSTR:
                return "fstr"
            elif self == stock.STOCK.STOCK_FSV:
                return "fsv"
            elif self == stock.STOCK.STOCK_FT:
                return "ft"
            elif self == stock.STOCK.STOCK_FTAG:
                return "ftag"
            elif self == stock.STOCK.STOCK_FTAI:
                return "ftai"
            elif self == stock.STOCK.STOCK_FTD:
                return "ftd"
            elif self == stock.STOCK.STOCK_FTEK:
                return "ftek"
            elif self == stock.STOCK.STOCK_FTEO:
                return "fteo"
            elif self == stock.STOCK.STOCK_FTF:
                return "ftf"
            elif self == stock.STOCK.STOCK_FTFT:
                return "ftft"
            elif self == stock.STOCK.STOCK_FTI:
                return "fti"
            elif self == stock.STOCK.STOCK_FTK:
                return "ftk"
            elif self == stock.STOCK.STOCK_FTNT:
                return "ftnt"
            elif self == stock.STOCK.STOCK_FTR:
                return "ftr"
            elif self == stock.STOCK.STOCK_FTRI:
                return "ftri"
            elif self == stock.STOCK.STOCK_FTRPR:
                return "ftrpr"
            elif self == stock.STOCK.STOCK_FTS:
                return "fts"
            elif self == stock.STOCK.STOCK_FTV:
                return "ftv"
            elif self == stock.STOCK.STOCK_FTVA:
                return "ftva"
            elif self == stock.STOCK.STOCK_FTXD:
                return "ftxd"
            elif self == stock.STOCK.STOCK_FTXG:
                return "ftxg"
            elif self == stock.STOCK.STOCK_FTXH:
                return "ftxh"
            elif self == stock.STOCK.STOCK_FTXL:
                return "ftxl"
            elif self == stock.STOCK.STOCK_FTXN:
                return "ftxn"
            elif self == stock.STOCK.STOCK_FTXO:
                return "ftxo"
            elif self == stock.STOCK.STOCK_FTXR:
                return "ftxr"
            elif self == stock.STOCK.STOCK_FUL:
                return "ful"
            elif self == stock.STOCK.STOCK_FULLL:
                return "fulll"
            elif self == stock.STOCK.STOCK_FULT:
                return "fult"
            elif self == stock.STOCK.STOCK_FUN:
                return "fun"
            elif self == stock.STOCK.STOCK_FUNC:
                return "func"
            elif self == stock.STOCK.STOCK_FUND:
                return "fund"
            elif self == stock.STOCK.STOCK_FUSB:
                return "fusb"
            elif self == stock.STOCK.STOCK_FUT:
                return "fut"
            elif self == stock.STOCK.STOCK_FUV:
                return "fuv"
            elif self == stock.STOCK.STOCK_FVAL:
                return "fval"
            elif self == stock.STOCK.STOCK_FVC:
                return "fvc"
            elif self == stock.STOCK.STOCK_FVE:
                return "fve"
            elif self == stock.STOCK.STOCK_FWONA:
                return "fwona"
            elif self == stock.STOCK.STOCK_FWONK:
                return "fwonk"
            elif self == stock.STOCK.STOCK_FWP:
                return "fwp"
            elif self == stock.STOCK.STOCK_FWRD:
                return "fwrd"
            elif self == stock.STOCK.STOCK_FXEP:
                return "fxep"
            elif self == stock.STOCK.STOCK_FXJP:
                return "fxjp"
            elif self == stock.STOCK.STOCK_G:
                return "g"
            elif self == stock.STOCK.STOCK_GAB:
                return "gab"
            elif self == stock.STOCK.STOCK_GABC:
                return "gabc"
            elif self == stock.STOCK.STOCK_GABR:
                return "gabr"
            elif self == stock.STOCK.STOCK_GABRW:
                return "gabrw"
            elif self == stock.STOCK.STOCK_GAB_D:
                return "gab_d"
            elif self == stock.STOCK.STOCK_GAB_G:
                return "gab_g"
            elif self == stock.STOCK.STOCK_GAB_H:
                return "gab_h"
            elif self == stock.STOCK.STOCK_GAB_J:
                return "gab_j"
            elif self == stock.STOCK.STOCK_GAIA:
                return "gaia"
            elif self == stock.STOCK.STOCK_GAIN:
                return "gain"
            elif self == stock.STOCK.STOCK_GAINM:
                return "gainm"
            elif self == stock.STOCK.STOCK_GAINN:
                return "gainn"
            elif self == stock.STOCK.STOCK_GAINO:
                return "gaino"
            elif self == stock.STOCK.STOCK_GALE:
                return "gale"
            elif self == stock.STOCK.STOCK_GALT:
                return "galt"
            elif self == stock.STOCK.STOCK_GAM:
                return "gam"
            elif self == stock.STOCK.STOCK_GAMR:
                return "gamr"
            elif self == stock.STOCK.STOCK_GAM_B:
                return "gam_b"
            elif self == stock.STOCK.STOCK_GARD:
                return "gard"
            elif self == stock.STOCK.STOCK_GARS:
                return "gars"
            elif self == stock.STOCK.STOCK_GASS:
                return "gass"
            elif self == stock.STOCK.STOCK_GASX:
                return "gasx"
            elif self == stock.STOCK.STOCK_GATX:
                return "gatx"
            elif self == stock.STOCK.STOCK_GAZB:
                return "gazb"
            elif self == stock.STOCK.STOCK_GBAB:
                return "gbab"
            elif self == stock.STOCK.STOCK_GBCI:
                return "gbci"
            elif self == stock.STOCK.STOCK_GBDC:
                return "gbdc"
            elif self == stock.STOCK.STOCK_GBIL:
                return "gbil"
            elif self == stock.STOCK.STOCK_GBL:
                return "gbl"
            elif self == stock.STOCK.STOCK_GBLI:
                return "gbli"
            elif self == stock.STOCK.STOCK_GBLIL:
                return "gblil"
            elif self == stock.STOCK.STOCK_GBLIZ:
                return "gbliz"
            elif self == stock.STOCK.STOCK_GBNK:
                return "gbnk"
            elif self == stock.STOCK.STOCK_GBR:
                return "gbr"
            elif self == stock.STOCK.STOCK_GBT:
                return "gbt"
            elif self == stock.STOCK.STOCK_GBX:
                return "gbx"
            elif self == stock.STOCK.STOCK_GCAP:
                return "gcap"
            elif self == stock.STOCK.STOCK_GCBC:
                return "gcbc"
            elif self == stock.STOCK.STOCK_GCH:
                return "gch"
            elif self == stock.STOCK.STOCK_GCI:
                return "gci"
            elif self == stock.STOCK.STOCK_GCO:
                return "gco"
            elif self == stock.STOCK.STOCK_GCOW:
                return "gcow"
            elif self == stock.STOCK.STOCK_GCP:
                return "gcp"
            elif self == stock.STOCK.STOCK_GCV:
                return "gcv"
            elif self == stock.STOCK.STOCK_GCVRZ:
                return "gcvrz"
            elif self == stock.STOCK.STOCK_GCV_B:
                return "gcv_b"
            elif self == stock.STOCK.STOCK_GD:
                return "gd"
            elif self == stock.STOCK.STOCK_GDDY:
                return "gddy"
            elif self == stock.STOCK.STOCK_GDEN:
                return "gden"
            elif self == stock.STOCK.STOCK_GDI:
                return "gdi"
            elif self == stock.STOCK.STOCK_GDL:
                return "gdl"
            elif self == stock.STOCK.STOCK_GDL_B:
                return "gdl_b"
            elif self == stock.STOCK.STOCK_GDO:
                return "gdo"
            elif self == stock.STOCK.STOCK_GDOT:
                return "gdot"
            elif self == stock.STOCK.STOCK_GDP:
                return "gdp"
            elif self == stock.STOCK.STOCK_GDS:
                return "gds"
            elif self == stock.STOCK.STOCK_GDV:
                return "gdv"
            elif self == stock.STOCK.STOCK_GDVD:
                return "gdvd"
            elif self == stock.STOCK.STOCK_GDV_A:
                return "gdv_a"
            elif self == stock.STOCK.STOCK_GDV_D:
                return "gdv_d"
            elif self == stock.STOCK.STOCK_GDV_G:
                return "gdv_g"
            elif self == stock.STOCK.STOCK_GE:
                return "ge"
            elif self == stock.STOCK.STOCK_GEB:
                return "geb"
            elif self == stock.STOCK.STOCK_GEC:
                return "gec"
            elif self == stock.STOCK.STOCK_GECC:
                return "gecc"
            elif self == stock.STOCK.STOCK_GECCL:
                return "geccl"
            elif self == stock.STOCK.STOCK_GEF-B:
                return "gef-b"
            elif self == stock.STOCK.STOCK_GEF:
                return "gef"
            elif self == stock.STOCK.STOCK_GEH:
                return "geh"
            elif self == stock.STOCK.STOCK_GEK:
                return "gek"
            elif self == stock.STOCK.STOCK_GEL:
                return "gel"
            elif self == stock.STOCK.STOCK_GEM:
                return "gem"
            elif self == stock.STOCK.STOCK_GEMP:
                return "gemp"
            elif self == stock.STOCK.STOCK_GEN:
                return "gen"
            elif self == stock.STOCK.STOCK_GENC:
                return "genc"
            elif self == stock.STOCK.STOCK_GENE:
                return "gene"
            elif self == stock.STOCK.STOCK_GENY:
                return "geny"
            elif self == stock.STOCK.STOCK_GEO:
                return "geo"
            elif self == stock.STOCK.STOCK_GEOS:
                return "geos"
            elif self == stock.STOCK.STOCK_GER:
                return "ger"
            elif self == stock.STOCK.STOCK_GERN:
                return "gern"
            elif self == stock.STOCK.STOCK_GES:
                return "ges"
            elif self == stock.STOCK.STOCK_GEVO:
                return "gevo"
            elif self == stock.STOCK.STOCK_GF:
                return "gf"
            elif self == stock.STOCK.STOCK_GFA:
                return "gfa"
            elif self == stock.STOCK.STOCK_GFED:
                return "gfed"
            elif self == stock.STOCK.STOCK_GFF:
                return "gff"
            elif self == stock.STOCK.STOCK_GFI:
                return "gfi"
            elif self == stock.STOCK.STOCK_GFN:
                return "gfn"
            elif self == stock.STOCK.STOCK_GFNCP:
                return "gfncp"
            elif self == stock.STOCK.STOCK_GFNSL:
                return "gfnsl"
            elif self == stock.STOCK.STOCK_GFY:
                return "gfy"
            elif self == stock.STOCK.STOCK_GG:
                return "gg"
            elif self == stock.STOCK.STOCK_GGAL:
                return "ggal"
            elif self == stock.STOCK.STOCK_GGB:
                return "ggb"
            elif self == stock.STOCK.STOCK_GGG:
                return "ggg"
            elif self == stock.STOCK.STOCK_GGM:
                return "ggm"
            elif self == stock.STOCK.STOCK_GGN:
                return "ggn"
            elif self == stock.STOCK.STOCK_GGN_B:
                return "ggn_b"
            elif self == stock.STOCK.STOCK_GGO:
                return "ggo"
            elif self == stock.STOCK.STOCK_GGO_A:
                return "ggo_a"
            elif self == stock.STOCK.STOCK_GGP:
                return "ggp"
            elif self == stock.STOCK.STOCK_GGP_A:
                return "ggp_a"
            elif self == stock.STOCK.STOCK_GGT:
                return "ggt"
            elif self == stock.STOCK.STOCK_GGT_B:
                return "ggt_b"
            elif self == stock.STOCK.STOCK_GGT_E:
                return "ggt_e"
            elif self == stock.STOCK.STOCK_GGZ:
                return "ggz"
            elif self == stock.STOCK.STOCK_GGZR:
                return "ggzr"
            elif self == stock.STOCK.STOCK_GGZRW:
                return "ggzrw"
            elif self == stock.STOCK.STOCK_GGZ_A:
                return "ggz_a"
            elif self == stock.STOCK.STOCK_GHC:
                return "ghc"
            elif self == stock.STOCK.STOCK_GHDX:
                return "ghdx"
            elif self == stock.STOCK.STOCK_GHL:
                return "ghl"
            elif self == stock.STOCK.STOCK_GHM:
                return "ghm"
            elif self == stock.STOCK.STOCK_GHS:
                return "ghs"
            elif self == stock.STOCK.STOCK_GHY:
                return "ghy"
            elif self == stock.STOCK.STOCK_GHYB:
                return "ghyb"
            elif self == stock.STOCK.STOCK_GHYG:
                return "ghyg"
            elif self == stock.STOCK.STOCK_GIB:
                return "gib"
            elif self == stock.STOCK.STOCK_GIFI:
                return "gifi"
            elif self == stock.STOCK.STOCK_GIGA:
                return "giga"
            elif self == stock.STOCK.STOCK_GIGB:
                return "gigb"
            elif self == stock.STOCK.STOCK_GIGM:
                return "gigm"
            elif self == stock.STOCK.STOCK_GIII:
                return "giii"
            elif self == stock.STOCK.STOCK_GIL:
                return "gil"
            elif self == stock.STOCK.STOCK_GILD:
                return "gild"
            elif self == stock.STOCK.STOCK_GILT:
                return "gilt"
            elif self == stock.STOCK.STOCK_GIM:
                return "gim"
            elif self == stock.STOCK.STOCK_GIMO:
                return "gimo"
            elif self == stock.STOCK.STOCK_GIS:
                return "gis"
            elif self == stock.STOCK.STOCK_GJH:
                return "gjh"
            elif self == stock.STOCK.STOCK_GJO:
                return "gjo"
            elif self == stock.STOCK.STOCK_GJP:
                return "gjp"
            elif self == stock.STOCK.STOCK_GJR:
                return "gjr"
            elif self == stock.STOCK.STOCK_GJS:
                return "gjs"
            elif self == stock.STOCK.STOCK_GJT:
                return "gjt"
            elif self == stock.STOCK.STOCK_GJV:
                return "gjv"
            elif self == stock.STOCK.STOCK_GKOS:
                return "gkos"
            elif self == stock.STOCK.STOCK_GLAD:
                return "glad"
            elif self == stock.STOCK.STOCK_GLADN:
                return "gladn"
            elif self == stock.STOCK.STOCK_GLBL:
                return "glbl"
            elif self == stock.STOCK.STOCK_GLBR:
                return "glbr"
            elif self == stock.STOCK.STOCK_GLBS:
                return "glbs"
            elif self == stock.STOCK.STOCK_GLBZ:
                return "glbz"
            elif self == stock.STOCK.STOCK_GLDD:
                return "gldd"
            elif self == stock.STOCK.STOCK_GLDW:
                return "gldw"
            elif self == stock.STOCK.STOCK_GLMD:
                return "glmd"
            elif self == stock.STOCK.STOCK_GLNG:
                return "glng"
            elif self == stock.STOCK.STOCK_GLO:
                return "glo"
            elif self == stock.STOCK.STOCK_GLOB:
                return "glob"
            elif self == stock.STOCK.STOCK_GLOG:
                return "glog"
            elif self == stock.STOCK.STOCK_GLOG_A:
                return "glog_a"
            elif self == stock.STOCK.STOCK_GLOP:
                return "glop"
            elif self == stock.STOCK.STOCK_GLOP_A:
                return "glop_a"
            elif self == stock.STOCK.STOCK_GLOW:
                return "glow"
            elif self == stock.STOCK.STOCK_GLP:
                return "glp"
            elif self == stock.STOCK.STOCK_GLPG:
                return "glpg"
            elif self == stock.STOCK.STOCK_GLPI:
                return "glpi"
            elif self == stock.STOCK.STOCK_GLQ:
                return "glq"
            elif self == stock.STOCK.STOCK_GLRE:
                return "glre"
            elif self == stock.STOCK.STOCK_GLT:
                return "glt"
            elif self == stock.STOCK.STOCK_GLU:
                return "glu"
            elif self == stock.STOCK.STOCK_GLUU:
                return "gluu"
            elif self == stock.STOCK.STOCK_GLU_A:
                return "glu_a"
            elif self == stock.STOCK.STOCK_GLV:
                return "glv"
            elif self == stock.STOCK.STOCK_GLW:
                return "glw"
            elif self == stock.STOCK.STOCK_GLYC:
                return "glyc"
            elif self == stock.STOCK.STOCK_GM-WS-B:
                return "gm-ws-b"
            elif self == stock.STOCK.STOCK_GM:
                return "gm"
            elif self == stock.STOCK.STOCK_GME:
                return "gme"
            elif self == stock.STOCK.STOCK_GMED:
                return "gmed"
            elif self == stock.STOCK.STOCK_GMFL:
                return "gmfl"
            elif self == stock.STOCK.STOCK_GMLP:
                return "gmlp"
            elif self == stock.STOCK.STOCK_GMLPP:
                return "gmlpp"
            elif self == stock.STOCK.STOCK_GMO:
                return "gmo"
            elif self == stock.STOCK.STOCK_GMRE:
                return "gmre"
            elif self == stock.STOCK.STOCK_GMRE_A:
                return "gmre_a"
            elif self == stock.STOCK.STOCK_GMS:
                return "gms"
            elif self == stock.STOCK.STOCK_GMTA:
                return "gmta"
            elif self == stock.STOCK.STOCK_GMZ:
                return "gmz"
            elif self == stock.STOCK.STOCK_GNBC:
                return "gnbc"
            elif self == stock.STOCK.STOCK_GNC:
                return "gnc"
            elif self == stock.STOCK.STOCK_GNCA:
                return "gnca"
            elif self == stock.STOCK.STOCK_GNCMA:
                return "gncma"
            elif self == stock.STOCK.STOCK_GNE:
                return "gne"
            elif self == stock.STOCK.STOCK_GNE_A:
                return "gne_a"
            elif self == stock.STOCK.STOCK_GNK:
                return "gnk"
            elif self == stock.STOCK.STOCK_GNL:
                return "gnl"
            elif self == stock.STOCK.STOCK_GNL_A:
                return "gnl_a"
            elif self == stock.STOCK.STOCK_GNMK:
                return "gnmk"
            elif self == stock.STOCK.STOCK_GNMX:
                return "gnmx"
            elif self == stock.STOCK.STOCK_GNRC:
                return "gnrc"
            elif self == stock.STOCK.STOCK_GNRT:
                return "gnrt"
            elif self == stock.STOCK.STOCK_GNRX:
                return "gnrx"
            elif self == stock.STOCK.STOCK_GNST:
                return "gnst"
            elif self == stock.STOCK.STOCK_GNT:
                return "gnt"
            elif self == stock.STOCK.STOCK_GNTX:
                return "gntx"
            elif self == stock.STOCK.STOCK_GNTY:
                return "gnty"
            elif self == stock.STOCK.STOCK_GNT_A:
                return "gnt_a"
            elif self == stock.STOCK.STOCK_GNUS:
                return "gnus"
            elif self == stock.STOCK.STOCK_GNW:
                return "gnw"
            elif self == stock.STOCK.STOCK_GOAU:
                return "goau"
            elif self == stock.STOCK.STOCK_GOEX:
                return "goex"
            elif self == stock.STOCK.STOCK_GOF:
                return "gof"
            elif self == stock.STOCK.STOCK_GOGL:
                return "gogl"
            elif self == stock.STOCK.STOCK_GOGO:
                return "gogo"
            elif self == stock.STOCK.STOCK_GOL:
                return "gol"
            elif self == stock.STOCK.STOCK_GOLD:
                return "gold"
            elif self == stock.STOCK.STOCK_GOLF:
                return "golf"
            elif self == stock.STOCK.STOCK_GOOD:
                return "good"
            elif self == stock.STOCK.STOCK_GOODM:
                return "goodm"
            elif self == stock.STOCK.STOCK_GOODO:
                return "goodo"
            elif self == stock.STOCK.STOCK_GOODP:
                return "goodp"
            elif self == stock.STOCK.STOCK_GOOG:
                return "goog"
            elif self == stock.STOCK.STOCK_GOOGL:
                return "googl"
            elif self == stock.STOCK.STOCK_GOOS:
                return "goos"
            elif self == stock.STOCK.STOCK_GOP:
                return "gop"
            elif self == stock.STOCK.STOCK_GORO:
                return "goro"
            elif self == stock.STOCK.STOCK_GOV:
                return "gov"
            elif self == stock.STOCK.STOCK_GOVNI:
                return "govni"
            elif self == stock.STOCK.STOCK_GPAC:
                return "gpac"
            elif self == stock.STOCK.STOCK_GPACU:
                return "gpacu"
            elif self == stock.STOCK.STOCK_GPACW:
                return "gpacw"
            elif self == stock.STOCK.STOCK_GPC:
                return "gpc"
            elif self == stock.STOCK.STOCK_GPE_A-CL:
                return "gpe_a-cl"
            elif self == stock.STOCK.STOCK_GPI:
                return "gpi"
            elif self == stock.STOCK.STOCK_GPIC:
                return "gpic"
            elif self == stock.STOCK.STOCK_GPJA:
                return "gpja"
            elif self == stock.STOCK.STOCK_GPK:
                return "gpk"
            elif self == stock.STOCK.STOCK_GPL:
                return "gpl"
            elif self == stock.STOCK.STOCK_GPM:
                return "gpm"
            elif self == stock.STOCK.STOCK_GPMT:
                return "gpmt"
            elif self == stock.STOCK.STOCK_GPMTW:
                return "gpmtw"
            elif self == stock.STOCK.STOCK_GPN:
                return "gpn"
            elif self == stock.STOCK.STOCK_GPOR:
                return "gpor"
            elif self == stock.STOCK.STOCK_GPP:
                return "gpp"
            elif self == stock.STOCK.STOCK_GPRE:
                return "gpre"
            elif self == stock.STOCK.STOCK_GPRK:
                return "gprk"
            elif self == stock.STOCK.STOCK_GPRO:
                return "gpro"
            elif self == stock.STOCK.STOCK_GPS:
                return "gps"
            elif self == stock.STOCK.STOCK_GPT:
                return "gpt"
            elif self == stock.STOCK.STOCK_GPT_A:
                return "gpt_a"
            elif self == stock.STOCK.STOCK_GPX:
                return "gpx"
            elif self == stock.STOCK.STOCK_GRA:
                return "gra"
            elif self == stock.STOCK.STOCK_GRAM:
                return "gram"
            elif self == stock.STOCK.STOCK_GRBK:
                return "grbk"
            elif self == stock.STOCK.STOCK_GRC:
                return "grc"
            elif self == stock.STOCK.STOCK_GRF:
                return "grf"
            elif self == stock.STOCK.STOCK_GRFS:
                return "grfs"
            elif self == stock.STOCK.STOCK_GRIF:
                return "grif"
            elif self == stock.STOCK.STOCK_GRMN:
                return "grmn"
            elif self == stock.STOCK.STOCK_GRMY:
                return "grmy"
            elif self == stock.STOCK.STOCK_GRNB:
                return "grnb"
            elif self == stock.STOCK.STOCK_GROW:
                return "grow"
            elif self == stock.STOCK.STOCK_GRP-U:
                return "grp-u"
            elif self == stock.STOCK.STOCK_GRPN:
                return "grpn"
            elif self == stock.STOCK.STOCK_GRR:
                return "grr"
            elif self == stock.STOCK.STOCK_GRUB:
                return "grub"
            elif self == stock.STOCK.STOCK_GRVY:
                return "grvy"
            elif self == stock.STOCK.STOCK_GRX:
                return "grx"
            elif self == stock.STOCK.STOCK_GRX_A:
                return "grx_a"
            elif self == stock.STOCK.STOCK_GRX_B:
                return "grx_b"
            elif self == stock.STOCK.STOCK_GS:
                return "gs"
            elif self == stock.STOCK.STOCK_GSAT:
                return "gsat"
            elif self == stock.STOCK.STOCK_GSB:
                return "gsb"
            elif self == stock.STOCK.STOCK_GSBC:
                return "gsbc"
            elif self == stock.STOCK.STOCK_GSBD:
                return "gsbd"
            elif self == stock.STOCK.STOCK_GSD:
                return "gsd"
            elif self == stock.STOCK.STOCK_GSEU:
                return "gseu"
            elif self == stock.STOCK.STOCK_GSEW:
                return "gsew"
            elif self == stock.STOCK.STOCK_GSH:
                return "gsh"
            elif self == stock.STOCK.STOCK_GSHT:
                return "gsht"
            elif self == stock.STOCK.STOCK_GSHTU:
                return "gshtu"
            elif self == stock.STOCK.STOCK_GSHTW:
                return "gshtw"
            elif self == stock.STOCK.STOCK_GSIE:
                return "gsie"
            elif self == stock.STOCK.STOCK_GSIT:
                return "gsit"
            elif self == stock.STOCK.STOCK_GSJY:
                return "gsjy"
            elif self == stock.STOCK.STOCK_GSK:
                return "gsk"
            elif self == stock.STOCK.STOCK_GSL:
                return "gsl"
            elif self == stock.STOCK.STOCK_GSLC:
                return "gslc"
            elif self == stock.STOCK.STOCK_GSL_B:
                return "gsl_b"
            elif self == stock.STOCK.STOCK_GSM:
                return "gsm"
            elif self == stock.STOCK.STOCK_GSS:
                return "gss"
            elif self == stock.STOCK.STOCK_GSSC:
                return "gssc"
            elif self == stock.STOCK.STOCK_GST:
                return "gst"
            elif self == stock.STOCK.STOCK_GST_A:
                return "gst_a"
            elif self == stock.STOCK.STOCK_GST_B:
                return "gst_b"
            elif self == stock.STOCK.STOCK_GSUM:
                return "gsum"
            elif self == stock.STOCK.STOCK_GSV:
                return "gsv"
            elif self == stock.STOCK.STOCK_GSVC:
                return "gsvc"
            elif self == stock.STOCK.STOCK_GS_A:
                return "gs_a"
            elif self == stock.STOCK.STOCK_GS_B:
                return "gs_b"
            elif self == stock.STOCK.STOCK_GS_C:
                return "gs_c"
            elif self == stock.STOCK.STOCK_GS_D:
                return "gs_d"
            elif self == stock.STOCK.STOCK_GS_I-CL:
                return "gs_i-cl"
            elif self == stock.STOCK.STOCK_GS_I:
                return "gs_i"
            elif self == stock.STOCK.STOCK_GS_J:
                return "gs_j"
            elif self == stock.STOCK.STOCK_GS_K:
                return "gs_k"
            elif self == stock.STOCK.STOCK_GS_N:
                return "gs_n"
            elif self == stock.STOCK.STOCK_GT:
                return "gt"
            elif self == stock.STOCK.STOCK_GTE:
                return "gte"
            elif self == stock.STOCK.STOCK_GTHX:
                return "gthx"
            elif self == stock.STOCK.STOCK_GTIM:
                return "gtim"
            elif self == stock.STOCK.STOCK_GTLS:
                return "gtls"
            elif self == stock.STOCK.STOCK_GTN-A:
                return "gtn-a"
            elif self == stock.STOCK.STOCK_GTN:
                return "gtn"
            elif self == stock.STOCK.STOCK_GTO:
                return "gto"
            elif self == stock.STOCK.STOCK_GTS:
                return "gts"
            elif self == stock.STOCK.STOCK_GTT:
                return "gtt"
            elif self == stock.STOCK.STOCK_GTXI:
                return "gtxi"
            elif self == stock.STOCK.STOCK_GTY:
                return "gty"
            elif self == stock.STOCK.STOCK_GTYH:
                return "gtyh"
            elif self == stock.STOCK.STOCK_GTYHU:
                return "gtyhu"
            elif self == stock.STOCK.STOCK_GTYHW:
                return "gtyhw"
            elif self == stock.STOCK.STOCK_GUDB:
                return "gudb"
            elif self == stock.STOCK.STOCK_GURE:
                return "gure"
            elif self == stock.STOCK.STOCK_GUT:
                return "gut"
            elif self == stock.STOCK.STOCK_GUT_A:
                return "gut_a"
            elif self == stock.STOCK.STOCK_GUT_C:
                return "gut_c"
            elif self == stock.STOCK.STOCK_GV:
                return "gv"
            elif self == stock.STOCK.STOCK_GVA:
                return "gva"
            elif self == stock.STOCK.STOCK_GVIP:
                return "gvip"
            elif self == stock.STOCK.STOCK_GVP:
                return "gvp"
            elif self == stock.STOCK.STOCK_GWB:
                return "gwb"
            elif self == stock.STOCK.STOCK_GWGH:
                return "gwgh"
            elif self == stock.STOCK.STOCK_GWPH:
                return "gwph"
            elif self == stock.STOCK.STOCK_GWR:
                return "gwr"
            elif self == stock.STOCK.STOCK_GWRE:
                return "gwre"
            elif self == stock.STOCK.STOCK_GWRS:
                return "gwrs"
            elif self == stock.STOCK.STOCK_GWW:
                return "gww"
            elif self == stock.STOCK.STOCK_GXP:
                return "gxp"
            elif self == stock.STOCK.STOCK_GYB:
                return "gyb"
            elif self == stock.STOCK.STOCK_GYC:
                return "gyc"
            elif self == stock.STOCK.STOCK_GYRO:
                return "gyro"
            elif self == stock.STOCK.STOCK_GZT:
                return "gzt"
            elif self == stock.STOCK.STOCK_H:
                return "h"
            elif self == stock.STOCK.STOCK_HA:
                return "ha"
            elif self == stock.STOCK.STOCK_HABT:
                return "habt"
            elif self == stock.STOCK.STOCK_HACK:
                return "hack"
            elif self == stock.STOCK.STOCK_HACV:
                return "hacv"
            elif self == stock.STOCK.STOCK_HACW:
                return "hacw"
            elif self == stock.STOCK.STOCK_HAE:
                return "hae"
            elif self == stock.STOCK.STOCK_HAFC:
                return "hafc"
            elif self == stock.STOCK.STOCK_HAHA:
                return "haha"
            elif self == stock.STOCK.STOCK_HAIN:
                return "hain"
            elif self == stock.STOCK.STOCK_HAIR:
                return "hair"
            elif self == stock.STOCK.STOCK_HAL:
                return "hal"
            elif self == stock.STOCK.STOCK_HALL:
                return "hall"
            elif self == stock.STOCK.STOCK_HALO:
                return "halo"
            elif self == stock.STOCK.STOCK_HAS:
                return "has"
            elif self == stock.STOCK.STOCK_HASI:
                return "hasi"
            elif self == stock.STOCK.STOCK_HAUD:
                return "haud"
            elif self == stock.STOCK.STOCK_HAWK:
                return "hawk"
            elif self == stock.STOCK.STOCK_HAWX:
                return "hawx"
            elif self == stock.STOCK.STOCK_HAYN:
                return "hayn"
            elif self == stock.STOCK.STOCK_HAYU:
                return "hayu"
            elif self == stock.STOCK.STOCK_HBAN:
                return "hban"
            elif self == stock.STOCK.STOCK_HBANN:
                return "hbann"
            elif self == stock.STOCK.STOCK_HBANO:
                return "hbano"
            elif self == stock.STOCK.STOCK_HBANP:
                return "hbanp"
            elif self == stock.STOCK.STOCK_HBB:
                return "hbb"
            elif self == stock.STOCK.STOCK_HBCP:
                return "hbcp"
            elif self == stock.STOCK.STOCK_HBHC:
                return "hbhc"
            elif self == stock.STOCK.STOCK_HBHCL:
                return "hbhcl"
            elif self == stock.STOCK.STOCK_HBI:
                return "hbi"
            elif self == stock.STOCK.STOCK_HBIO:
                return "hbio"
            elif self == stock.STOCK.STOCK_HBK:
                return "hbk"
            elif self == stock.STOCK.STOCK_HBM-WS:
                return "hbm-ws"
            elif self == stock.STOCK.STOCK_HBM:
                return "hbm"
            elif self == stock.STOCK.STOCK_HBMD:
                return "hbmd"
            elif self == stock.STOCK.STOCK_HBNC:
                return "hbnc"
            elif self == stock.STOCK.STOCK_HBP:
                return "hbp"
            elif self == stock.STOCK.STOCK_HCA:
                return "hca"
            elif self == stock.STOCK.STOCK_HCAC-U:
                return "hcac-u"
            elif self == stock.STOCK.STOCK_HCAC-WS:
                return "hcac-ws"
            elif self == stock.STOCK.STOCK_HCAC:
                return "hcac"
            elif self == stock.STOCK.STOCK_HCAP:
                return "hcap"
            elif self == stock.STOCK.STOCK_HCAPZ:
                return "hcapz"
            elif self == stock.STOCK.STOCK_HCC:
                return "hcc"
            elif self == stock.STOCK.STOCK_HCCI:
                return "hcci"
            elif self == stock.STOCK.STOCK_HCHC:
                return "hchc"
            elif self == stock.STOCK.STOCK_HCI:
                return "hci"
            elif self == stock.STOCK.STOCK_HCKT:
                return "hckt"
            elif self == stock.STOCK.STOCK_HCLP:
                return "hclp"
            elif self == stock.STOCK.STOCK_HCM:
                return "hcm"
            elif self == stock.STOCK.STOCK_HCN:
                return "hcn"
            elif self == stock.STOCK.STOCK_HCN_I:
                return "hcn_i"
            elif self == stock.STOCK.STOCK_HCOM:
                return "hcom"
            elif self == stock.STOCK.STOCK_HCP:
                return "hcp"
            elif self == stock.STOCK.STOCK_HCRF:
                return "hcrf"
            elif self == stock.STOCK.STOCK_HCSG:
                return "hcsg"
            elif self == stock.STOCK.STOCK_HD:
                return "hd"
            elif self == stock.STOCK.STOCK_HDAW:
                return "hdaw"
            elif self == stock.STOCK.STOCK_HDB:
                return "hdb"
            elif self == stock.STOCK.STOCK_HDEE:
                return "hdee"
            elif self == stock.STOCK.STOCK_HDEF:
                return "hdef"
            elif self == stock.STOCK.STOCK_HDEZ:
                return "hdez"
            elif self == stock.STOCK.STOCK_HDLV:
                return "hdlv"
            elif self == stock.STOCK.STOCK_HDMV:
                return "hdmv"
            elif self == stock.STOCK.STOCK_HDNG:
                return "hdng"
            elif self == stock.STOCK.STOCK_HDP:
                return "hdp"
            elif self == stock.STOCK.STOCK_HDRW:
                return "hdrw"
            elif self == stock.STOCK.STOCK_HDS:
                return "hds"
            elif self == stock.STOCK.STOCK_HDSN:
                return "hdsn"
            elif self == stock.STOCK.STOCK_HE:
                return "he"
            elif self == stock.STOCK.STOCK_HEAR:
                return "hear"
            elif self == stock.STOCK.STOCK_HEB:
                return "heb"
            elif self == stock.STOCK.STOCK_HEBT:
                return "hebt"
            elif self == stock.STOCK.STOCK_HEES:
                return "hees"
            elif self == stock.STOCK.STOCK_HEFV:
                return "hefv"
            elif self == stock.STOCK.STOCK_HEI-A:
                return "hei-a"
            elif self == stock.STOCK.STOCK_HEI:
                return "hei"
            elif self == stock.STOCK.STOCK_HELE:
                return "hele"
            elif self == stock.STOCK.STOCK_HEMV:
                return "hemv"
            elif self == stock.STOCK.STOCK_HEP:
                return "hep"
            elif self == stock.STOCK.STOCK_HEQ:
                return "heq"
            elif self == stock.STOCK.STOCK_HES:
                return "hes"
            elif self == stock.STOCK.STOCK_HESM:
                return "hesm"
            elif self == stock.STOCK.STOCK_HES_A:
                return "hes_a"
            elif self == stock.STOCK.STOCK_HEUS:
                return "heus"
            elif self == stock.STOCK.STOCK_HEUV:
                return "heuv"
            elif self == stock.STOCK.STOCK_HEWC:
                return "hewc"
            elif self == stock.STOCK.STOCK_HEWI:
                return "hewi"
            elif self == stock.STOCK.STOCK_HEWL:
                return "hewl"
            elif self == stock.STOCK.STOCK_HEWP:
                return "hewp"
            elif self == stock.STOCK.STOCK_HEWU:
                return "hewu"
            elif self == stock.STOCK.STOCK_HEWW:
                return "heww"
            elif self == stock.STOCK.STOCK_HEWY:
                return "hewy"
            elif self == stock.STOCK.STOCK_HE_U:
                return "he_u"
            elif self == stock.STOCK.STOCK_HF:
                return "hf"
            elif self == stock.STOCK.STOCK_HFBC:
                return "hfbc"
            elif self == stock.STOCK.STOCK_HFBL:
                return "hfbl"
            elif self == stock.STOCK.STOCK_HFC:
                return "hfc"
            elif self == stock.STOCK.STOCK_HFRO:
                return "hfro"
            elif self == stock.STOCK.STOCK_HFWA:
                return "hfwa"
            elif self == stock.STOCK.STOCK_HFXE:
                return "hfxe"
            elif self == stock.STOCK.STOCK_HFXI:
                return "hfxi"
            elif self == stock.STOCK.STOCK_HFXJ:
                return "hfxj"
            elif self == stock.STOCK.STOCK_HGH:
                return "hgh"
            elif self == stock.STOCK.STOCK_HGSD:
                return "hgsd"
            elif self == stock.STOCK.STOCK_HGSH:
                return "hgsh"
            elif self == stock.STOCK.STOCK_HGT:
                return "hgt"
            elif self == stock.STOCK.STOCK_HGV:
                return "hgv"
            elif self == stock.STOCK.STOCK_HHC:
                return "hhc"
            elif self == stock.STOCK.STOCK_HHS:
                return "hhs"
            elif self == stock.STOCK.STOCK_HHYX:
                return "hhyx"
            elif self == stock.STOCK.STOCK_HI:
                return "hi"
            elif self == stock.STOCK.STOCK_HIBB:
                return "hibb"
            elif self == stock.STOCK.STOCK_HIE:
                return "hie"
            elif self == stock.STOCK.STOCK_HIFR:
                return "hifr"
            elif self == stock.STOCK.STOCK_HIFS:
                return "hifs"
            elif self == stock.STOCK.STOCK_HIG-WS:
                return "hig-ws"
            elif self == stock.STOCK.STOCK_HIG:
                return "hig"
            elif self == stock.STOCK.STOCK_HIHO:
                return "hiho"
            elif self == stock.STOCK.STOCK_HII:
                return "hii"
            elif self == stock.STOCK.STOCK_HIIQ:
                return "hiiq"
            elif self == stock.STOCK.STOCK_HIL:
                return "hil"
            elif self == stock.STOCK.STOCK_HIMX:
                return "himx"
            elif self == stock.STOCK.STOCK_HIO:
                return "hio"
            elif self == stock.STOCK.STOCK_HIPS:
                return "hips"
            elif self == stock.STOCK.STOCK_HIVE:
                return "hive"
            elif self == stock.STOCK.STOCK_HIW:
                return "hiw"
            elif self == stock.STOCK.STOCK_HIX:
                return "hix"
            elif self == stock.STOCK.STOCK_HJPX:
                return "hjpx"
            elif self == stock.STOCK.STOCK_HJV:
                return "hjv"
            elif self == stock.STOCK.STOCK_HK-WS:
                return "hk-ws"
            elif self == stock.STOCK.STOCK_HK:
                return "hk"
            elif self == stock.STOCK.STOCK_HL:
                return "hl"
            elif self == stock.STOCK.STOCK_HLF:
                return "hlf"
            elif self == stock.STOCK.STOCK_HLG:
                return "hlg"
            elif self == stock.STOCK.STOCK_HLI:
                return "hli"
            elif self == stock.STOCK.STOCK_HLIT:
                return "hlit"
            elif self == stock.STOCK.STOCK_HLM_:
                return "hlm_"
            elif self == stock.STOCK.STOCK_HLNE:
                return "hlne"
            elif self == stock.STOCK.STOCK_HLS:
                return "hls"
            elif self == stock.STOCK.STOCK_HLT:
                return "hlt"
            elif self == stock.STOCK.STOCK_HLTH:
                return "hlth"
            elif self == stock.STOCK.STOCK_HLX:
                return "hlx"
            elif self == stock.STOCK.STOCK_HL_B:
                return "hl_b"
            elif self == stock.STOCK.STOCK_HMC:
                return "hmc"
            elif self == stock.STOCK.STOCK_HMG:
                return "hmg"
            elif self == stock.STOCK.STOCK_HMHC:
                return "hmhc"
            elif self == stock.STOCK.STOCK_HMLP:
                return "hmlp"
            elif self == stock.STOCK.STOCK_HMLP_A:
                return "hmlp_a"
            elif self == stock.STOCK.STOCK_HMN:
                return "hmn"
            elif self == stock.STOCK.STOCK_HMNF:
                return "hmnf"
            elif self == stock.STOCK.STOCK_HMNY:
                return "hmny"
            elif self == stock.STOCK.STOCK_HMST:
                return "hmst"
            elif self == stock.STOCK.STOCK_HMSY:
                return "hmsy"
            elif self == stock.STOCK.STOCK_HMTA:
                return "hmta"
            elif self == stock.STOCK.STOCK_HMTV:
                return "hmtv"
            elif self == stock.STOCK.STOCK_HMY:
                return "hmy"
            elif self == stock.STOCK.STOCK_HNI:
                return "hni"
            elif self == stock.STOCK.STOCK_HNNA:
                return "hnna"
            elif self == stock.STOCK.STOCK_HNP:
                return "hnp"
            elif self == stock.STOCK.STOCK_HNRG:
                return "hnrg"
            elif self == stock.STOCK.STOCK_HNW:
                return "hnw"
            elif self == stock.STOCK.STOCK_HOFT:
                return "hoft"
            elif self == stock.STOCK.STOCK_HOG:
                return "hog"
            elif self == stock.STOCK.STOCK_HOLI:
                return "holi"
            elif self == stock.STOCK.STOCK_HOLX:
                return "holx"
            elif self == stock.STOCK.STOCK_HOMB:
                return "homb"
            elif self == stock.STOCK.STOCK_HOME:
                return "home"
            elif self == stock.STOCK.STOCK_HOML:
                return "homl"
            elif self == stock.STOCK.STOCK_HON:
                return "hon"
            elif self == stock.STOCK.STOCK_HONE:
                return "hone"
            elif self == stock.STOCK.STOCK_HOPE:
                return "hope"
            elif self == stock.STOCK.STOCK_HOS:
                return "hos"
            elif self == stock.STOCK.STOCK_HOTR:
                return "hotr"
            elif self == stock.STOCK.STOCK_HOV:
                return "hov"
            elif self == stock.STOCK.STOCK_HOVNP:
                return "hovnp"
            elif self == stock.STOCK.STOCK_HP:
                return "hp"
            elif self == stock.STOCK.STOCK_HPE:
                return "hpe"
            elif self == stock.STOCK.STOCK_HPF:
                return "hpf"
            elif self == stock.STOCK.STOCK_HPI:
                return "hpi"
            elif self == stock.STOCK.STOCK_HPJ:
                return "hpj"
            elif self == stock.STOCK.STOCK_HPP:
                return "hpp"
            elif self == stock.STOCK.STOCK_HPQ:
                return "hpq"
            elif self == stock.STOCK.STOCK_HPS:
                return "hps"
            elif self == stock.STOCK.STOCK_HPT:
                return "hpt"
            elif self == stock.STOCK.STOCK_HQCL:
                return "hqcl"
            elif self == stock.STOCK.STOCK_HQH:
                return "hqh"
            elif self == stock.STOCK.STOCK_HQL:
                return "hql"
            elif self == stock.STOCK.STOCK_HQY:
                return "hqy"
            elif self == stock.STOCK.STOCK_HR:
                return "hr"
            elif self == stock.STOCK.STOCK_HRB:
                return "hrb"
            elif self == stock.STOCK.STOCK_HRC:
                return "hrc"
            elif self == stock.STOCK.STOCK_HRG:
                return "hrg"
            elif self == stock.STOCK.STOCK_HRI:
                return "hri"
            elif self == stock.STOCK.STOCK_HRL:
                return "hrl"
            elif self == stock.STOCK.STOCK_HRS:
                return "hrs"
            elif self == stock.STOCK.STOCK_HRTG:
                return "hrtg"
            elif self == stock.STOCK.STOCK_HRTX:
                return "hrtx"
            elif self == stock.STOCK.STOCK_HRZN:
                return "hrzn"
            elif self == stock.STOCK.STOCK_HSBC:
                return "hsbc"
            elif self == stock.STOCK.STOCK_HSBC_A:
                return "hsbc_a"
            elif self == stock.STOCK.STOCK_HSC:
                return "hsc"
            elif self == stock.STOCK.STOCK_HSCZ:
                return "hscz"
            elif self == stock.STOCK.STOCK_HSEA:
                return "hsea"
            elif self == stock.STOCK.STOCK_HSEB:
                return "hseb"
            elif self == stock.STOCK.STOCK_HSGX:
                return "hsgx"
            elif self == stock.STOCK.STOCK_HSIC:
                return "hsic"
            elif self == stock.STOCK.STOCK_HSII:
                return "hsii"
            elif self == stock.STOCK.STOCK_HSKA:
                return "hska"
            elif self == stock.STOCK.STOCK_HSNI:
                return "hsni"
            elif self == stock.STOCK.STOCK_HSON:
                return "hson"
            elif self == stock.STOCK.STOCK_HST:
                return "hst"
            elif self == stock.STOCK.STOCK_HSTM:
                return "hstm"
            elif self == stock.STOCK.STOCK_HSY:
                return "hsy"
            elif self == stock.STOCK.STOCK_HT:
                return "ht"
            elif self == stock.STOCK.STOCK_HTA:
                return "hta"
            elif self == stock.STOCK.STOCK_HTBI:
                return "htbi"
            elif self == stock.STOCK.STOCK_HTBK:
                return "htbk"
            elif self == stock.STOCK.STOCK_HTBX:
                return "htbx"
            elif self == stock.STOCK.STOCK_HTD:
                return "htd"
            elif self == stock.STOCK.STOCK_HTF-CL:
                return "htf-cl"
            elif self == stock.STOCK.STOCK_HTFA:
                return "htfa"
            elif self == stock.STOCK.STOCK_HTGC:
                return "htgc"
            elif self == stock.STOCK.STOCK_HTGM:
                return "htgm"
            elif self == stock.STOCK.STOCK_HTGX:
                return "htgx"
            elif self == stock.STOCK.STOCK_HTH:
                return "hth"
            elif self == stock.STOCK.STOCK_HTHT:
                return "htht"
            elif self == stock.STOCK.STOCK_HTLD:
                return "htld"
            elif self == stock.STOCK.STOCK_HTLF:
                return "htlf"
            elif self == stock.STOCK.STOCK_HTM:
                return "htm"
            elif self == stock.STOCK.STOCK_HTRB:
                return "htrb"
            elif self == stock.STOCK.STOCK_HTUS:
                return "htus"
            elif self == stock.STOCK.STOCK_HTY:
                return "hty"
            elif self == stock.STOCK.STOCK_HTZ:
                return "htz"
            elif self == stock.STOCK.STOCK_HT_C:
                return "ht_c"
            elif self == stock.STOCK.STOCK_HT_D:
                return "ht_d"
            elif self == stock.STOCK.STOCK_HT_E:
                return "ht_e"
            elif self == stock.STOCK.STOCK_HUBB:
                return "hubb"
            elif self == stock.STOCK.STOCK_HUBG:
                return "hubg"
            elif self == stock.STOCK.STOCK_HUBS:
                return "hubs"
            elif self == stock.STOCK.STOCK_HUM:
                return "hum"
            elif self == stock.STOCK.STOCK_HUN:
                return "hun"
            elif self == stock.STOCK.STOCK_HUNT:
                return "hunt"
            elif self == stock.STOCK.STOCK_HUNTU:
                return "huntu"
            elif self == stock.STOCK.STOCK_HUNTW:
                return "huntw"
            elif self == stock.STOCK.STOCK_HURC:
                return "hurc"
            elif self == stock.STOCK.STOCK_HURN:
                return "hurn"
            elif self == stock.STOCK.STOCK_HUSA:
                return "husa"
            elif self == stock.STOCK.STOCK_HUSV:
                return "husv"
            elif self == stock.STOCK.STOCK_HVBC:
                return "hvbc"
            elif self == stock.STOCK.STOCK_HVT-A:
                return "hvt-a"
            elif self == stock.STOCK.STOCK_HVT:
                return "hvt"
            elif self == stock.STOCK.STOCK_HWBK:
                return "hwbk"
            elif self == stock.STOCK.STOCK_HWCC:
                return "hwcc"
            elif self == stock.STOCK.STOCK_HWKN:
                return "hwkn"
            elif self == stock.STOCK.STOCK_HX:
                return "hx"
            elif self == stock.STOCK.STOCK_HXL:
                return "hxl"
            elif self == stock.STOCK.STOCK_HY:
                return "hy"
            elif self == stock.STOCK.STOCK_HYACU:
                return "hyacu"
            elif self == stock.STOCK.STOCK_HYB:
                return "hyb"
            elif self == stock.STOCK.STOCK_HYDB:
                return "hydb"
            elif self == stock.STOCK.STOCK_HYDD:
                return "hydd"
            elif self == stock.STOCK.STOCK_HYGS:
                return "hygs"
            elif self == stock.STOCK.STOCK_HYH:
                return "hyh"
            elif self == stock.STOCK.STOCK_HYHG:
                return "hyhg"
            elif self == stock.STOCK.STOCK_HYI:
                return "hyi"
            elif self == stock.STOCK.STOCK_HYLB:
                return "hylb"
            elif self == stock.STOCK.STOCK_HYLV:
                return "hylv"
            elif self == stock.STOCK.STOCK_HYT:
                return "hyt"
            elif self == stock.STOCK.STOCK_HYXE:
                return "hyxe"
            elif self == stock.STOCK.STOCK_HYXU:
                return "hyxu"
            elif self == stock.STOCK.STOCK_HZN:
                return "hzn"
            elif self == stock.STOCK.STOCK_HZNP:
                return "hznp"
            elif self == stock.STOCK.STOCK_HZO:
                return "hzo"
            elif self == stock.STOCK.STOCK_I:
                return "i"
            elif self == stock.STOCK.STOCK_IAC:
                return "iac"
            elif self == stock.STOCK.STOCK_IAE:
                return "iae"
            elif self == stock.STOCK.STOCK_IAF:
                return "iaf"
            elif self == stock.STOCK.STOCK_IAG:
                return "iag"
            elif self == stock.STOCK.STOCK_IAGG:
                return "iagg"
            elif self == stock.STOCK.STOCK_IAM:
                return "iam"
            elif self == stock.STOCK.STOCK_IAMXR:
                return "iamxr"
            elif self == stock.STOCK.STOCK_IAMXW:
                return "iamxw"
            elif self == stock.STOCK.STOCK_IART:
                return "iart"
            elif self == stock.STOCK.STOCK_IBA:
                return "iba"
            elif self == stock.STOCK.STOCK_IBCP:
                return "ibcp"
            elif self == stock.STOCK.STOCK_IBD:
                return "ibd"
            elif self == stock.STOCK.STOCK_IBDR:
                return "ibdr"
            elif self == stock.STOCK.STOCK_IBDS:
                return "ibds"
            elif self == stock.STOCK.STOCK_IBIO:
                return "ibio"
            elif self == stock.STOCK.STOCK_IBKC:
                return "ibkc"
            elif self == stock.STOCK.STOCK_IBKCO:
                return "ibkco"
            elif self == stock.STOCK.STOCK_IBKCP:
                return "ibkcp"
            elif self == stock.STOCK.STOCK_IBKR:
                return "ibkr"
            elif self == stock.STOCK.STOCK_IBM:
                return "ibm"
            elif self == stock.STOCK.STOCK_IBMJ:
                return "ibmj"
            elif self == stock.STOCK.STOCK_IBMK:
                return "ibmk"
            elif self == stock.STOCK.STOCK_IBML:
                return "ibml"
            elif self == stock.STOCK.STOCK_IBN:
                return "ibn"
            elif self == stock.STOCK.STOCK_IBO:
                return "ibo"
            elif self == stock.STOCK.STOCK_IBOC:
                return "iboc"
            elif self == stock.STOCK.STOCK_IBP:
                return "ibp"
            elif self == stock.STOCK.STOCK_IBTX:
                return "ibtx"
            elif self == stock.STOCK.STOCK_IBUY:
                return "ibuy"
            elif self == stock.STOCK.STOCK_ICAD:
                return "icad"
            elif self == stock.STOCK.STOCK_ICAN:
                return "ican"
            elif self == stock.STOCK.STOCK_ICB:
                return "icb"
            elif self == stock.STOCK.STOCK_ICBK:
                return "icbk"
            elif self == stock.STOCK.STOCK_ICCC:
                return "iccc"
            elif self == stock.STOCK.STOCK_ICCH:
                return "icch"
            elif self == stock.STOCK.STOCK_ICD:
                return "icd"
            elif self == stock.STOCK.STOCK_ICE:
                return "ice"
            elif self == stock.STOCK.STOCK_ICFI:
                return "icfi"
            elif self == stock.STOCK.STOCK_ICHR:
                return "ichr"
            elif self == stock.STOCK.STOCK_ICL:
                return "icl"
            elif self == stock.STOCK.STOCK_ICLR:
                return "iclr"
            elif self == stock.STOCK.STOCK_ICON:
                return "icon"
            elif self == stock.STOCK.STOCK_ICOW:
                return "icow"
            elif self == stock.STOCK.STOCK_ICPT:
                return "icpt"
            elif self == stock.STOCK.STOCK_ICSH:
                return "icsh"
            elif self == stock.STOCK.STOCK_ICUI:
                return "icui"
            elif self == stock.STOCK.STOCK_ICVT:
                return "icvt"
            elif self == stock.STOCK.STOCK_IDA:
                return "ida"
            elif self == stock.STOCK.STOCK_IDCC:
                return "idcc"
            elif self == stock.STOCK.STOCK_IDE:
                return "ide"
            elif self == stock.STOCK.STOCK_IDEV:
                return "idev"
            elif self == stock.STOCK.STOCK_IDHD:
                return "idhd"
            elif self == stock.STOCK.STOCK_IDLB:
                return "idlb"
            elif self == stock.STOCK.STOCK_IDMO:
                return "idmo"
            elif self == stock.STOCK.STOCK_IDN:
                return "idn"
            elif self == stock.STOCK.STOCK_IDRA:
                return "idra"
            elif self == stock.STOCK.STOCK_IDSA:
                return "idsa"
            elif self == stock.STOCK.STOCK_IDSY:
                return "idsy"
            elif self == stock.STOCK.STOCK_IDT:
                return "idt"
            elif self == stock.STOCK.STOCK_IDTI:
                return "idti"
            elif self == stock.STOCK.STOCK_IDXG:
                return "idxg"
            elif self == stock.STOCK.STOCK_IDXX:
                return "idxx"
            elif self == stock.STOCK.STOCK_IEC:
                return "iec"
            elif self == stock.STOCK.STOCK_IEP:
                return "iep"
            elif self == stock.STOCK.STOCK_IESC:
                return "iesc"
            elif self == stock.STOCK.STOCK_IEX:
                return "iex"
            elif self == stock.STOCK.STOCK_IF:
                return "if"
            elif self == stock.STOCK.STOCK_IFF:
                return "iff"
            elif self == stock.STOCK.STOCK_IFIX:
                return "ifix"
            elif self == stock.STOCK.STOCK_IFLY:
                return "ifly"
            elif self == stock.STOCK.STOCK_IFMK:
                return "ifmk"
            elif self == stock.STOCK.STOCK_IFN:
                return "ifn"
            elif self == stock.STOCK.STOCK_IFON:
                return "ifon"
            elif self == stock.STOCK.STOCK_IFRX:
                return "ifrx"
            elif self == stock.STOCK.STOCK_IGA:
                return "iga"
            elif self == stock.STOCK.STOCK_IGC:
                return "igc"
            elif self == stock.STOCK.STOCK_IGD:
                return "igd"
            elif self == stock.STOCK.STOCK_IGEB:
                return "igeb"
            elif self == stock.STOCK.STOCK_IGEM:
                return "igem"
            elif self == stock.STOCK.STOCK_IGHG:
                return "ighg"
            elif self == stock.STOCK.STOCK_IGI:
                return "igi"
            elif self == stock.STOCK.STOCK_IGLD:
                return "igld"
            elif self == stock.STOCK.STOCK_IGR:
                return "igr"
            elif self == stock.STOCK.STOCK_IGRO:
                return "igro"
            elif self == stock.STOCK.STOCK_IGT:
                return "igt"
            elif self == stock.STOCK.STOCK_IGVT:
                return "igvt"
            elif self == stock.STOCK.STOCK_IGZ:
                return "igz"
            elif self == stock.STOCK.STOCK_IHC:
                return "ihc"
            elif self == stock.STOCK.STOCK_IHD:
                return "ihd"
            elif self == stock.STOCK.STOCK_IHG:
                return "ihg"
            elif self == stock.STOCK.STOCK_IHIT:
                return "ihit"
            elif self == stock.STOCK.STOCK_IHT:
                return "iht"
            elif self == stock.STOCK.STOCK_IID:
                return "iid"
            elif self == stock.STOCK.STOCK_IIF:
                return "iif"
            elif self == stock.STOCK.STOCK_III:
                return "iii"
            elif self == stock.STOCK.STOCK_IIIN:
                return "iiin"
            elif self == stock.STOCK.STOCK_IIJI:
                return "iiji"
            elif self == stock.STOCK.STOCK_IIM:
                return "iim"
            elif self == stock.STOCK.STOCK_IIN:
                return "iin"
            elif self == stock.STOCK.STOCK_IIPR:
                return "iipr"
            elif self == stock.STOCK.STOCK_IIPR_A:
                return "iipr_a"
            elif self == stock.STOCK.STOCK_IIVI:
                return "iivi"
            elif self == stock.STOCK.STOCK_IKNX:
                return "iknx"
            elif self == stock.STOCK.STOCK_ILG:
                return "ilg"
            elif self == stock.STOCK.STOCK_ILMN:
                return "ilmn"
            elif self == stock.STOCK.STOCK_IMAX:
                return "imax"
            elif self == stock.STOCK.STOCK_IMDZ:
                return "imdz"
            elif self == stock.STOCK.STOCK_IMGN:
                return "imgn"
            elif self == stock.STOCK.STOCK_IMH:
                return "imh"
            elif self == stock.STOCK.STOCK_IMI:
                return "imi"
            elif self == stock.STOCK.STOCK_IMKTA:
                return "imkta"
            elif self == stock.STOCK.STOCK_IMMR:
                return "immr"
            elif self == stock.STOCK.STOCK_IMMU:
                return "immu"
            elif self == stock.STOCK.STOCK_IMMY:
                return "immy"
            elif self == stock.STOCK.STOCK_IMNP:
                return "imnp"
            elif self == stock.STOCK.STOCK_IMO:
                return "imo"
            elif self == stock.STOCK.STOCK_IMOM:
                return "imom"
            elif self == stock.STOCK.STOCK_IMOS:
                return "imos"
            elif self == stock.STOCK.STOCK_IMPV:
                return "impv"
            elif self == stock.STOCK.STOCK_IMRN:
                return "imrn"
            elif self == stock.STOCK.STOCK_IMRNW:
                return "imrnw"
            elif self == stock.STOCK.STOCK_IMTB:
                return "imtb"
            elif self == stock.STOCK.STOCK_IMTE:
                return "imte"
            elif self == stock.STOCK.STOCK_IMUC-WS:
                return "imuc-ws"
            elif self == stock.STOCK.STOCK_IMUC:
                return "imuc"
            elif self == stock.STOCK.STOCK_INAP:
                return "inap"
            elif self == stock.STOCK.STOCK_INB:
                return "inb"
            elif self == stock.STOCK.STOCK_INBK:
                return "inbk"
            elif self == stock.STOCK.STOCK_INBKL:
                return "inbkl"
            elif self == stock.STOCK.STOCK_INCR:
                return "incr"
            elif self == stock.STOCK.STOCK_INCY:
                return "incy"
            elif self == stock.STOCK.STOCK_INDB:
                return "indb"
            elif self == stock.STOCK.STOCK_INDF:
                return "indf"
            elif self == stock.STOCK.STOCK_INDU:
                return "indu"
            elif self == stock.STOCK.STOCK_INDUU:
                return "induu"
            elif self == stock.STOCK.STOCK_INDUW:
                return "induw"
            elif self == stock.STOCK.STOCK_INF:
                return "inf"
            elif self == stock.STOCK.STOCK_INFI:
                return "infi"
            elif self == stock.STOCK.STOCK_INFN:
                return "infn"
            elif self == stock.STOCK.STOCK_INFO:
                return "info"
            elif self == stock.STOCK.STOCK_INFR:
                return "infr"
            elif self == stock.STOCK.STOCK_INFU:
                return "infu"
            elif self == stock.STOCK.STOCK_INFY:
                return "infy"
            elif self == stock.STOCK.STOCK_ING:
                return "ing"
            elif self == stock.STOCK.STOCK_INGN:
                return "ingn"
            elif self == stock.STOCK.STOCK_INGR:
                return "ingr"
            elif self == stock.STOCK.STOCK_INN:
                return "inn"
            elif self == stock.STOCK.STOCK_INN_B-CL:
                return "inn_b-cl"
            elif self == stock.STOCK.STOCK_INN_B:
                return "inn_b"
            elif self == stock.STOCK.STOCK_INN_C:
                return "inn_c"
            elif self == stock.STOCK.STOCK_INN_D:
                return "inn_d"
            elif self == stock.STOCK.STOCK_INO:
                return "ino"
            elif self == stock.STOCK.STOCK_INOD:
                return "inod"
            elif self == stock.STOCK.STOCK_INOV:
                return "inov"
            elif self == stock.STOCK.STOCK_INPX:
                return "inpx"
            elif self == stock.STOCK.STOCK_INS:
                return "ins"
            elif self == stock.STOCK.STOCK_INSE:
                return "inse"
            elif self == stock.STOCK.STOCK_INSG:
                return "insg"
            elif self == stock.STOCK.STOCK_INSI:
                return "insi"
            elif self == stock.STOCK.STOCK_INSM:
                return "insm"
            elif self == stock.STOCK.STOCK_INST:
                return "inst"
            elif self == stock.STOCK.STOCK_INSW:
                return "insw"
            elif self == stock.STOCK.STOCK_INSY:
                return "insy"
            elif self == stock.STOCK.STOCK_INT:
                return "int"
            elif self == stock.STOCK.STOCK_INTC:
                return "intc"
            elif self == stock.STOCK.STOCK_INTG:
                return "intg"
            elif self == stock.STOCK.STOCK_INTL:
                return "intl"
            elif self == stock.STOCK.STOCK_INTT:
                return "intt"
            elif self == stock.STOCK.STOCK_INTU:
                return "intu"
            elif self == stock.STOCK.STOCK_INTX:
                return "intx"
            elif self == stock.STOCK.STOCK_INUV:
                return "inuv"
            elif self == stock.STOCK.STOCK_INVA:
                return "inva"
            elif self == stock.STOCK.STOCK_INVE:
                return "inve"
            elif self == stock.STOCK.STOCK_INVH:
                return "invh"
            elif self == stock.STOCK.STOCK_INWK:
                return "inwk"
            elif self == stock.STOCK.STOCK_INXN:
                return "inxn"
            elif self == stock.STOCK.STOCK_IO:
                return "io"
            elif self == stock.STOCK.STOCK_IONS:
                return "ions"
            elif self == stock.STOCK.STOCK_IOR:
                return "ior"
            elif self == stock.STOCK.STOCK_IOSP:
                return "iosp"
            elif self == stock.STOCK.STOCK_IOTS:
                return "iots"
            elif self == stock.STOCK.STOCK_IOVA:
                return "iova"
            elif self == stock.STOCK.STOCK_IP:
                return "ip"
            elif self == stock.STOCK.STOCK_IPAR:
                return "ipar"
            elif self == stock.STOCK.STOCK_IPAS:
                return "ipas"
            elif self == stock.STOCK.STOCK_IPAY:
                return "ipay"
            elif self == stock.STOCK.STOCK_IPB:
                return "ipb"
            elif self == stock.STOCK.STOCK_IPCC:
                return "ipcc"
            elif self == stock.STOCK.STOCK_IPCI:
                return "ipci"
            elif self == stock.STOCK.STOCK_IPDN:
                return "ipdn"
            elif self == stock.STOCK.STOCK_IPG:
                return "ipg"
            elif self == stock.STOCK.STOCK_IPGP:
                return "ipgp"
            elif self == stock.STOCK.STOCK_IPHI:
                return "iphi"
            elif self == stock.STOCK.STOCK_IPHS:
                return "iphs"
            elif self == stock.STOCK.STOCK_IPI:
                return "ipi"
            elif self == stock.STOCK.STOCK_IPL_D:
                return "ipl_d"
            elif self == stock.STOCK.STOCK_IPOA-U:
                return "ipoa-u"
            elif self == stock.STOCK.STOCK_IPOA-WS:
                return "ipoa-ws"
            elif self == stock.STOCK.STOCK_IPOA:
                return "ipoa"
            elif self == stock.STOCK.STOCK_IPOS:
                return "ipos"
            elif self == stock.STOCK.STOCK_IPWR:
                return "ipwr"
            elif self == stock.STOCK.STOCK_IPXL:
                return "ipxl"
            elif self == stock.STOCK.STOCK_IQDG:
                return "iqdg"
            elif self == stock.STOCK.STOCK_IQI:
                return "iqi"
            elif self == stock.STOCK.STOCK_IR:
                return "ir"
            elif self == stock.STOCK.STOCK_IRBT:
                return "irbt"
            elif self == stock.STOCK.STOCK_IRCP:
                return "ircp"
            elif self == stock.STOCK.STOCK_IRDM:
                return "irdm"
            elif self == stock.STOCK.STOCK_IRDMB:
                return "irdmb"
            elif self == stock.STOCK.STOCK_IRET:
                return "iret"
            elif self == stock.STOCK.STOCK_IRET_B-CL:
                return "iret_b-cl"
            elif self == stock.STOCK.STOCK_IRET_C:
                return "iret_c"
            elif self == stock.STOCK.STOCK_IRIX:
                return "irix"
            elif self == stock.STOCK.STOCK_IRL:
                return "irl"
            elif self == stock.STOCK.STOCK_IRLR:
                return "irlr"
            elif self == stock.STOCK.STOCK_IRM:
                return "irm"
            elif self == stock.STOCK.STOCK_IRMD:
                return "irmd"
            elif self == stock.STOCK.STOCK_IROQ:
                return "iroq"
            elif self == stock.STOCK.STOCK_IRR:
                return "irr"
            elif self == stock.STOCK.STOCK_IRS:
                return "irs"
            elif self == stock.STOCK.STOCK_IRT:
                return "irt"
            elif self == stock.STOCK.STOCK_IRTC:
                return "irtc"
            elif self == stock.STOCK.STOCK_IRWD:
                return "irwd"
            elif self == stock.STOCK.STOCK_ISBC:
                return "isbc"
            elif self == stock.STOCK.STOCK_ISCA:
                return "isca"
            elif self == stock.STOCK.STOCK_ISD:
                return "isd"
            elif self == stock.STOCK.STOCK_ISDR:
                return "isdr"
            elif self == stock.STOCK.STOCK_ISF:
                return "isf"
            elif self == stock.STOCK.STOCK_ISG:
                return "isg"
            elif self == stock.STOCK.STOCK_ISIG:
                return "isig"
            elif self == stock.STOCK.STOCK_ISL:
                return "isl"
            elif self == stock.STOCK.STOCK_ISM:
                return "ism"
            elif self == stock.STOCK.STOCK_ISMD:
                return "ismd"
            elif self == stock.STOCK.STOCK_ISNS:
                return "isns"
            elif self == stock.STOCK.STOCK_ISP-CL:
                return "isp-cl"
            elif self == stock.STOCK.STOCK_ISR:
                return "isr"
            elif self == stock.STOCK.STOCK_ISRG:
                return "isrg"
            elif self == stock.STOCK.STOCK_ISRL:
                return "isrl"
            elif self == stock.STOCK.STOCK_ISSC:
                return "issc"
            elif self == stock.STOCK.STOCK_ISTR:
                return "istr"
            elif self == stock.STOCK.STOCK_ISZE:
                return "isze"
            elif self == stock.STOCK.STOCK_IT:
                return "it"
            elif self == stock.STOCK.STOCK_ITCB:
                return "itcb"
            elif self == stock.STOCK.STOCK_ITCI:
                return "itci"
            elif self == stock.STOCK.STOCK_ITEK:
                return "itek"
            elif self == stock.STOCK.STOCK_ITEQ:
                return "iteq"
            elif self == stock.STOCK.STOCK_ITG:
                return "itg"
            elif self == stock.STOCK.STOCK_ITGR:
                return "itgr"
            elif self == stock.STOCK.STOCK_ITI:
                return "iti"
            elif self == stock.STOCK.STOCK_ITIC:
                return "itic"
            elif self == stock.STOCK.STOCK_ITRI:
                return "itri"
            elif self == stock.STOCK.STOCK_ITRN:
                return "itrn"
            elif self == stock.STOCK.STOCK_ITT:
                return "itt"
            elif self == stock.STOCK.STOCK_ITUB:
                return "itub"
            elif self == stock.STOCK.STOCK_ITUS:
                return "itus"
            elif self == stock.STOCK.STOCK_ITW:
                return "itw"
            elif self == stock.STOCK.STOCK_IVAC:
                return "ivac"
            elif self == stock.STOCK.STOCK_IVAL:
                return "ival"
            elif self == stock.STOCK.STOCK_IVC:
                return "ivc"
            elif self == stock.STOCK.STOCK_IVENC:
                return "ivenc"
            elif self == stock.STOCK.STOCK_IVFGC:
                return "ivfgc"
            elif self == stock.STOCK.STOCK_IVFVC:
                return "ivfvc"
            elif self == stock.STOCK.STOCK_IVH:
                return "ivh"
            elif self == stock.STOCK.STOCK_IVLU:
                return "ivlu"
            elif self == stock.STOCK.STOCK_IVR:
                return "ivr"
            elif self == stock.STOCK.STOCK_IVR_A:
                return "ivr_a"
            elif self == stock.STOCK.STOCK_IVR_B:
                return "ivr_b"
            elif self == stock.STOCK.STOCK_IVR_C:
                return "ivr_c"
            elif self == stock.STOCK.STOCK_IVTY:
                return "ivty"
            elif self == stock.STOCK.STOCK_IVZ:
                return "ivz"
            elif self == stock.STOCK.STOCK_IX:
                return "ix"
            elif self == stock.STOCK.STOCK_IXYS:
                return "ixys"
            elif self == stock.STOCK.STOCK_IYLD:
                return "iyld"
            elif self == stock.STOCK.STOCK_IZEA:
                return "izea"
            elif self == stock.STOCK.STOCK_JACK:
                return "jack"
            elif self == stock.STOCK.STOCK_JAG:
                return "jag"
            elif self == stock.STOCK.STOCK_JAGX:
                return "jagx"
            elif self == stock.STOCK.STOCK_JAKK:
                return "jakk"
            elif self == stock.STOCK.STOCK_JASN:
                return "jasn"
            elif self == stock.STOCK.STOCK_JASNW:
                return "jasnw"
            elif self == stock.STOCK.STOCK_JASO:
                return "jaso"
            elif self == stock.STOCK.STOCK_JAX:
                return "jax"
            elif self == stock.STOCK.STOCK_JAZZ:
                return "jazz"
            elif self == stock.STOCK.STOCK_JBGS:
                return "jbgs"
            elif self == stock.STOCK.STOCK_JBHT:
                return "jbht"
            elif self == stock.STOCK.STOCK_JBK:
                return "jbk"
            elif self == stock.STOCK.STOCK_JBL:
                return "jbl"
            elif self == stock.STOCK.STOCK_JBLU:
                return "jblu"
            elif self == stock.STOCK.STOCK_JBN:
                return "jbn"
            elif self == stock.STOCK.STOCK_JBR:
                return "jbr"
            elif self == stock.STOCK.STOCK_JBSS:
                return "jbss"
            elif self == stock.STOCK.STOCK_JBT:
                return "jbt"
            elif self == stock.STOCK.STOCK_JCAP:
                return "jcap"
            elif self == stock.STOCK.STOCK_JCE:
                return "jce"
            elif self == stock.STOCK.STOCK_JCI:
                return "jci"
            elif self == stock.STOCK.STOCK_JCO:
                return "jco"
            elif self == stock.STOCK.STOCK_JCOM:
                return "jcom"
            elif self == stock.STOCK.STOCK_JCP:
                return "jcp"
            elif self == stock.STOCK.STOCK_JCS:
                return "jcs"
            elif self == stock.STOCK.STOCK_JCTCF:
                return "jctcf"
            elif self == stock.STOCK.STOCK_JD:
                return "jd"
            elif self == stock.STOCK.STOCK_JDD:
                return "jdd"
            elif self == stock.STOCK.STOCK_JDIV:
                return "jdiv"
            elif self == stock.STOCK.STOCK_JE:
                return "je"
            elif self == stock.STOCK.STOCK_JEC:
                return "jec"
            elif self == stock.STOCK.STOCK_JELD:
                return "jeld"
            elif self == stock.STOCK.STOCK_JEMD:
                return "jemd"
            elif self == stock.STOCK.STOCK_JEQ:
                return "jeq"
            elif self == stock.STOCK.STOCK_JETS:
                return "jets"
            elif self == stock.STOCK.STOCK_JE_A:
                return "je_a"
            elif self == stock.STOCK.STOCK_JFR:
                return "jfr"
            elif self == stock.STOCK.STOCK_JGH:
                return "jgh"
            elif self == stock.STOCK.STOCK_JHA:
                return "jha"
            elif self == stock.STOCK.STOCK_JHB:
                return "jhb"
            elif self == stock.STOCK.STOCK_JHD:
                return "jhd"
            elif self == stock.STOCK.STOCK_JHG:
                return "jhg"
            elif self == stock.STOCK.STOCK_JHI:
                return "jhi"
            elif self == stock.STOCK.STOCK_JHMA:
                return "jhma"
            elif self == stock.STOCK.STOCK_JHMC:
                return "jhmc"
            elif self == stock.STOCK.STOCK_JHMD:
                return "jhmd"
            elif self == stock.STOCK.STOCK_JHME:
                return "jhme"
            elif self == stock.STOCK.STOCK_JHMF:
                return "jhmf"
            elif self == stock.STOCK.STOCK_JHMH:
                return "jhmh"
            elif self == stock.STOCK.STOCK_JHMI:
                return "jhmi"
            elif self == stock.STOCK.STOCK_JHML:
                return "jhml"
            elif self == stock.STOCK.STOCK_JHMM:
                return "jhmm"
            elif self == stock.STOCK.STOCK_JHMS:
                return "jhms"
            elif self == stock.STOCK.STOCK_JHMT:
                return "jhmt"
            elif self == stock.STOCK.STOCK_JHMU:
                return "jhmu"
            elif self == stock.STOCK.STOCK_JHS:
                return "jhs"
            elif self == stock.STOCK.STOCK_JHSC:
                return "jhsc"
            elif self == stock.STOCK.STOCK_JHX:
                return "jhx"
            elif self == stock.STOCK.STOCK_JHY:
                return "jhy"
            elif self == stock.STOCK.STOCK_JILL:
                return "jill"
            elif self == stock.STOCK.STOCK_JJSF:
                return "jjsf"
            elif self == stock.STOCK.STOCK_JKHY:
                return "jkhy"
            elif self == stock.STOCK.STOCK_JKS:
                return "jks"
            elif self == stock.STOCK.STOCK_JLL:
                return "jll"
            elif self == stock.STOCK.STOCK_JLS:
                return "jls"
            elif self == stock.STOCK.STOCK_JMBA:
                return "jmba"
            elif self == stock.STOCK.STOCK_JMEI:
                return "jmei"
            elif self == stock.STOCK.STOCK_JMF:
                return "jmf"
            elif self == stock.STOCK.STOCK_JMLP:
                return "jmlp"
            elif self == stock.STOCK.STOCK_JMM:
                return "jmm"
            elif self == stock.STOCK.STOCK_JMOM:
                return "jmom"
            elif self == stock.STOCK.STOCK_JMP:
                return "jmp"
            elif self == stock.STOCK.STOCK_JMPB:
                return "jmpb"
            elif self == stock.STOCK.STOCK_JMPC:
                return "jmpc"
            elif self == stock.STOCK.STOCK_JMT:
                return "jmt"
            elif self == stock.STOCK.STOCK_JMU:
                return "jmu"
            elif self == stock.STOCK.STOCK_JNCE:
                return "jnce"
            elif self == stock.STOCK.STOCK_JNJ:
                return "jnj"
            elif self == stock.STOCK.STOCK_JNP:
                return "jnp"
            elif self == stock.STOCK.STOCK_JNPR:
                return "jnpr"
            elif self == stock.STOCK.STOCK_JOB:
                return "job"
            elif self == stock.STOCK.STOCK_JOBS:
                return "jobs"
            elif self == stock.STOCK.STOCK_JOE:
                return "joe"
            elif self == stock.STOCK.STOCK_JOF:
                return "jof"
            elif self == stock.STOCK.STOCK_JONE:
                return "jone"
            elif self == stock.STOCK.STOCK_JOUT:
                return "jout"
            elif self == stock.STOCK.STOCK_JP:
                return "jp"
            elif self == stock.STOCK.STOCK_JPC:
                return "jpc"
            elif self == stock.STOCK.STOCK_JPEH:
                return "jpeh"
            elif self == stock.STOCK.STOCK_JPEM:
                return "jpem"
            elif self == stock.STOCK.STOCK_JPEU:
                return "jpeu"
            elif self == stock.STOCK.STOCK_JPGB:
                return "jpgb"
            elif self == stock.STOCK.STOCK_JPHF:
                return "jphf"
            elif self == stock.STOCK.STOCK_JPHY:
                return "jphy"
            elif self == stock.STOCK.STOCK_JPI:
                return "jpi"
            elif self == stock.STOCK.STOCK_JPIH:
                return "jpih"
            elif self == stock.STOCK.STOCK_JPIN:
                return "jpin"
            elif self == stock.STOCK.STOCK_JPM-WS:
                return "jpm-ws"
            elif self == stock.STOCK.STOCK_JPM:
                return "jpm"
            elif self == stock.STOCK.STOCK_JPME:
                return "jpme"
            elif self == stock.STOCK.STOCK_JPM_A:
                return "jpm_a"
            elif self == stock.STOCK.STOCK_JPM_B:
                return "jpm_b"
            elif self == stock.STOCK.STOCK_JPM_D-CL:
                return "jpm_d-cl"
            elif self == stock.STOCK.STOCK_JPM_D:
                return "jpm_d"
            elif self == stock.STOCK.STOCK_JPM_E:
                return "jpm_e"
            elif self == stock.STOCK.STOCK_JPM_F:
                return "jpm_f"
            elif self == stock.STOCK.STOCK_JPM_G:
                return "jpm_g"
            elif self == stock.STOCK.STOCK_JPM_H:
                return "jpm_h"
            elif self == stock.STOCK.STOCK_JPN:
                return "jpn"
            elif self == stock.STOCK.STOCK_JPS:
                return "jps"
            elif self == stock.STOCK.STOCK_JPSE:
                return "jpse"
            elif self == stock.STOCK.STOCK_JPST:
                return "jpst"
            elif self == stock.STOCK.STOCK_JPT:
                return "jpt"
            elif self == stock.STOCK.STOCK_JPUS:
                return "jpus"
            elif self == stock.STOCK.STOCK_JPXN:
                return "jpxn"
            elif self == stock.STOCK.STOCK_JQC:
                return "jqc"
            elif self == stock.STOCK.STOCK_JRI:
                return "jri"
            elif self == stock.STOCK.STOCK_JRJC:
                return "jrjc"
            elif self == stock.STOCK.STOCK_JRJR:
                return "jrjr"
            elif self == stock.STOCK.STOCK_JRO:
                return "jro"
            elif self == stock.STOCK.STOCK_JRS:
                return "jrs"
            elif self == stock.STOCK.STOCK_JRVR:
                return "jrvr"
            elif self == stock.STOCK.STOCK_JSD:
                return "jsd"
            elif self == stock.STOCK.STOCK_JSM:
                return "jsm"
            elif self == stock.STOCK.STOCK_JSMD:
                return "jsmd"
            elif self == stock.STOCK.STOCK_JSML:
                return "jsml"
            elif self == stock.STOCK.STOCK_JSYN:
                return "jsyn"
            elif self == stock.STOCK.STOCK_JSYNR:
                return "jsynr"
            elif self == stock.STOCK.STOCK_JSYNU:
                return "jsynu"
            elif self == stock.STOCK.STOCK_JSYNW:
                return "jsynw"
            elif self == stock.STOCK.STOCK_JT:
                return "jt"
            elif self == stock.STOCK.STOCK_JTA:
                return "jta"
            elif self == stock.STOCK.STOCK_JTD:
                return "jtd"
            elif self == stock.STOCK.STOCK_JTPY:
                return "jtpy"
            elif self == stock.STOCK.STOCK_JUNO:
                return "juno"
            elif self == stock.STOCK.STOCK_JVA:
                return "jva"
            elif self == stock.STOCK.STOCK_JW-A:
                return "jw-a"
            elif self == stock.STOCK.STOCK_JW-B:
                return "jw-b"
            elif self == stock.STOCK.STOCK_JWN:
                return "jwn"
            elif self == stock.STOCK.STOCK_JXSB:
                return "jxsb"
            elif self == stock.STOCK.STOCK_JYNT:
                return "jynt"
            elif self == stock.STOCK.STOCK_K:
                return "k"
            elif self == stock.STOCK.STOCK_KAAC:
                return "kaac"
            elif self == stock.STOCK.STOCK_KAACU:
                return "kaacu"
            elif self == stock.STOCK.STOCK_KAACW:
                return "kaacw"
            elif self == stock.STOCK.STOCK_KAI:
                return "kai"
            elif self == stock.STOCK.STOCK_KALA:
                return "kala"
            elif self == stock.STOCK.STOCK_KALU:
                return "kalu"
            elif self == stock.STOCK.STOCK_KALV:
                return "kalv"
            elif self == stock.STOCK.STOCK_KAMN:
                return "kamn"
            elif self == stock.STOCK.STOCK_KANG:
                return "kang"
            elif self == stock.STOCK.STOCK_KAP:
                return "kap"
            elif self == stock.STOCK.STOCK_KAR:
                return "kar"
            elif self == stock.STOCK.STOCK_KB:
                return "kb"
            elif self == stock.STOCK.STOCK_KBAL:
                return "kbal"
            elif self == stock.STOCK.STOCK_KBH:
                return "kbh"
            elif self == stock.STOCK.STOCK_KBLM:
                return "kblm"
            elif self == stock.STOCK.STOCK_KBLMR:
                return "kblmr"
            elif self == stock.STOCK.STOCK_KBLMU:
                return "kblmu"
            elif self == stock.STOCK.STOCK_KBLMW:
                return "kblmw"
            elif self == stock.STOCK.STOCK_KBR:
                return "kbr"
            elif self == stock.STOCK.STOCK_KBSF:
                return "kbsf"
            elif self == stock.STOCK.STOCK_KBWB:
                return "kbwb"
            elif self == stock.STOCK.STOCK_KBWD:
                return "kbwd"
            elif self == stock.STOCK.STOCK_KBWY:
                return "kbwy"
            elif self == stock.STOCK.STOCK_KCAP:
                return "kcap"
            elif self == stock.STOCK.STOCK_KCAPL:
                return "kcapl"
            elif self == stock.STOCK.STOCK_KCNY:
                return "kcny"
            elif self == stock.STOCK.STOCK_KDMN:
                return "kdmn"
            elif self == stock.STOCK.STOCK_KE:
                return "ke"
            elif self == stock.STOCK.STOCK_KED:
                return "ked"
            elif self == stock.STOCK.STOCK_KEG:
                return "keg"
            elif self == stock.STOCK.STOCK_KELYA:
                return "kelya"
            elif self == stock.STOCK.STOCK_KELYB:
                return "kelyb"
            elif self == stock.STOCK.STOCK_KEM:
                return "kem"
            elif self == stock.STOCK.STOCK_KEMP:
                return "kemp"
            elif self == stock.STOCK.STOCK_KEMQ:
                return "kemq"
            elif self == stock.STOCK.STOCK_KEN:
                return "ken"
            elif self == stock.STOCK.STOCK_KEP:
                return "kep"
            elif self == stock.STOCK.STOCK_KEQU:
                return "kequ"
            elif self == stock.STOCK.STOCK_KERX:
                return "kerx"
            elif self == stock.STOCK.STOCK_KEX:
                return "kex"
            elif self == stock.STOCK.STOCK_KEY:
                return "key"
            elif self == stock.STOCK.STOCK_KEYS:
                return "keys"
            elif self == stock.STOCK.STOCK_KEYW:
                return "keyw"
            elif self == stock.STOCK.STOCK_KEY_I:
                return "key_i"
            elif self == stock.STOCK.STOCK_KF:
                return "kf"
            elif self == stock.STOCK.STOCK_KFFB:
                return "kffb"
            elif self == stock.STOCK.STOCK_KFN_:
                return "kfn_"
            elif self == stock.STOCK.STOCK_KFRC:
                return "kfrc"
            elif self == stock.STOCK.STOCK_KFS:
                return "kfs"
            elif self == stock.STOCK.STOCK_KFY:
                return "kfy"
            elif self == stock.STOCK.STOCK_KGC:
                return "kgc"
            elif self == stock.STOCK.STOCK_KGJI:
                return "kgji"
            elif self == stock.STOCK.STOCK_KGRN:
                return "kgrn"
            elif self == stock.STOCK.STOCK_KHC:
                return "khc"
            elif self == stock.STOCK.STOCK_KIDS:
                return "kids"
            elif self == stock.STOCK.STOCK_KIM:
                return "kim"
            elif self == stock.STOCK.STOCK_KIM_I:
                return "kim_i"
            elif self == stock.STOCK.STOCK_KIM_J:
                return "kim_j"
            elif self == stock.STOCK.STOCK_KIM_K:
                return "kim_k"
            elif self == stock.STOCK.STOCK_KIM_L:
                return "kim_l"
            elif self == stock.STOCK.STOCK_KIN:
                return "kin"
            elif self == stock.STOCK.STOCK_KINS:
                return "kins"
            elif self == stock.STOCK.STOCK_KIO:
                return "kio"
            elif self == stock.STOCK.STOCK_KIOR:
                return "kior"
            elif self == stock.STOCK.STOCK_KIORW:
                return "kiorw"
            elif self == stock.STOCK.STOCK_KIQ:
                return "kiq"
            elif self == stock.STOCK.STOCK_KIRK:
                return "kirk"
            elif self == stock.STOCK.STOCK_KKR:
                return "kkr"
            elif self == stock.STOCK.STOCK_KKR_A:
                return "kkr_a"
            elif self == stock.STOCK.STOCK_KKR_B:
                return "kkr_b"
            elif self == stock.STOCK.STOCK_KL:
                return "kl"
            elif self == stock.STOCK.STOCK_KLAC:
                return "klac"
            elif self == stock.STOCK.STOCK_KLDW:
                return "kldw"
            elif self == stock.STOCK.STOCK_KLDX:
                return "kldx"
            elif self == stock.STOCK.STOCK_KLIC:
                return "klic"
            elif self == stock.STOCK.STOCK_KLXI:
                return "klxi"
            elif self == stock.STOCK.STOCK_KMB:
                return "kmb"
            elif self == stock.STOCK.STOCK_KMDA:
                return "kmda"
            elif self == stock.STOCK.STOCK_KMF:
                return "kmf"
            elif self == stock.STOCK.STOCK_KMG:
                return "kmg"
            elif self == stock.STOCK.STOCK_KMI:
                return "kmi"
            elif self == stock.STOCK.STOCK_KMI_A:
                return "kmi_a"
            elif self == stock.STOCK.STOCK_KMM:
                return "kmm"
            elif self == stock.STOCK.STOCK_KMPA:
                return "kmpa"
            elif self == stock.STOCK.STOCK_KMPH:
                return "kmph"
            elif self == stock.STOCK.STOCK_KMPR:
                return "kmpr"
            elif self == stock.STOCK.STOCK_KMT:
                return "kmt"
            elif self == stock.STOCK.STOCK_KMX:
                return "kmx"
            elif self == stock.STOCK.STOCK_KN:
                return "kn"
            elif self == stock.STOCK.STOCK_KND:
                return "knd"
            elif self == stock.STOCK.STOCK_KNDI:
                return "kndi"
            elif self == stock.STOCK.STOCK_KNL:
                return "knl"
            elif self == stock.STOCK.STOCK_KNOP:
                return "knop"
            elif self == stock.STOCK.STOCK_KNSL:
                return "knsl"
            elif self == stock.STOCK.STOCK_KNX:
                return "knx"
            elif self == stock.STOCK.STOCK_KO:
                return "ko"
            elif self == stock.STOCK.STOCK_KODK-WS-A:
                return "kodk-ws-a"
            elif self == stock.STOCK.STOCK_KODK-WS:
                return "kodk-ws"
            elif self == stock.STOCK.STOCK_KODK:
                return "kodk"
            elif self == stock.STOCK.STOCK_KOF:
                return "kof"
            elif self == stock.STOCK.STOCK_KONA:
                return "kona"
            elif self == stock.STOCK.STOCK_KONE:
                return "kone"
            elif self == stock.STOCK.STOCK_KOOL:
                return "kool"
            elif self == stock.STOCK.STOCK_KOP:
                return "kop"
            elif self == stock.STOCK.STOCK_KOPN:
                return "kopn"
            elif self == stock.STOCK.STOCK_KOR:
                return "kor"
            elif self == stock.STOCK.STOCK_KORS:
                return "kors"
            elif self == stock.STOCK.STOCK_KOS:
                return "kos"
            elif self == stock.STOCK.STOCK_KOSS:
                return "koss"
            elif self == stock.STOCK.STOCK_KPTI:
                return "kpti"
            elif self == stock.STOCK.STOCK_KR:
                return "kr"
            elif self == stock.STOCK.STOCK_KRA:
                return "kra"
            elif self == stock.STOCK.STOCK_KRC:
                return "krc"
            elif self == stock.STOCK.STOCK_KREF:
                return "kref"
            elif self == stock.STOCK.STOCK_KRG:
                return "krg"
            elif self == stock.STOCK.STOCK_KRMA:
                return "krma"
            elif self == stock.STOCK.STOCK_KRNT:
                return "krnt"
            elif self == stock.STOCK.STOCK_KRNY:
                return "krny"
            elif self == stock.STOCK.STOCK_KRO:
                return "kro"
            elif self == stock.STOCK.STOCK_KRP:
                return "krp"
            elif self == stock.STOCK.STOCK_KRYS:
                return "krys"
            elif self == stock.STOCK.STOCK_KS:
                return "ks"
            elif self == stock.STOCK.STOCK_KSA:
                return "ksa"
            elif self == stock.STOCK.STOCK_KSM:
                return "ksm"
            elif self == stock.STOCK.STOCK_KSS:
                return "kss"
            elif self == stock.STOCK.STOCK_KST:
                return "kst"
            elif self == stock.STOCK.STOCK_KSU:
                return "ksu"
            elif self == stock.STOCK.STOCK_KSU_:
                return "ksu_"
            elif self == stock.STOCK.STOCK_KT:
                return "kt"
            elif self == stock.STOCK.STOCK_KTCC:
                return "ktcc"
            elif self == stock.STOCK.STOCK_KTEC:
                return "ktec"
            elif self == stock.STOCK.STOCK_KTF:
                return "ktf"
            elif self == stock.STOCK.STOCK_KTH:
                return "kth"
            elif self == stock.STOCK.STOCK_KTN:
                return "ktn"
            elif self == stock.STOCK.STOCK_KTOS:
                return "ktos"
            elif self == stock.STOCK.STOCK_KTOV:
                return "ktov"
            elif self == stock.STOCK.STOCK_KTOVW:
                return "ktovw"
            elif self == stock.STOCK.STOCK_KTP:
                return "ktp"
            elif self == stock.STOCK.STOCK_KTWO:
                return "ktwo"
            elif self == stock.STOCK.STOCK_KURA:
                return "kura"
            elif self == stock.STOCK.STOCK_KVHI:
                return "kvhi"
            elif self == stock.STOCK.STOCK_KW:
                return "kw"
            elif self == stock.STOCK.STOCK_KWEB:
                return "kweb"
            elif self == stock.STOCK.STOCK_KWN-CL:
                return "kwn-cl"
            elif self == stock.STOCK.STOCK_KWN:
                return "kwn"
            elif self == stock.STOCK.STOCK_KWR:
                return "kwr"
            elif self == stock.STOCK.STOCK_KYE:
                return "kye"
            elif self == stock.STOCK.STOCK_KYN:
                return "kyn"
            elif self == stock.STOCK.STOCK_KYN_F:
                return "kyn_f"
            elif self == stock.STOCK.STOCK_KYO:
                return "kyo"
            elif self == stock.STOCK.STOCK_L:
                return "l"
            elif self == stock.STOCK.STOCK_LABL:
                return "labl"
            elif self == stock.STOCK.STOCK_LAD:
                return "lad"
            elif self == stock.STOCK.STOCK_LADR:
                return "ladr"
            elif self == stock.STOCK.STOCK_LAKE:
                return "lake"
            elif self == stock.STOCK.STOCK_LAMR:
                return "lamr"
            elif self == stock.STOCK.STOCK_LANC:
                return "lanc"
            elif self == stock.STOCK.STOCK_LAND:
                return "land"
            elif self == stock.STOCK.STOCK_LANDP:
                return "landp"
            elif self == stock.STOCK.STOCK_LAQ:
                return "laq"
            elif self == stock.STOCK.STOCK_LARE:
                return "lare"
            elif self == stock.STOCK.STOCK_LARK:
                return "lark"
            elif self == stock.STOCK.STOCK_LAUR:
                return "laur"
            elif self == stock.STOCK.STOCK_LAWS:
                return "laws"
            elif self == stock.STOCK.STOCK_LAYN:
                return "layn"
            elif self == stock.STOCK.STOCK_LAZ:
                return "laz"
            elif self == stock.STOCK.STOCK_LB:
                return "lb"
            elif self == stock.STOCK.STOCK_LBAI:
                return "lbai"
            elif self == stock.STOCK.STOCK_LBDC:
                return "lbdc"
            elif self == stock.STOCK.STOCK_LBIX:
                return "lbix"
            elif self == stock.STOCK.STOCK_LBRDA:
                return "lbrda"
            elif self == stock.STOCK.STOCK_LBRDK:
                return "lbrdk"
            elif self == stock.STOCK.STOCK_LBTYA:
                return "lbtya"
            elif self == stock.STOCK.STOCK_LBTYB:
                return "lbtyb"
            elif self == stock.STOCK.STOCK_LBTYK:
                return "lbtyk"
            elif self == stock.STOCK.STOCK_LBY:
                return "lby"
            elif self == stock.STOCK.STOCK_LC:
                return "lc"
            elif self == stock.STOCK.STOCK_LCA:
                return "lca"
            elif self == stock.STOCK.STOCK_LCAHU:
                return "lcahu"
            elif self == stock.STOCK.STOCK_LCAHW:
                return "lcahw"
            elif self == stock.STOCK.STOCK_LCI:
                return "lci"
            elif self == stock.STOCK.STOCK_LCII:
                return "lcii"
            elif self == stock.STOCK.STOCK_LCM:
                return "lcm"
            elif self == stock.STOCK.STOCK_LCNB:
                return "lcnb"
            elif self == stock.STOCK.STOCK_LCUT:
                return "lcut"
            elif self == stock.STOCK.STOCK_LDF:
                return "ldf"
            elif self == stock.STOCK.STOCK_LDL:
                return "ldl"
            elif self == stock.STOCK.STOCK_LDOS:
                return "ldos"
            elif self == stock.STOCK.STOCK_LDP:
                return "ldp"
            elif self == stock.STOCK.STOCK_LDR:
                return "ldr"
            elif self == stock.STOCK.STOCK_LE:
                return "le"
            elif self == stock.STOCK.STOCK_LEA:
                return "lea"
            elif self == stock.STOCK.STOCK_LEAD:
                return "lead"
            elif self == stock.STOCK.STOCK_LECO:
                return "leco"
            elif self == stock.STOCK.STOCK_LEDS:
                return "leds"
            elif self == stock.STOCK.STOCK_LEE:
                return "lee"
            elif self == stock.STOCK.STOCK_LEG:
                return "leg"
            elif self == stock.STOCK.STOCK_LEJU:
                return "leju"
            elif self == stock.STOCK.STOCK_LEN-B:
                return "len-b"
            elif self == stock.STOCK.STOCK_LEN:
                return "len"
            elif self == stock.STOCK.STOCK_LENS:
                return "lens"
            elif self == stock.STOCK.STOCK_LEO:
                return "leo"
            elif self == stock.STOCK.STOCK_LEU:
                return "leu"
            elif self == stock.STOCK.STOCK_LEXEA:
                return "lexea"
            elif self == stock.STOCK.STOCK_LEXEB:
                return "lexeb"
            elif self == stock.STOCK.STOCK_LFC:
                return "lfc"
            elif self == stock.STOCK.STOCK_LFEQ:
                return "lfeq"
            elif self == stock.STOCK.STOCK_LFGR:
                return "lfgr"
            elif self == stock.STOCK.STOCK_LFUS:
                return "lfus"
            elif self == stock.STOCK.STOCK_LFVN:
                return "lfvn"
            elif self == stock.STOCK.STOCK_LGCY:
                return "lgcy"
            elif self == stock.STOCK.STOCK_LGCYO:
                return "lgcyo"
            elif self == stock.STOCK.STOCK_LGCYP:
                return "lgcyp"
            elif self == stock.STOCK.STOCK_LGF-A:
                return "lgf-a"
            elif self == stock.STOCK.STOCK_LGF-B:
                return "lgf-b"
            elif self == stock.STOCK.STOCK_LGI:
                return "lgi"
            elif self == stock.STOCK.STOCK_LGIH:
                return "lgih"
            elif self == stock.STOCK.STOCK_LGL:
                return "lgl"
            elif self == stock.STOCK.STOCK_LGLR:
                return "lglr"
            elif self == stock.STOCK.STOCK_LGND:
                return "lgnd"
            elif self == stock.STOCK.STOCK_LH:
                return "lh"
            elif self == stock.STOCK.STOCK_LHCG:
                return "lhcg"
            elif self == stock.STOCK.STOCK_LHO:
                return "lho"
            elif self == stock.STOCK.STOCK_LHO_I:
                return "lho_i"
            elif self == stock.STOCK.STOCK_LHO_J:
                return "lho_j"
            elif self == stock.STOCK.STOCK_LIFE:
                return "life"
            elif self == stock.STOCK.STOCK_LII:
                return "lii"
            elif self == stock.STOCK.STOCK_LILA:
                return "lila"
            elif self == stock.STOCK.STOCK_LILAK:
                return "lilak"
            elif self == stock.STOCK.STOCK_LINC:
                return "linc"
            elif self == stock.STOCK.STOCK_LIND:
                return "lind"
            elif self == stock.STOCK.STOCK_LINDW:
                return "lindw"
            elif self == stock.STOCK.STOCK_LINK:
                return "link"
            elif self == stock.STOCK.STOCK_LINU:
                return "linu"
            elif self == stock.STOCK.STOCK_LION:
                return "lion"
            elif self == stock.STOCK.STOCK_LIQT:
                return "liqt"
            elif self == stock.STOCK.STOCK_LITB:
                return "litb"
            elif self == stock.STOCK.STOCK_LITE:
                return "lite"
            elif self == stock.STOCK.STOCK_LIVE:
                return "live"
            elif self == stock.STOCK.STOCK_LIVN:
                return "livn"
            elif self == stock.STOCK.STOCK_LJPC:
                return "ljpc"
            elif self == stock.STOCK.STOCK_LKFN:
                return "lkfn"
            elif self == stock.STOCK.STOCK_LKOR:
                return "lkor"
            elif self == stock.STOCK.STOCK_LKQ:
                return "lkq"
            elif self == stock.STOCK.STOCK_LKSD:
                return "lksd"
            elif self == stock.STOCK.STOCK_LL:
                return "ll"
            elif self == stock.STOCK.STOCK_LLEX:
                return "llex"
            elif self == stock.STOCK.STOCK_LLIT:
                return "llit"
            elif self == stock.STOCK.STOCK_LLL:
                return "lll"
            elif self == stock.STOCK.STOCK_LLNW:
                return "llnw"
            elif self == stock.STOCK.STOCK_LLQD:
                return "llqd"
            elif self == stock.STOCK.STOCK_LLY:
                return "lly"
            elif self == stock.STOCK.STOCK_LM:
                return "lm"
            elif self == stock.STOCK.STOCK_LMAT:
                return "lmat"
            elif self == stock.STOCK.STOCK_LMB:
                return "lmb"
            elif self == stock.STOCK.STOCK_LMFA:
                return "lmfa"
            elif self == stock.STOCK.STOCK_LMFAW:
                return "lmfaw"
            elif self == stock.STOCK.STOCK_LMHA:
                return "lmha"
            elif self == stock.STOCK.STOCK_LMHB:
                return "lmhb"
            elif self == stock.STOCK.STOCK_LMNR:
                return "lmnr"
            elif self == stock.STOCK.STOCK_LMNX:
                return "lmnx"
            elif self == stock.STOCK.STOCK_LMOS:
                return "lmos"
            elif self == stock.STOCK.STOCK_LMRK:
                return "lmrk"
            elif self == stock.STOCK.STOCK_LMRKO:
                return "lmrko"
            elif self == stock.STOCK.STOCK_LMRKP:
                return "lmrkp"
            elif self == stock.STOCK.STOCK_LMT:
                return "lmt"
            elif self == stock.STOCK.STOCK_LN:
                return "ln"
            elif self == stock.STOCK.STOCK_LNC-WS:
                return "lnc-ws"
            elif self == stock.STOCK.STOCK_LNC:
                return "lnc"
            elif self == stock.STOCK.STOCK_LNCE:
                return "lnce"
            elif self == stock.STOCK.STOCK_LND:
                return "lnd"
            elif self == stock.STOCK.STOCK_LNDC:
                return "lndc"
            elif self == stock.STOCK.STOCK_LNG:
                return "lng"
            elif self == stock.STOCK.STOCK_LNGR:
                return "lngr"
            elif self == stock.STOCK.STOCK_LNN:
                return "lnn"
            elif self == stock.STOCK.STOCK_LNT:
                return "lnt"
            elif self == stock.STOCK.STOCK_LNTH:
                return "lnth"
            elif self == stock.STOCK.STOCK_LOAN:
                return "loan"
            elif self == stock.STOCK.STOCK_LOB:
                return "lob"
            elif self == stock.STOCK.STOCK_LOCO:
                return "loco"
            elif self == stock.STOCK.STOCK_LODE:
                return "lode"
            elif self == stock.STOCK.STOCK_LOGI:
                return "logi"
            elif self == stock.STOCK.STOCK_LOGM:
                return "logm"
            elif self == stock.STOCK.STOCK_LOGO:
                return "logo"
            elif self == stock.STOCK.STOCK_LOMA:
                return "loma"
            elif self == stock.STOCK.STOCK_LONE:
                return "lone"
            elif self == stock.STOCK.STOCK_LOPE:
                return "lope"
            elif self == stock.STOCK.STOCK_LOR:
                return "lor"
            elif self == stock.STOCK.STOCK_LORL:
                return "lorl"
            elif self == stock.STOCK.STOCK_LOV:
                return "lov"
            elif self == stock.STOCK.STOCK_LOVW:
                return "lovw"
            elif self == stock.STOCK.STOCK_LOW:
                return "low"
            elif self == stock.STOCK.STOCK_LOXO:
                return "loxo"
            elif self == stock.STOCK.STOCK_LPCN:
                return "lpcn"
            elif self == stock.STOCK.STOCK_LPG:
                return "lpg"
            elif self == stock.STOCK.STOCK_LPI:
                return "lpi"
            elif self == stock.STOCK.STOCK_LPL:
                return "lpl"
            elif self == stock.STOCK.STOCK_LPLA:
                return "lpla"
            elif self == stock.STOCK.STOCK_LPNT:
                return "lpnt"
            elif self == stock.STOCK.STOCK_LPSN:
                return "lpsn"
            elif self == stock.STOCK.STOCK_LPT:
                return "lpt"
            elif self == stock.STOCK.STOCK_LPTH:
                return "lpth"
            elif self == stock.STOCK.STOCK_LPTX:
                return "lptx"
            elif self == stock.STOCK.STOCK_LPX:
                return "lpx"
            elif self == stock.STOCK.STOCK_LQ:
                return "lq"
            elif self == stock.STOCK.STOCK_LQDT:
                return "lqdt"
            elif self == stock.STOCK.STOCK_LRAD:
                return "lrad"
            elif self == stock.STOCK.STOCK_LRCX:
                return "lrcx"
            elif self == stock.STOCK.STOCK_LRET:
                return "lret"
            elif self == stock.STOCK.STOCK_LRGE:
                return "lrge"
            elif self == stock.STOCK.STOCK_LRN:
                return "lrn"
            elif self == stock.STOCK.STOCK_LSBK:
                return "lsbk"
            elif self == stock.STOCK.STOCK_LSCC:
                return "lscc"
            elif self == stock.STOCK.STOCK_LSI:
                return "lsi"
            elif self == stock.STOCK.STOCK_LSTR:
                return "lstr"
            elif self == stock.STOCK.STOCK_LSVX:
                return "lsvx"
            elif self == stock.STOCK.STOCK_LSXMA:
                return "lsxma"
            elif self == stock.STOCK.STOCK_LSXMB:
                return "lsxmb"
            elif self == stock.STOCK.STOCK_LSXMK:
                return "lsxmk"
            elif self == stock.STOCK.STOCK_LTBR:
                return "ltbr"
            elif self == stock.STOCK.STOCK_LTC:
                return "ltc"
            elif self == stock.STOCK.STOCK_LTEA:
                return "ltea"
            elif self == stock.STOCK.STOCK_LTM:
                return "ltm"
            elif self == stock.STOCK.STOCK_LTRPA:
                return "ltrpa"
            elif self == stock.STOCK.STOCK_LTRPB:
                return "ltrpb"
            elif self == stock.STOCK.STOCK_LTRX:
                return "ltrx"
            elif self == stock.STOCK.STOCK_LTS:
                return "lts"
            elif self == stock.STOCK.STOCK_LTS_A:
                return "lts_a"
            elif self == stock.STOCK.STOCK_LTXB:
                return "ltxb"
            elif self == stock.STOCK.STOCK_LUB:
                return "lub"
            elif self == stock.STOCK.STOCK_LUK:
                return "luk"
            elif self == stock.STOCK.STOCK_LULU:
                return "lulu"
            elif self == stock.STOCK.STOCK_LUNA:
                return "luna"
            elif self == stock.STOCK.STOCK_LUV:
                return "luv"
            elif self == stock.STOCK.STOCK_LVHB:
                return "lvhb"
            elif self == stock.STOCK.STOCK_LVHD:
                return "lvhd"
            elif self == stock.STOCK.STOCK_LVHE:
                return "lvhe"
            elif self == stock.STOCK.STOCK_LVHI:
                return "lvhi"
            elif self == stock.STOCK.STOCK_LVIN:
                return "lvin"
            elif self == stock.STOCK.STOCK_LVLT:
                return "lvlt"
            elif self == stock.STOCK.STOCK_LVNTA:
                return "lvnta"
            elif self == stock.STOCK.STOCK_LVNTB:
                return "lvntb"
            elif self == stock.STOCK.STOCK_LVS:
                return "lvs"
            elif self == stock.STOCK.STOCK_LVUS:
                return "lvus"
            elif self == stock.STOCK.STOCK_LW:
                return "lw"
            elif self == stock.STOCK.STOCK_LWAY:
                return "lway"
            elif self == stock.STOCK.STOCK_LXFR:
                return "lxfr"
            elif self == stock.STOCK.STOCK_LXFT:
                return "lxft"
            elif self == stock.STOCK.STOCK_LXP:
                return "lxp"
            elif self == stock.STOCK.STOCK_LXP_C:
                return "lxp_c"
            elif self == stock.STOCK.STOCK_LXRX:
                return "lxrx"
            elif self == stock.STOCK.STOCK_LXU:
                return "lxu"
            elif self == stock.STOCK.STOCK_LYB:
                return "lyb"
            elif self == stock.STOCK.STOCK_LYG:
                return "lyg"
            elif self == stock.STOCK.STOCK_LYL:
                return "lyl"
            elif self == stock.STOCK.STOCK_LYTS:
                return "lyts"
            elif self == stock.STOCK.STOCK_LYV:
                return "lyv"
            elif self == stock.STOCK.STOCK_LZB:
                return "lzb"
            elif self == stock.STOCK.STOCK_M:
                return "m"
            elif self == stock.STOCK.STOCK_MA:
                return "ma"
            elif self == stock.STOCK.STOCK_MAA:
                return "maa"
            elif self == stock.STOCK.STOCK_MAA_I:
                return "maa_i"
            elif self == stock.STOCK.STOCK_MAB:
                return "mab"
            elif self == stock.STOCK.STOCK_MAC:
                return "mac"
            elif self == stock.STOCK.STOCK_MACK:
                return "mack"
            elif self == stock.STOCK.STOCK_MACQ:
                return "macq"
            elif self == stock.STOCK.STOCK_MACQU:
                return "macqu"
            elif self == stock.STOCK.STOCK_MACQW:
                return "macqw"
            elif self == stock.STOCK.STOCK_MAG:
                return "mag"
            elif self == stock.STOCK.STOCK_MAGA:
                return "maga"
            elif self == stock.STOCK.STOCK_MAGS:
                return "mags"
            elif self == stock.STOCK.STOCK_MAIN:
                return "main"
            elif self == stock.STOCK.STOCK_MAMS:
                return "mams"
            elif self == stock.STOCK.STOCK_MAN:
                return "man"
            elif self == stock.STOCK.STOCK_MANH:
                return "manh"
            elif self == stock.STOCK.STOCK_MANT:
                return "mant"
            elif self == stock.STOCK.STOCK_MANU:
                return "manu"
            elif self == stock.STOCK.STOCK_MAPI:
                return "mapi"
            elif self == stock.STOCK.STOCK_MAR:
                return "mar"
            elif self == stock.STOCK.STOCK_MARA:
                return "mara"
            elif self == stock.STOCK.STOCK_MARK:
                return "mark"
            elif self == stock.STOCK.STOCK_MARPS:
                return "marps"
            elif self == stock.STOCK.STOCK_MAS:
                return "mas"
            elif self == stock.STOCK.STOCK_MASI:
                return "masi"
            elif self == stock.STOCK.STOCK_MAT:
                return "mat"
            elif self == stock.STOCK.STOCK_MATF:
                return "matf"
            elif self == stock.STOCK.STOCK_MATR:
                return "matr"
            elif self == stock.STOCK.STOCK_MATW:
                return "matw"
            elif self == stock.STOCK.STOCK_MATX:
                return "matx"
            elif self == stock.STOCK.STOCK_MAV:
                return "mav"
            elif self == stock.STOCK.STOCK_MAXR:
                return "maxr"
            elif self == stock.STOCK.STOCK_MAYS:
                return "mays"
            elif self == stock.STOCK.STOCK_MB:
                return "mb"
            elif self == stock.STOCK.STOCK_MBCN:
                return "mbcn"
            elif self == stock.STOCK.STOCK_MBFI:
                return "mbfi"
            elif self == stock.STOCK.STOCK_MBFIP:
                return "mbfip"
            elif self == stock.STOCK.STOCK_MBI:
                return "mbi"
            elif self == stock.STOCK.STOCK_MBII:
                return "mbii"
            elif self == stock.STOCK.STOCK_MBIN:
                return "mbin"
            elif self == stock.STOCK.STOCK_MBIO:
                return "mbio"
            elif self == stock.STOCK.STOCK_MBOT:
                return "mbot"
            elif self == stock.STOCK.STOCK_MBRX:
                return "mbrx"
            elif self == stock.STOCK.STOCK_MBT:
                return "mbt"
            elif self == stock.STOCK.STOCK_MBTF:
                return "mbtf"
            elif self == stock.STOCK.STOCK_MBUU:
                return "mbuu"
            elif self == stock.STOCK.STOCK_MBVX:
                return "mbvx"
            elif self == stock.STOCK.STOCK_MBWM:
                return "mbwm"
            elif self == stock.STOCK.STOCK_MC:
                return "mc"
            elif self == stock.STOCK.STOCK_MCA:
                return "mca"
            elif self == stock.STOCK.STOCK_MCB:
                return "mcb"
            elif self == stock.STOCK.STOCK_MCBC:
                return "mcbc"
            elif self == stock.STOCK.STOCK_MCC:
                return "mcc"
            elif self == stock.STOCK.STOCK_MCD:
                return "mcd"
            elif self == stock.STOCK.STOCK_MCEF:
                return "mcef"
            elif self == stock.STOCK.STOCK_MCEP:
                return "mcep"
            elif self == stock.STOCK.STOCK_MCF:
                return "mcf"
            elif self == stock.STOCK.STOCK_MCFT:
                return "mcft"
            elif self == stock.STOCK.STOCK_MCHP:
                return "mchp"
            elif self == stock.STOCK.STOCK_MCHX:
                return "mchx"
            elif self == stock.STOCK.STOCK_MCI:
                return "mci"
            elif self == stock.STOCK.STOCK_MCK:
                return "mck"
            elif self == stock.STOCK.STOCK_MCN:
                return "mcn"
            elif self == stock.STOCK.STOCK_MCO:
                return "mco"
            elif self == stock.STOCK.STOCK_MCR:
                return "mcr"
            elif self == stock.STOCK.STOCK_MCRB:
                return "mcrb"
            elif self == stock.STOCK.STOCK_MCRI:
                return "mcri"
            elif self == stock.STOCK.STOCK_MCRN:
                return "mcrn"
            elif self == stock.STOCK.STOCK_MCS:
                return "mcs"
            elif self == stock.STOCK.STOCK_MCV:
                return "mcv"
            elif self == stock.STOCK.STOCK_MCX:
                return "mcx"
            elif self == stock.STOCK.STOCK_MCY:
                return "mcy"
            elif self == stock.STOCK.STOCK_MD:
                return "md"
            elif self == stock.STOCK.STOCK_MDB:
                return "mdb"
            elif self == stock.STOCK.STOCK_MDC:
                return "mdc"
            elif self == stock.STOCK.STOCK_MDCA:
                return "mdca"
            elif self == stock.STOCK.STOCK_MDCO:
                return "mdco"
            elif self == stock.STOCK.STOCK_MDGL:
                return "mdgl"
            elif self == stock.STOCK.STOCK_MDGS:
                return "mdgs"
            elif self == stock.STOCK.STOCK_MDLQ:
                return "mdlq"
            elif self == stock.STOCK.STOCK_MDLX:
                return "mdlx"
            elif self == stock.STOCK.STOCK_MDLY:
                return "mdly"
            elif self == stock.STOCK.STOCK_MDLZ:
                return "mdlz"
            elif self == stock.STOCK.STOCK_MDP:
                return "mdp"
            elif self == stock.STOCK.STOCK_MDR:
                return "mdr"
            elif self == stock.STOCK.STOCK_MDRX:
                return "mdrx"
            elif self == stock.STOCK.STOCK_MDSO:
                return "mdso"
            elif self == stock.STOCK.STOCK_MDT:
                return "mdt"
            elif self == stock.STOCK.STOCK_MDU:
                return "mdu"
            elif self == stock.STOCK.STOCK_MDVX:
                return "mdvx"
            elif self == stock.STOCK.STOCK_MDVXW:
                return "mdvxw"
            elif self == stock.STOCK.STOCK_MDWD:
                return "mdwd"
            elif self == stock.STOCK.STOCK_MDXG:
                return "mdxg"
            elif self == stock.STOCK.STOCK_MEAR:
                return "mear"
            elif self == stock.STOCK.STOCK_MED:
                return "med"
            elif self == stock.STOCK.STOCK_MEDP:
                return "medp"
            elif self == stock.STOCK.STOCK_MEET:
                return "meet"
            elif self == stock.STOCK.STOCK_MEI:
                return "mei"
            elif self == stock.STOCK.STOCK_MEIP:
                return "meip"
            elif self == stock.STOCK.STOCK_MELI:
                return "meli"
            elif self == stock.STOCK.STOCK_MELR:
                return "melr"
            elif self == stock.STOCK.STOCK_MEN:
                return "men"
            elif self == stock.STOCK.STOCK_MENU:
                return "menu"
            elif self == stock.STOCK.STOCK_MEOH:
                return "meoh"
            elif self == stock.STOCK.STOCK_MERC:
                return "merc"
            elif self == stock.STOCK.STOCK_MER_K:
                return "mer_k"
            elif self == stock.STOCK.STOCK_MER_P:
                return "mer_p"
            elif self == stock.STOCK.STOCK_MESO:
                return "meso"
            elif self == stock.STOCK.STOCK_MET:
                return "met"
            elif self == stock.STOCK.STOCK_METC:
                return "metc"
            elif self == stock.STOCK.STOCK_MET_A:
                return "met_a"
            elif self == stock.STOCK.STOCK_MEXX:
                return "mexx"
            elif self == stock.STOCK.STOCK_MFA:
                return "mfa"
            elif self == stock.STOCK.STOCK_MFA_B:
                return "mfa_b"
            elif self == stock.STOCK.STOCK_MFC:
                return "mfc"
            elif self == stock.STOCK.STOCK_MFCB:
                return "mfcb"
            elif self == stock.STOCK.STOCK_MFDX:
                return "mfdx"
            elif self == stock.STOCK.STOCK_MFEM:
                return "mfem"
            elif self == stock.STOCK.STOCK_MFG:
                return "mfg"
            elif self == stock.STOCK.STOCK_MFGP:
                return "mfgp"
            elif self == stock.STOCK.STOCK_MFIN:
                return "mfin"
            elif self == stock.STOCK.STOCK_MFINL:
                return "mfinl"
            elif self == stock.STOCK.STOCK_MFL:
                return "mfl"
            elif self == stock.STOCK.STOCK_MFM:
                return "mfm"
            elif self == stock.STOCK.STOCK_MFNC:
                return "mfnc"
            elif self == stock.STOCK.STOCK_MFO:
                return "mfo"
            elif self == stock.STOCK.STOCK_MFSF:
                return "mfsf"
            elif self == stock.STOCK.STOCK_MFT:
                return "mft"
            elif self == stock.STOCK.STOCK_MFUS:
                return "mfus"
            elif self == stock.STOCK.STOCK_MFV:
                return "mfv"
            elif self == stock.STOCK.STOCK_MG:
                return "mg"
            elif self == stock.STOCK.STOCK_MGA:
                return "mga"
            elif self == stock.STOCK.STOCK_MGCD:
                return "mgcd"
            elif self == stock.STOCK.STOCK_MGEE:
                return "mgee"
            elif self == stock.STOCK.STOCK_MGEN:
                return "mgen"
            elif self == stock.STOCK.STOCK_MGF:
                return "mgf"
            elif self == stock.STOCK.STOCK_MGI:
                return "mgi"
            elif self == stock.STOCK.STOCK_MGIC:
                return "mgic"
            elif self == stock.STOCK.STOCK_MGLN:
                return "mgln"
            elif self == stock.STOCK.STOCK_MGM:
                return "mgm"
            elif self == stock.STOCK.STOCK_MGNX:
                return "mgnx"
            elif self == stock.STOCK.STOCK_MGP:
                return "mgp"
            elif self == stock.STOCK.STOCK_MGPI:
                return "mgpi"
            elif self == stock.STOCK.STOCK_MGRC:
                return "mgrc"
            elif self == stock.STOCK.STOCK_MGU:
                return "mgu"
            elif self == stock.STOCK.STOCK_MGYR:
                return "mgyr"
            elif self == stock.STOCK.STOCK_MHD:
                return "mhd"
            elif self == stock.STOCK.STOCK_MHE:
                return "mhe"
            elif self == stock.STOCK.STOCK_MHF:
                return "mhf"
            elif self == stock.STOCK.STOCK_MHH:
                return "mhh"
            elif self == stock.STOCK.STOCK_MHI:
                return "mhi"
            elif self == stock.STOCK.STOCK_MHK:
                return "mhk"
            elif self == stock.STOCK.STOCK_MHLA:
                return "mhla"
            elif self == stock.STOCK.STOCK_MHLD:
                return "mhld"
            elif self == stock.STOCK.STOCK_MHN:
                return "mhn"
            elif self == stock.STOCK.STOCK_MHNC:
                return "mhnc"
            elif self == stock.STOCK.STOCK_MHO:
                return "mho"
            elif self == stock.STOCK.STOCK_MH_A:
                return "mh_a"
            elif self == stock.STOCK.STOCK_MH_C:
                return "mh_c"
            elif self == stock.STOCK.STOCK_MH_D:
                return "mh_d"
            elif self == stock.STOCK.STOCK_MIC:
                return "mic"
            elif self == stock.STOCK.STOCK_MICR:
                return "micr"
            elif self == stock.STOCK.STOCK_MICT:
                return "mict"
            elif self == stock.STOCK.STOCK_MICTW:
                return "mictw"
            elif self == stock.STOCK.STOCK_MIDD:
                return "midd"
            elif self == stock.STOCK.STOCK_MIE:
                return "mie"
            elif self == stock.STOCK.STOCK_MIII:
                return "miii"
            elif self == stock.STOCK.STOCK_MIIIU:
                return "miiiu"
            elif self == stock.STOCK.STOCK_MIIIW:
                return "miiiw"
            elif self == stock.STOCK.STOCK_MIK:
                return "mik"
            elif self == stock.STOCK.STOCK_MILN:
                return "miln"
            elif self == stock.STOCK.STOCK_MIME:
                return "mime"
            elif self == stock.STOCK.STOCK_MIN:
                return "min"
            elif self == stock.STOCK.STOCK_MIND:
                return "mind"
            elif self == stock.STOCK.STOCK_MINDP:
                return "mindp"
            elif self == stock.STOCK.STOCK_MINI:
                return "mini"
            elif self == stock.STOCK.STOCK_MITK:
                return "mitk"
            elif self == stock.STOCK.STOCK_MITL:
                return "mitl"
            elif self == stock.STOCK.STOCK_MITT:
                return "mitt"
            elif self == stock.STOCK.STOCK_MITT_A:
                return "mitt_a"
            elif self == stock.STOCK.STOCK_MITT_B:
                return "mitt_b"
            elif self == stock.STOCK.STOCK_MIW:
                return "miw"
            elif self == stock.STOCK.STOCK_MIXT:
                return "mixt"
            elif self == stock.STOCK.STOCK_MIY:
                return "miy"
            elif self == stock.STOCK.STOCK_MJCO:
                return "mjco"
            elif self == stock.STOCK.STOCK_MKC-V:
                return "mkc-v"
            elif self == stock.STOCK.STOCK_MKC:
                return "mkc"
            elif self == stock.STOCK.STOCK_MKL:
                return "mkl"
            elif self == stock.STOCK.STOCK_MKSI:
                return "mksi"
            elif self == stock.STOCK.STOCK_MKTX:
                return "mktx"
            elif self == stock.STOCK.STOCK_MLAB:
                return "mlab"
            elif self == stock.STOCK.STOCK_MLCO:
                return "mlco"
            elif self == stock.STOCK.STOCK_MLHR:
                return "mlhr"
            elif self == stock.STOCK.STOCK_MLI:
                return "mli"
            elif self == stock.STOCK.STOCK_MLM:
                return "mlm"
            elif self == stock.STOCK.STOCK_MLNK:
                return "mlnk"
            elif self == stock.STOCK.STOCK_MLNT:
                return "mlnt"
            elif self == stock.STOCK.STOCK_MLNX:
                return "mlnx"
            elif self == stock.STOCK.STOCK_MLP:
                return "mlp"
            elif self == stock.STOCK.STOCK_MLPB:
                return "mlpb"
            elif self == stock.STOCK.STOCK_MLPQ:
                return "mlpq"
            elif self == stock.STOCK.STOCK_MLPZ:
                return "mlpz"
            elif self == stock.STOCK.STOCK_MLQD:
                return "mlqd"
            elif self == stock.STOCK.STOCK_MLR:
                return "mlr"
            elif self == stock.STOCK.STOCK_MLSS:
                return "mlss"
            elif self == stock.STOCK.STOCK_MLTI:
                return "mlti"
            elif self == stock.STOCK.STOCK_MLVF:
                return "mlvf"
            elif self == stock.STOCK.STOCK_MMAC:
                return "mmac"
            elif self == stock.STOCK.STOCK_MMC:
                return "mmc"
            elif self == stock.STOCK.STOCK_MMD:
                return "mmd"
            elif self == stock.STOCK.STOCK_MMDM:
                return "mmdm"
            elif self == stock.STOCK.STOCK_MMDMR:
                return "mmdmr"
            elif self == stock.STOCK.STOCK_MMDMU:
                return "mmdmu"
            elif self == stock.STOCK.STOCK_MMDMW:
                return "mmdmw"
            elif self == stock.STOCK.STOCK_MMI:
                return "mmi"
            elif self == stock.STOCK.STOCK_MMIT:
                return "mmit"
            elif self == stock.STOCK.STOCK_MMLP:
                return "mmlp"
            elif self == stock.STOCK.STOCK_MMM:
                return "mmm"
            elif self == stock.STOCK.STOCK_MMP:
                return "mmp"
            elif self == stock.STOCK.STOCK_MMS:
                return "mms"
            elif self == stock.STOCK.STOCK_MMSI:
                return "mmsi"
            elif self == stock.STOCK.STOCK_MMT:
                return "mmt"
            elif self == stock.STOCK.STOCK_MMU:
                return "mmu"
            elif self == stock.STOCK.STOCK_MMV:
                return "mmv"
            elif self == stock.STOCK.STOCK_MMYT:
                return "mmyt"
            elif self == stock.STOCK.STOCK_MN:
                return "mn"
            elif self == stock.STOCK.STOCK_MNDO:
                return "mndo"
            elif self == stock.STOCK.STOCK_MNE:
                return "mne"
            elif self == stock.STOCK.STOCK_MNGA:
                return "mnga"
            elif self == stock.STOCK.STOCK_MNI:
                return "mni"
            elif self == stock.STOCK.STOCK_MNK:
                return "mnk"
            elif self == stock.STOCK.STOCK_MNKD:
                return "mnkd"
            elif self == stock.STOCK.STOCK_MNOV:
                return "mnov"
            elif self == stock.STOCK.STOCK_MNP:
                return "mnp"
            elif self == stock.STOCK.STOCK_MNR:
                return "mnr"
            elif self == stock.STOCK.STOCK_MNRO:
                return "mnro"
            elif self == stock.STOCK.STOCK_MNR_C:
                return "mnr_c"
            elif self == stock.STOCK.STOCK_MNST:
                return "mnst"
            elif self == stock.STOCK.STOCK_MNTA:
                return "mnta"
            elif self == stock.STOCK.STOCK_MNTX:
                return "mntx"
            elif self == stock.STOCK.STOCK_MO:
                return "mo"
            elif self == stock.STOCK.STOCK_MOBL:
                return "mobl"
            elif self == stock.STOCK.STOCK_MOC:
                return "moc"
            elif self == stock.STOCK.STOCK_MOD:
                return "mod"
            elif self == stock.STOCK.STOCK_MODN:
                return "modn"
            elif self == stock.STOCK.STOCK_MOFG:
                return "mofg"
            elif self == stock.STOCK.STOCK_MOG-A:
                return "mog-a"
            elif self == stock.STOCK.STOCK_MOG-B:
                return "mog-b"
            elif self == stock.STOCK.STOCK_MOGLC:
                return "moglc"
            elif self == stock.STOCK.STOCK_MOH:
                return "moh"
            elif self == stock.STOCK.STOCK_MOLC:
                return "molc"
            elif self == stock.STOCK.STOCK_MOMO:
                return "momo"
            elif self == stock.STOCK.STOCK_MON:
                return "mon"
            elif self == stock.STOCK.STOCK_MORN:
                return "morn"
            elif self == stock.STOCK.STOCK_MOS:
                return "mos"
            elif self == stock.STOCK.STOCK_MOSC-U:
                return "mosc-u"
            elif self == stock.STOCK.STOCK_MOSY:
                return "mosy"
            elif self == stock.STOCK.STOCK_MOTI:
                return "moti"
            elif self == stock.STOCK.STOCK_MOV:
                return "mov"
            elif self == stock.STOCK.STOCK_MOXC:
                return "moxc"
            elif self == stock.STOCK.STOCK_MPA:
                return "mpa"
            elif self == stock.STOCK.STOCK_MPAA:
                return "mpaa"
            elif self == stock.STOCK.STOCK_MPAC:
                return "mpac"
            elif self == stock.STOCK.STOCK_MPACU:
                return "mpacu"
            elif self == stock.STOCK.STOCK_MPACW:
                return "mpacw"
            elif self == stock.STOCK.STOCK_MPB:
                return "mpb"
            elif self == stock.STOCK.STOCK_MPC:
                return "mpc"
            elif self == stock.STOCK.STOCK_MPCT:
                return "mpct"
            elif self == stock.STOCK.STOCK_MPLX:
                return "mplx"
            elif self == stock.STOCK.STOCK_MPO:
                return "mpo"
            elif self == stock.STOCK.STOCK_MPV:
                return "mpv"
            elif self == stock.STOCK.STOCK_MPVD:
                return "mpvd"
            elif self == stock.STOCK.STOCK_MPW:
                return "mpw"
            elif self == stock.STOCK.STOCK_MPWR:
                return "mpwr"
            elif self == stock.STOCK.STOCK_MPX:
                return "mpx"
            elif self == stock.STOCK.STOCK_MP_D:
                return "mp_d"
            elif self == stock.STOCK.STOCK_MQT:
                return "mqt"
            elif self == stock.STOCK.STOCK_MQY:
                return "mqy"
            elif self == stock.STOCK.STOCK_MRAM:
                return "mram"
            elif self == stock.STOCK.STOCK_MRBK:
                return "mrbk"
            elif self == stock.STOCK.STOCK_MRC:
                return "mrc"
            elif self == stock.STOCK.STOCK_MRCC:
                return "mrcc"
            elif self == stock.STOCK.STOCK_MRCY:
                return "mrcy"
            elif self == stock.STOCK.STOCK_MRDN:
                return "mrdn"
            elif self == stock.STOCK.STOCK_MRDNW:
                return "mrdnw"
            elif self == stock.STOCK.STOCK_MRIN:
                return "mrin"
            elif self == stock.STOCK.STOCK_MRK:
                return "mrk"
            elif self == stock.STOCK.STOCK_MRLN:
                return "mrln"
            elif self == stock.STOCK.STOCK_MRNS:
                return "mrns"
            elif self == stock.STOCK.STOCK_MRO:
                return "mro"
            elif self == stock.STOCK.STOCK_MRRL:
                return "mrrl"
            elif self == stock.STOCK.STOCK_MRSN:
                return "mrsn"
            elif self == stock.STOCK.STOCK_MRT:
                return "mrt"
            elif self == stock.STOCK.STOCK_MRTN:
                return "mrtn"
            elif self == stock.STOCK.STOCK_MRTX:
                return "mrtx"
            elif self == stock.STOCK.STOCK_MRUS:
                return "mrus"
            elif self == stock.STOCK.STOCK_MRVL:
                return "mrvl"
            elif self == stock.STOCK.STOCK_MS:
                return "ms"
            elif self == stock.STOCK.STOCK_MSA:
                return "msa"
            elif self == stock.STOCK.STOCK_MSB:
                return "msb"
            elif self == stock.STOCK.STOCK_MSBF:
                return "msbf"
            elif self == stock.STOCK.STOCK_MSBI:
                return "msbi"
            elif self == stock.STOCK.STOCK_MSCA:
                return "msca"
            elif self == stock.STOCK.STOCK_MSCC:
                return "mscc"
            elif self == stock.STOCK.STOCK_MSCI:
                return "msci"
            elif self == stock.STOCK.STOCK_MSD:
                return "msd"
            elif self == stock.STOCK.STOCK_MSDI:
                return "msdi"
            elif self == stock.STOCK.STOCK_MSDIW:
                return "msdiw"
            elif self == stock.STOCK.STOCK_MSEX:
                return "msex"
            elif self == stock.STOCK.STOCK_MSF:
                return "msf"
            elif self == stock.STOCK.STOCK_MSFG:
                return "msfg"
            elif self == stock.STOCK.STOCK_MSFT:
                return "msft"
            elif self == stock.STOCK.STOCK_MSG:
                return "msg"
            elif self == stock.STOCK.STOCK_MSGN:
                return "msgn"
            elif self == stock.STOCK.STOCK_MSI:
                return "msi"
            elif self == stock.STOCK.STOCK_MSL:
                return "msl"
            elif self == stock.STOCK.STOCK_MSM:
                return "msm"
            elif self == stock.STOCK.STOCK_MSN:
                return "msn"
            elif self == stock.STOCK.STOCK_MSON:
                return "mson"
            elif self == stock.STOCK.STOCK_MSP:
                return "msp"
            elif self == stock.STOCK.STOCK_MSTR:
                return "mstr"
            elif self == stock.STOCK.STOCK_MS_A:
                return "ms_a"
            elif self == stock.STOCK.STOCK_MS_E:
                return "ms_e"
            elif self == stock.STOCK.STOCK_MS_F:
                return "ms_f"
            elif self == stock.STOCK.STOCK_MS_G:
                return "ms_g"
            elif self == stock.STOCK.STOCK_MS_I:
                return "ms_i"
            elif self == stock.STOCK.STOCK_MS_K:
                return "ms_k"
            elif self == stock.STOCK.STOCK_MT:
                return "mt"
            elif self == stock.STOCK.STOCK_MTB-WS:
                return "mtb-ws"
            elif self == stock.STOCK.STOCK_MTB:
                return "mtb"
            elif self == stock.STOCK.STOCK_MTBC:
                return "mtbc"
            elif self == stock.STOCK.STOCK_MTBCP:
                return "mtbcp"
            elif self == stock.STOCK.STOCK_MTB_:
                return "mtb_"
            elif self == stock.STOCK.STOCK_MTB_C:
                return "mtb_c"
            elif self == stock.STOCK.STOCK_MTCH:
                return "mtch"
            elif self == stock.STOCK.STOCK_MTD:
                return "mtd"
            elif self == stock.STOCK.STOCK_MTDR:
                return "mtdr"
            elif self == stock.STOCK.STOCK_MTEM:
                return "mtem"
            elif self == stock.STOCK.STOCK_MTEX:
                return "mtex"
            elif self == stock.STOCK.STOCK_MTFB:
                return "mtfb"
            elif self == stock.STOCK.STOCK_MTFBW:
                return "mtfbw"
            elif self == stock.STOCK.STOCK_MTG:
                return "mtg"
            elif self == stock.STOCK.STOCK_MTGE:
                return "mtge"
            elif self == stock.STOCK.STOCK_MTGEP:
                return "mtgep"
            elif self == stock.STOCK.STOCK_MTH:
                return "mth"
            elif self == stock.STOCK.STOCK_MTL:
                return "mtl"
            elif self == stock.STOCK.STOCK_MTLS:
                return "mtls"
            elif self == stock.STOCK.STOCK_MTL_:
                return "mtl_"
            elif self == stock.STOCK.STOCK_MTN:
                return "mtn"
            elif self == stock.STOCK.STOCK_MTNB:
                return "mtnb"
            elif self == stock.STOCK.STOCK_MTOR:
                return "mtor"
            elif self == stock.STOCK.STOCK_MTP:
                return "mtp"
            elif self == stock.STOCK.STOCK_MTR:
                return "mtr"
            elif self == stock.STOCK.STOCK_MTRN:
                return "mtrn"
            elif self == stock.STOCK.STOCK_MTRX:
                return "mtrx"
            elif self == stock.STOCK.STOCK_MTSC:
                return "mtsc"
            elif self == stock.STOCK.STOCK_MTSI:
                return "mtsi"
            elif self == stock.STOCK.STOCK_MTSL:
                return "mtsl"
            elif self == stock.STOCK.STOCK_MTT:
                return "mtt"
            elif self == stock.STOCK.STOCK_MTU:
                return "mtu"
            elif self == stock.STOCK.STOCK_MTW:
                return "mtw"
            elif self == stock.STOCK.STOCK_MTX:
                return "mtx"
            elif self == stock.STOCK.STOCK_MTZ:
                return "mtz"
            elif self == stock.STOCK.STOCK_MU:
                return "mu"
            elif self == stock.STOCK.STOCK_MUA:
                return "mua"
            elif self == stock.STOCK.STOCK_MUC:
                return "muc"
            elif self == stock.STOCK.STOCK_MUE:
                return "mue"
            elif self == stock.STOCK.STOCK_MUH:
                return "muh"
            elif self == stock.STOCK.STOCK_MUI:
                return "mui"
            elif self == stock.STOCK.STOCK_MUJ:
                return "muj"
            elif self == stock.STOCK.STOCK_MULE:
                return "mule"
            elif self == stock.STOCK.STOCK_MUR:
                return "mur"
            elif self == stock.STOCK.STOCK_MUS:
                return "mus"
            elif self == stock.STOCK.STOCK_MUSA:
                return "musa"
            elif self == stock.STOCK.STOCK_MUX:
                return "mux"
            elif self == stock.STOCK.STOCK_MVC:
                return "mvc"
            elif self == stock.STOCK.STOCK_MVCB:
                return "mvcb"
            elif self == stock.STOCK.STOCK_MVF:
                return "mvf"
            elif self == stock.STOCK.STOCK_MVIN:
                return "mvin"
            elif self == stock.STOCK.STOCK_MVIS:
                return "mvis"
            elif self == stock.STOCK.STOCK_MVO:
                return "mvo"
            elif self == stock.STOCK.STOCK_MVT:
                return "mvt"
            elif self == stock.STOCK.STOCK_MWA:
                return "mwa"
            elif self == stock.STOCK.STOCK_MX:
                return "mx"
            elif self == stock.STOCK.STOCK_MXC:
                return "mxc"
            elif self == stock.STOCK.STOCK_MXDU:
                return "mxdu"
            elif self == stock.STOCK.STOCK_MXE:
                return "mxe"
            elif self == stock.STOCK.STOCK_MXF:
                return "mxf"
            elif self == stock.STOCK.STOCK_MXIM:
                return "mxim"
            elif self == stock.STOCK.STOCK_MXL:
                return "mxl"
            elif self == stock.STOCK.STOCK_MXWL:
                return "mxwl"
            elif self == stock.STOCK.STOCK_MYC:
                return "myc"
            elif self == stock.STOCK.STOCK_MYD:
                return "myd"
            elif self == stock.STOCK.STOCK_MYE:
                return "mye"
            elif self == stock.STOCK.STOCK_MYF:
                return "myf"
            elif self == stock.STOCK.STOCK_MYGN:
                return "mygn"
            elif self == stock.STOCK.STOCK_MYI:
                return "myi"
            elif self == stock.STOCK.STOCK_MYJ:
                return "myj"
            elif self == stock.STOCK.STOCK_MYL:
                return "myl"
            elif self == stock.STOCK.STOCK_MYN:
                return "myn"
            elif self == stock.STOCK.STOCK_MYND:
                return "mynd"
            elif self == stock.STOCK.STOCK_MYNDW:
                return "myndw"
            elif self == stock.STOCK.STOCK_MYO:
                return "myo"
            elif self == stock.STOCK.STOCK_MYOK:
                return "myok"
            elif self == stock.STOCK.STOCK_MYOS:
                return "myos"
            elif self == stock.STOCK.STOCK_MYOV:
                return "myov"
            elif self == stock.STOCK.STOCK_MYRG:
                return "myrg"
            elif self == stock.STOCK.STOCK_MYSZ:
                return "mysz"
            elif self == stock.STOCK.STOCK_MZA:
                return "mza"
            elif self == stock.STOCK.STOCK_MZF:
                return "mzf"
            elif self == stock.STOCK.STOCK_MZOR:
                return "mzor"
            elif self == stock.STOCK.STOCK_NAC:
                return "nac"
            elif self == stock.STOCK.STOCK_NAD:
                return "nad"
            elif self == stock.STOCK.STOCK_NAII:
                return "naii"
            elif self == stock.STOCK.STOCK_NAIL:
                return "nail"
            elif self == stock.STOCK.STOCK_NAK:
                return "nak"
            elif self == stock.STOCK.STOCK_NAKD:
                return "nakd"
            elif self == stock.STOCK.STOCK_NAN:
                return "nan"
            elif self == stock.STOCK.STOCK_NANO:
                return "nano"
            elif self == stock.STOCK.STOCK_NANR:
                return "nanr"
            elif self == stock.STOCK.STOCK_NAO:
                return "nao"
            elif self == stock.STOCK.STOCK_NAOV:
                return "naov"
            elif self == stock.STOCK.STOCK_NAP:
                return "nap"
            elif self == stock.STOCK.STOCK_NAT:
                return "nat"
            elif self == stock.STOCK.STOCK_NATH:
                return "nath"
            elif self == stock.STOCK.STOCK_NATI:
                return "nati"
            elif self == stock.STOCK.STOCK_NATR:
                return "natr"
            elif self == stock.STOCK.STOCK_NAUH:
                return "nauh"
            elif self == stock.STOCK.STOCK_NAV:
                return "nav"
            elif self == stock.STOCK.STOCK_NAVB:
                return "navb"
            elif self == stock.STOCK.STOCK_NAVG:
                return "navg"
            elif self == stock.STOCK.STOCK_NAVI:
                return "navi"
            elif self == stock.STOCK.STOCK_NAV_D:
                return "nav_d"
            elif self == stock.STOCK.STOCK_NAZ:
                return "naz"
            elif self == stock.STOCK.STOCK_NBB:
                return "nbb"
            elif self == stock.STOCK.STOCK_NBD:
                return "nbd"
            elif self == stock.STOCK.STOCK_NBEV:
                return "nbev"
            elif self == stock.STOCK.STOCK_NBH:
                return "nbh"
            elif self == stock.STOCK.STOCK_NBHC:
                return "nbhc"
            elif self == stock.STOCK.STOCK_NBIX:
                return "nbix"
            elif self == stock.STOCK.STOCK_NBL:
                return "nbl"
            elif self == stock.STOCK.STOCK_NBLX:
                return "nblx"
            elif self == stock.STOCK.STOCK_NBN:
                return "nbn"
            elif self == stock.STOCK.STOCK_NBO:
                return "nbo"
            elif self == stock.STOCK.STOCK_NBR:
                return "nbr"
            elif self == stock.STOCK.STOCK_NBRV:
                return "nbrv"
            elif self == stock.STOCK.STOCK_NBTB:
                return "nbtb"
            elif self == stock.STOCK.STOCK_NBW:
                return "nbw"
            elif self == stock.STOCK.STOCK_NBY:
                return "nby"
            elif self == stock.STOCK.STOCK_NC:
                return "nc"
            elif self == stock.STOCK.STOCK_NCA:
                return "nca"
            elif self == stock.STOCK.STOCK_NCB:
                return "ncb"
            elif self == stock.STOCK.STOCK_NCBS:
                return "ncbs"
            elif self == stock.STOCK.STOCK_NCI:
                return "nci"
            elif self == stock.STOCK.STOCK_NCLH:
                return "nclh"
            elif self == stock.STOCK.STOCK_NCMI:
                return "ncmi"
            elif self == stock.STOCK.STOCK_NCNA:
                return "ncna"
            elif self == stock.STOCK.STOCK_NCOM:
                return "ncom"
            elif self == stock.STOCK.STOCK_NCR:
                return "ncr"
            elif self == stock.STOCK.STOCK_NCS:
                return "ncs"
            elif self == stock.STOCK.STOCK_NCSM:
                return "ncsm"
            elif self == stock.STOCK.STOCK_NCTY:
                return "ncty"
            elif self == stock.STOCK.STOCK_NCV:
                return "ncv"
            elif self == stock.STOCK.STOCK_NCZ:
                return "ncz"
            elif self == stock.STOCK.STOCK_NDAQ:
                return "ndaq"
            elif self == stock.STOCK.STOCK_NDLS:
                return "ndls"
            elif self == stock.STOCK.STOCK_NDP:
                return "ndp"
            elif self == stock.STOCK.STOCK_NDRA:
                return "ndra"
            elif self == stock.STOCK.STOCK_NDRAW:
                return "ndraw"
            elif self == stock.STOCK.STOCK_NDRM:
                return "ndrm"
            elif self == stock.STOCK.STOCK_NDRO:
                return "ndro"
            elif self == stock.STOCK.STOCK_NDSN:
                return "ndsn"
            elif self == stock.STOCK.STOCK_NE:
                return "ne"
            elif self == stock.STOCK.STOCK_NEA:
                return "nea"
            elif self == stock.STOCK.STOCK_NEE:
                return "nee"
            elif self == stock.STOCK.STOCK_NEE_C-CL:
                return "nee_c-cl"
            elif self == stock.STOCK.STOCK_NEE_C:
                return "nee_c"
            elif self == stock.STOCK.STOCK_NEE_G-CL:
                return "nee_g-cl"
            elif self == stock.STOCK.STOCK_NEE_H-CL:
                return "nee_h-cl"
            elif self == stock.STOCK.STOCK_NEE_I:
                return "nee_i"
            elif self == stock.STOCK.STOCK_NEE_J:
                return "nee_j"
            elif self == stock.STOCK.STOCK_NEE_K:
                return "nee_k"
            elif self == stock.STOCK.STOCK_NEE_Q:
                return "nee_q"
            elif self == stock.STOCK.STOCK_NEE_R:
                return "nee_r"
            elif self == stock.STOCK.STOCK_NEM:
                return "nem"
            elif self == stock.STOCK.STOCK_NEN:
                return "nen"
            elif self == stock.STOCK.STOCK_NEO:
                return "neo"
            elif self == stock.STOCK.STOCK_NEOG:
                return "neog"
            elif self == stock.STOCK.STOCK_NEON:
                return "neon"
            elif self == stock.STOCK.STOCK_NEOS:
                return "neos"
            elif self == stock.STOCK.STOCK_NEOT:
                return "neot"
            elif self == stock.STOCK.STOCK_NEP:
                return "nep"
            elif self == stock.STOCK.STOCK_NEPT:
                return "nept"
            elif self == stock.STOCK.STOCK_NERV:
                return "nerv"
            elif self == stock.STOCK.STOCK_NES:
                return "nes"
            elif self == stock.STOCK.STOCK_NESR:
                return "nesr"
            elif self == stock.STOCK.STOCK_NESRW:
                return "nesrw"
            elif self == stock.STOCK.STOCK_NETE:
                return "nete"
            elif self == stock.STOCK.STOCK_NETS:
                return "nets"
            elif self == stock.STOCK.STOCK_NEU:
                return "neu"
            elif self == stock.STOCK.STOCK_NEV:
                return "nev"
            elif self == stock.STOCK.STOCK_NEWA:
                return "newa"
            elif self == stock.STOCK.STOCK_NEWM:
                return "newm"
            elif self == stock.STOCK.STOCK_NEWR:
                return "newr"
            elif self == stock.STOCK.STOCK_NEWS:
                return "news"
            elif self == stock.STOCK.STOCK_NEWT:
                return "newt"
            elif self == stock.STOCK.STOCK_NEWTL:
                return "newtl"
            elif self == stock.STOCK.STOCK_NEWTZ:
                return "newtz"
            elif self == stock.STOCK.STOCK_NEXA:
                return "nexa"
            elif self == stock.STOCK.STOCK_NEXT:
                return "next"
            elif self == stock.STOCK.STOCK_NEXTW:
                return "nextw"
            elif self == stock.STOCK.STOCK_NFBK:
                return "nfbk"
            elif self == stock.STOCK.STOCK_NFEC:
                return "nfec"
            elif self == stock.STOCK.STOCK_NFG:
                return "nfg"
            elif self == stock.STOCK.STOCK_NFJ:
                return "nfj"
            elif self == stock.STOCK.STOCK_NFLT:
                return "nflt"
            elif self == stock.STOCK.STOCK_NFLX:
                return "nflx"
            elif self == stock.STOCK.STOCK_NFX:
                return "nfx"
            elif self == stock.STOCK.STOCK_NG:
                return "ng"
            elif self == stock.STOCK.STOCK_NGD:
                return "ngd"
            elif self == stock.STOCK.STOCK_NGG:
                return "ngg"
            elif self == stock.STOCK.STOCK_NGHC:
                return "nghc"
            elif self == stock.STOCK.STOCK_NGHCN:
                return "nghcn"
            elif self == stock.STOCK.STOCK_NGHCO:
                return "nghco"
            elif self == stock.STOCK.STOCK_NGHCP:
                return "nghcp"
            elif self == stock.STOCK.STOCK_NGHCZ:
                return "nghcz"
            elif self == stock.STOCK.STOCK_NGL:
                return "ngl"
            elif self == stock.STOCK.STOCK_NGLS_A:
                return "ngls_a"
            elif self == stock.STOCK.STOCK_NGL_B:
                return "ngl_b"
            elif self == stock.STOCK.STOCK_NGS:
                return "ngs"
            elif self == stock.STOCK.STOCK_NGVC:
                return "ngvc"
            elif self == stock.STOCK.STOCK_NGVT:
                return "ngvt"
            elif self == stock.STOCK.STOCK_NH:
                return "nh"
            elif self == stock.STOCK.STOCK_NHA:
                return "nha"
            elif self == stock.STOCK.STOCK_NHC:
                return "nhc"
            elif self == stock.STOCK.STOCK_NHF:
                return "nhf"
            elif self == stock.STOCK.STOCK_NHI:
                return "nhi"
            elif self == stock.STOCK.STOCK_NHLD:
                return "nhld"
            elif self == stock.STOCK.STOCK_NHLDW:
                return "nhldw"
            elif self == stock.STOCK.STOCK_NHS:
                return "nhs"
            elif self == stock.STOCK.STOCK_NHTC:
                return "nhtc"
            elif self == stock.STOCK.STOCK_NI:
                return "ni"
            elif self == stock.STOCK.STOCK_NICE:
                return "nice"
            elif self == stock.STOCK.STOCK_NICK:
                return "nick"
            elif self == stock.STOCK.STOCK_NID:
                return "nid"
            elif self == stock.STOCK.STOCK_NIE:
                return "nie"
            elif self == stock.STOCK.STOCK_NIHD:
                return "nihd"
            elif self == stock.STOCK.STOCK_NIM:
                return "nim"
            elif self == stock.STOCK.STOCK_NIQ:
                return "niq"
            elif self == stock.STOCK.STOCK_NITE:
                return "nite"
            elif self == stock.STOCK.STOCK_NJR:
                return "njr"
            elif self == stock.STOCK.STOCK_NJV:
                return "njv"
            elif self == stock.STOCK.STOCK_NK:
                return "nk"
            elif self == stock.STOCK.STOCK_NKE:
                return "nke"
            elif self == stock.STOCK.STOCK_NKG:
                return "nkg"
            elif self == stock.STOCK.STOCK_NKSH:
                return "nksh"
            elif self == stock.STOCK.STOCK_NKTR:
                return "nktr"
            elif self == stock.STOCK.STOCK_NKX:
                return "nkx"
            elif self == stock.STOCK.STOCK_NL:
                return "nl"
            elif self == stock.STOCK.STOCK_NLNK:
                return "nlnk"
            elif self == stock.STOCK.STOCK_NLS:
                return "nls"
            elif self == stock.STOCK.STOCK_NLSN:
                return "nlsn"
            elif self == stock.STOCK.STOCK_NLST:
                return "nlst"
            elif self == stock.STOCK.STOCK_NLY:
                return "nly"
            elif self == stock.STOCK.STOCK_NLY_C:
                return "nly_c"
            elif self == stock.STOCK.STOCK_NLY_D:
                return "nly_d"
            elif self == stock.STOCK.STOCK_NLY_E:
                return "nly_e"
            elif self == stock.STOCK.STOCK_NLY_F:
                return "nly_f"
            elif self == stock.STOCK.STOCK_NM:
                return "nm"
            elif self == stock.STOCK.STOCK_NMFC:
                return "nmfc"
            elif self == stock.STOCK.STOCK_NMI:
                return "nmi"
            elif self == stock.STOCK.STOCK_NMIH:
                return "nmih"
            elif self == stock.STOCK.STOCK_NMK_B:
                return "nmk_b"
            elif self == stock.STOCK.STOCK_NMK_C:
                return "nmk_c"
            elif self == stock.STOCK.STOCK_NML:
                return "nml"
            elif self == stock.STOCK.STOCK_NMM:
                return "nmm"
            elif self == stock.STOCK.STOCK_NMR:
                return "nmr"
            elif self == stock.STOCK.STOCK_NMRX:
                return "nmrx"
            elif self == stock.STOCK.STOCK_NMS:
                return "nms"
            elif self == stock.STOCK.STOCK_NMT:
                return "nmt"
            elif self == stock.STOCK.STOCK_NMY:
                return "nmy"
            elif self == stock.STOCK.STOCK_NMZ:
                return "nmz"
            elif self == stock.STOCK.STOCK_NM_G:
                return "nm_g"
            elif self == stock.STOCK.STOCK_NM_H:
                return "nm_h"
            elif self == stock.STOCK.STOCK_NNA:
                return "nna"
            elif self == stock.STOCK.STOCK_NNBR:
                return "nnbr"
            elif self == stock.STOCK.STOCK_NNC:
                return "nnc"
            elif self == stock.STOCK.STOCK_NNDM:
                return "nndm"
            elif self == stock.STOCK.STOCK_NNI:
                return "nni"
            elif self == stock.STOCK.STOCK_NNN:
                return "nnn"
            elif self == stock.STOCK.STOCK_NNN_E:
                return "nnn_e"
            elif self == stock.STOCK.STOCK_NNN_F:
                return "nnn_f"
            elif self == stock.STOCK.STOCK_NNVC:
                return "nnvc"
            elif self == stock.STOCK.STOCK_NNY:
                return "nny"
            elif self == stock.STOCK.STOCK_NOA:
                return "noa"
            elif self == stock.STOCK.STOCK_NOAH:
                return "noah"
            elif self == stock.STOCK.STOCK_NOC:
                return "noc"
            elif self == stock.STOCK.STOCK_NODK:
                return "nodk"
            elif self == stock.STOCK.STOCK_NOG:
                return "nog"
            elif self == stock.STOCK.STOCK_NOK:
                return "nok"
            elif self == stock.STOCK.STOCK_NOM:
                return "nom"
            elif self == stock.STOCK.STOCK_NOMD:
                return "nomd"
            elif self == stock.STOCK.STOCK_NOV:
                return "nov"
            elif self == stock.STOCK.STOCK_NOVN:
                return "novn"
            elif self == stock.STOCK.STOCK_NOVT:
                return "novt"
            elif self == stock.STOCK.STOCK_NOW:
                return "now"
            elif self == stock.STOCK.STOCK_NP:
                return "np"
            elif self == stock.STOCK.STOCK_NPK:
                return "npk"
            elif self == stock.STOCK.STOCK_NPN:
                return "npn"
            elif self == stock.STOCK.STOCK_NPO:
                return "npo"
            elif self == stock.STOCK.STOCK_NPTN:
                return "nptn"
            elif self == stock.STOCK.STOCK_NPV:
                return "npv"
            elif self == stock.STOCK.STOCK_NQ:
                return "nq"
            elif self == stock.STOCK.STOCK_NQP:
                return "nqp"
            elif self == stock.STOCK.STOCK_NR:
                return "nr"
            elif self == stock.STOCK.STOCK_NRCIA:
                return "nrcia"
            elif self == stock.STOCK.STOCK_NRCIB:
                return "nrcib"
            elif self == stock.STOCK.STOCK_NRE:
                return "nre"
            elif self == stock.STOCK.STOCK_NRG:
                return "nrg"
            elif self == stock.STOCK.STOCK_NRIM:
                return "nrim"
            elif self == stock.STOCK.STOCK_NRK:
                return "nrk"
            elif self == stock.STOCK.STOCK_NRO:
                return "nro"
            elif self == stock.STOCK.STOCK_NRP:
                return "nrp"
            elif self == stock.STOCK.STOCK_NRT:
                return "nrt"
            elif self == stock.STOCK.STOCK_NRZ:
                return "nrz"
            elif self == stock.STOCK.STOCK_NS:
                return "ns"
            elif self == stock.STOCK.STOCK_NSA:
                return "nsa"
            elif self == stock.STOCK.STOCK_NSA_A:
                return "nsa_a"
            elif self == stock.STOCK.STOCK_NSC:
                return "nsc"
            elif self == stock.STOCK.STOCK_NSEC:
                return "nsec"
            elif self == stock.STOCK.STOCK_NSH:
                return "nsh"
            elif self == stock.STOCK.STOCK_NSIT:
                return "nsit"
            elif self == stock.STOCK.STOCK_NSL:
                return "nsl"
            elif self == stock.STOCK.STOCK_NSM:
                return "nsm"
            elif self == stock.STOCK.STOCK_NSP:
                return "nsp"
            elif self == stock.STOCK.STOCK_NSPR-WS-B:
                return "nspr-ws-b"
            elif self == stock.STOCK.STOCK_NSPR-WS:
                return "nspr-ws"
            elif self == stock.STOCK.STOCK_NSPR:
                return "nspr"
            elif self == stock.STOCK.STOCK_NSS:
                return "nss"
            elif self == stock.STOCK.STOCK_NSSC:
                return "nssc"
            elif self == stock.STOCK.STOCK_NSTG:
                return "nstg"
            elif self == stock.STOCK.STOCK_NSU:
                return "nsu"
            elif self == stock.STOCK.STOCK_NSYS:
                return "nsys"
            elif self == stock.STOCK.STOCK_NS_A:
                return "ns_a"
            elif self == stock.STOCK.STOCK_NS_B:
                return "ns_b"
            elif self == stock.STOCK.STOCK_NTAP:
                return "ntap"
            elif self == stock.STOCK.STOCK_NTB:
                return "ntb"
            elif self == stock.STOCK.STOCK_NTC:
                return "ntc"
            elif self == stock.STOCK.STOCK_NTCT:
                return "ntct"
            elif self == stock.STOCK.STOCK_NTEC:
                return "ntec"
            elif self == stock.STOCK.STOCK_NTES:
                return "ntes"
            elif self == stock.STOCK.STOCK_NTG:
                return "ntg"
            elif self == stock.STOCK.STOCK_NTGR:
                return "ntgr"
            elif self == stock.STOCK.STOCK_NTIC:
                return "ntic"
            elif self == stock.STOCK.STOCK_NTIP:
                return "ntip"
            elif self == stock.STOCK.STOCK_NTL:
                return "ntl"
            elif self == stock.STOCK.STOCK_NTLA:
                return "ntla"
            elif self == stock.STOCK.STOCK_NTN:
                return "ntn"
            elif self == stock.STOCK.STOCK_NTNX:
                return "ntnx"
            elif self == stock.STOCK.STOCK_NTP:
                return "ntp"
            elif self == stock.STOCK.STOCK_NTRA:
                return "ntra"
            elif self == stock.STOCK.STOCK_NTRI:
                return "ntri"
            elif self == stock.STOCK.STOCK_NTRP:
                return "ntrp"
            elif self == stock.STOCK.STOCK_NTRS:
                return "ntrs"
            elif self == stock.STOCK.STOCK_NTRSP:
                return "ntrsp"
            elif self == stock.STOCK.STOCK_NTWK:
                return "ntwk"
            elif self == stock.STOCK.STOCK_NTX:
                return "ntx"
            elif self == stock.STOCK.STOCK_NTZ:
                return "ntz"
            elif self == stock.STOCK.STOCK_NUAG:
                return "nuag"
            elif self == stock.STOCK.STOCK_NUAN:
                return "nuan"
            elif self == stock.STOCK.STOCK_NUBD:
                return "nubd"
            elif self == stock.STOCK.STOCK_NUDM:
                return "nudm"
            elif self == stock.STOCK.STOCK_NUE:
                return "nue"
            elif self == stock.STOCK.STOCK_NUEM:
                return "nuem"
            elif self == stock.STOCK.STOCK_NULG:
                return "nulg"
            elif self == stock.STOCK.STOCK_NULV:
                return "nulv"
            elif self == stock.STOCK.STOCK_NUM:
                return "num"
            elif self == stock.STOCK.STOCK_NUMG:
                return "numg"
            elif self == stock.STOCK.STOCK_NUMV:
                return "numv"
            elif self == stock.STOCK.STOCK_NUO:
                return "nuo"
            elif self == stock.STOCK.STOCK_NURE:
                return "nure"
            elif self == stock.STOCK.STOCK_NURO:
                return "nuro"
            elif self == stock.STOCK.STOCK_NUROW:
                return "nurow"
            elif self == stock.STOCK.STOCK_NUS:
                return "nus"
            elif self == stock.STOCK.STOCK_NUSA:
                return "nusa"
            elif self == stock.STOCK.STOCK_NUSC:
                return "nusc"
            elif self == stock.STOCK.STOCK_NUV:
                return "nuv"
            elif self == stock.STOCK.STOCK_NUVA:
                return "nuva"
            elif self == stock.STOCK.STOCK_NUW:
                return "nuw"
            elif self == stock.STOCK.STOCK_NVAX:
                return "nvax"
            elif self == stock.STOCK.STOCK_NVCN:
                return "nvcn"
            elif self == stock.STOCK.STOCK_NVCR:
                return "nvcr"
            elif self == stock.STOCK.STOCK_NVDA:
                return "nvda"
            elif self == stock.STOCK.STOCK_NVEC:
                return "nvec"
            elif self == stock.STOCK.STOCK_NVEE:
                return "nvee"
            elif self == stock.STOCK.STOCK_NVFY:
                return "nvfy"
            elif self == stock.STOCK.STOCK_NVG:
                return "nvg"
            elif self == stock.STOCK.STOCK_NVGN:
                return "nvgn"
            elif self == stock.STOCK.STOCK_NVGS:
                return "nvgs"
            elif self == stock.STOCK.STOCK_NVIV:
                return "nviv"
            elif self == stock.STOCK.STOCK_NVLN:
                return "nvln"
            elif self == stock.STOCK.STOCK_NVMI:
                return "nvmi"
            elif self == stock.STOCK.STOCK_NVO:
                return "nvo"
            elif self == stock.STOCK.STOCK_NVR:
                return "nvr"
            elif self == stock.STOCK.STOCK_NVRO:
                return "nvro"
            elif self == stock.STOCK.STOCK_NVS:
                return "nvs"
            elif self == stock.STOCK.STOCK_NVTA:
                return "nvta"
            elif self == stock.STOCK.STOCK_NVTR:
                return "nvtr"
            elif self == stock.STOCK.STOCK_NVUS:
                return "nvus"
            elif self == stock.STOCK.STOCK_NWBI:
                return "nwbi"
            elif self == stock.STOCK.STOCK_NWE:
                return "nwe"
            elif self == stock.STOCK.STOCK_NWFL:
                return "nwfl"
            elif self == stock.STOCK.STOCK_NWHM:
                return "nwhm"
            elif self == stock.STOCK.STOCK_NWL:
                return "nwl"
            elif self == stock.STOCK.STOCK_NWLI:
                return "nwli"
            elif self == stock.STOCK.STOCK_NWN:
                return "nwn"
            elif self == stock.STOCK.STOCK_NWPX:
                return "nwpx"
            elif self == stock.STOCK.STOCK_NWS:
                return "nws"
            elif self == stock.STOCK.STOCK_NWSA:
                return "nwsa"
            elif self == stock.STOCK.STOCK_NWY:
                return "nwy"
            elif self == stock.STOCK.STOCK_NW_C-CL:
                return "nw_c-cl"
            elif self == stock.STOCK.STOCK_NX:
                return "nx"
            elif self == stock.STOCK.STOCK_NXC:
                return "nxc"
            elif self == stock.STOCK.STOCK_NXE:
                return "nxe"
            elif self == stock.STOCK.STOCK_NXEO:
                return "nxeo"
            elif self == stock.STOCK.STOCK_NXEOU:
                return "nxeou"
            elif self == stock.STOCK.STOCK_NXEOW:
                return "nxeow"
            elif self == stock.STOCK.STOCK_NXJ:
                return "nxj"
            elif self == stock.STOCK.STOCK_NXN:
                return "nxn"
            elif self == stock.STOCK.STOCK_NXP:
                return "nxp"
            elif self == stock.STOCK.STOCK_NXPI:
                return "nxpi"
            elif self == stock.STOCK.STOCK_NXQ:
                return "nxq"
            elif self == stock.STOCK.STOCK_NXR:
                return "nxr"
            elif self == stock.STOCK.STOCK_NXRT:
                return "nxrt"
            elif self == stock.STOCK.STOCK_NXST:
                return "nxst"
            elif self == stock.STOCK.STOCK_NXTD:
                return "nxtd"
            elif self == stock.STOCK.STOCK_NXTDW:
                return "nxtdw"
            elif self == stock.STOCK.STOCK_NXTM:
                return "nxtm"
            elif self == stock.STOCK.STOCK_NYCB:
                return "nycb"
            elif self == stock.STOCK.STOCK_NYCB_A:
                return "nycb_a"
            elif self == stock.STOCK.STOCK_NYCB_U:
                return "nycb_u"
            elif self == stock.STOCK.STOCK_NYH:
                return "nyh"
            elif self == stock.STOCK.STOCK_NYLD-A:
                return "nyld-a"
            elif self == stock.STOCK.STOCK_NYLD:
                return "nyld"
            elif self == stock.STOCK.STOCK_NYMT:
                return "nymt"
            elif self == stock.STOCK.STOCK_NYMTN:
                return "nymtn"
            elif self == stock.STOCK.STOCK_NYMTO:
                return "nymto"
            elif self == stock.STOCK.STOCK_NYMTP:
                return "nymtp"
            elif self == stock.STOCK.STOCK_NYMX:
                return "nymx"
            elif self == stock.STOCK.STOCK_NYNY:
                return "nyny"
            elif self == stock.STOCK.STOCK_NYRT:
                return "nyrt"
            elif self == stock.STOCK.STOCK_NYT:
                return "nyt"
            elif self == stock.STOCK.STOCK_NYV:
                return "nyv"
            elif self == stock.STOCK.STOCK_NZF:
                return "nzf"
            elif self == stock.STOCK.STOCK_O:
                return "o"
            elif self == stock.STOCK.STOCK_OA:
                return "oa"
            elif self == stock.STOCK.STOCK_OACQ:
                return "oacq"
            elif self == stock.STOCK.STOCK_OACQR:
                return "oacqr"
            elif self == stock.STOCK.STOCK_OACQU:
                return "oacqu"
            elif self == stock.STOCK.STOCK_OACQW:
                return "oacqw"
            elif self == stock.STOCK.STOCK_OAK:
                return "oak"
            elif self == stock.STOCK.STOCK_OAKS:
                return "oaks"
            elif self == stock.STOCK.STOCK_OAKS_A:
                return "oaks_a"
            elif self == stock.STOCK.STOCK_OAPH:
                return "oaph"
            elif self == stock.STOCK.STOCK_OAS:
                return "oas"
            elif self == stock.STOCK.STOCK_OASI:
                return "oasi"
            elif self == stock.STOCK.STOCK_OASM:
                return "oasm"
            elif self == stock.STOCK.STOCK_OBAS:
                return "obas"
            elif self == stock.STOCK.STOCK_OBCI:
                return "obci"
            elif self == stock.STOCK.STOCK_OBE:
                return "obe"
            elif self == stock.STOCK.STOCK_OBLN:
                return "obln"
            elif self == stock.STOCK.STOCK_OBOR:
                return "obor"
            elif self == stock.STOCK.STOCK_OBSV:
                return "obsv"
            elif self == stock.STOCK.STOCK_OC:
                return "oc"
            elif self == stock.STOCK.STOCK_OCC:
                return "occ"
            elif self == stock.STOCK.STOCK_OCFC:
                return "ocfc"
            elif self == stock.STOCK.STOCK_OCIO:
                return "ocio"
            elif self == stock.STOCK.STOCK_OCIP:
                return "ocip"
            elif self == stock.STOCK.STOCK_OCLR:
                return "oclr"
            elif self == stock.STOCK.STOCK_OCN:
                return "ocn"
            elif self == stock.STOCK.STOCK_OCRX:
                return "ocrx"
            elif self == stock.STOCK.STOCK_OCSI:
                return "ocsi"
            elif self == stock.STOCK.STOCK_OCSL:
                return "ocsl"
            elif self == stock.STOCK.STOCK_OCSLL:
                return "ocsll"
            elif self == stock.STOCK.STOCK_OCUL:
                return "ocul"
            elif self == stock.STOCK.STOCK_OCX:
                return "ocx"
            elif self == stock.STOCK.STOCK_ODC:
                return "odc"
            elif self == stock.STOCK.STOCK_ODFL:
                return "odfl"
            elif self == stock.STOCK.STOCK_ODP:
                return "odp"
            elif self == stock.STOCK.STOCK_OEC:
                return "oec"
            elif self == stock.STOCK.STOCK_OESX:
                return "oesx"
            elif self == stock.STOCK.STOCK_OEUH:
                return "oeuh"
            elif self == stock.STOCK.STOCK_OEUR:
                return "oeur"
            elif self == stock.STOCK.STOCK_OEW:
                return "oew"
            elif self == stock.STOCK.STOCK_OFC:
                return "ofc"
            elif self == stock.STOCK.STOCK_OFED:
                return "ofed"
            elif self == stock.STOCK.STOCK_OFG:
                return "ofg"
            elif self == stock.STOCK.STOCK_OFG_A:
                return "ofg_a"
            elif self == stock.STOCK.STOCK_OFG_B:
                return "ofg_b"
            elif self == stock.STOCK.STOCK_OFG_D:
                return "ofg_d"
            elif self == stock.STOCK.STOCK_OFIX:
                return "ofix"
            elif self == stock.STOCK.STOCK_OFLX:
                return "oflx"
            elif self == stock.STOCK.STOCK_OFS:
                return "ofs"
            elif self == stock.STOCK.STOCK_OGCP:
                return "ogcp"
            elif self == stock.STOCK.STOCK_OGE:
                return "oge"
            elif self == stock.STOCK.STOCK_OGEN:
                return "ogen"
            elif self == stock.STOCK.STOCK_OGS:
                return "ogs"
            elif self == stock.STOCK.STOCK_OHAI:
                return "ohai"
            elif self == stock.STOCK.STOCK_OHGI:
                return "ohgi"
            elif self == stock.STOCK.STOCK_OHI:
                return "ohi"
            elif self == stock.STOCK.STOCK_OHRP:
                return "ohrp"
            elif self == stock.STOCK.STOCK_OI:
                return "oi"
            elif self == stock.STOCK.STOCK_OIA:
                return "oia"
            elif self == stock.STOCK.STOCK_OIBR-C:
                return "oibr-c"
            elif self == stock.STOCK.STOCK_OII:
                return "oii"
            elif self == stock.STOCK.STOCK_OIIL:
                return "oiil"
            elif self == stock.STOCK.STOCK_OIIM:
                return "oiim"
            elif self == stock.STOCK.STOCK_OILB:
                return "oilb"
            elif self == stock.STOCK.STOCK_OILD:
                return "oild"
            elif self == stock.STOCK.STOCK_OILK:
                return "oilk"
            elif self == stock.STOCK.STOCK_OILU:
                return "oilu"
            elif self == stock.STOCK.STOCK_OILX:
                return "oilx"
            elif self == stock.STOCK.STOCK_OIS:
                return "ois"
            elif self == stock.STOCK.STOCK_OKE:
                return "oke"
            elif self == stock.STOCK.STOCK_OKSB:
                return "oksb"
            elif self == stock.STOCK.STOCK_OKTA:
                return "okta"
            elif self == stock.STOCK.STOCK_OLBK:
                return "olbk"
            elif self == stock.STOCK.STOCK_OLD:
                return "old"
            elif self == stock.STOCK.STOCK_OLED:
                return "oled"
            elif self == stock.STOCK.STOCK_OLLI:
                return "olli"
            elif self == stock.STOCK.STOCK_OLN:
                return "oln"
            elif self == stock.STOCK.STOCK_OLP:
                return "olp"
            elif self == stock.STOCK.STOCK_OMAA:
                return "omaa"
            elif self == stock.STOCK.STOCK_OMAB:
                return "omab"
            elif self == stock.STOCK.STOCK_OMAM:
                return "omam"
            elif self == stock.STOCK.STOCK_OMC:
                return "omc"
            elif self == stock.STOCK.STOCK_OMCL:
                return "omcl"
            elif self == stock.STOCK.STOCK_OME:
                return "ome"
            elif self == stock.STOCK.STOCK_OMED:
                return "omed"
            elif self == stock.STOCK.STOCK_OMER:
                return "omer"
            elif self == stock.STOCK.STOCK_OMEX:
                return "omex"
            elif self == stock.STOCK.STOCK_OMF:
                return "omf"
            elif self == stock.STOCK.STOCK_OMFL:
                return "omfl"
            elif self == stock.STOCK.STOCK_OMFS:
                return "omfs"
            elif self == stock.STOCK.STOCK_OMI:
                return "omi"
            elif self == stock.STOCK.STOCK_OMN:
                return "omn"
            elif self == stock.STOCK.STOCK_OMNT:
                return "omnt"
            elif self == stock.STOCK.STOCK_OMP:
                return "omp"
            elif self == stock.STOCK.STOCK_ON:
                return "on"
            elif self == stock.STOCK.STOCK_ONB:
                return "onb"
            elif self == stock.STOCK.STOCK_ONCE:
                return "once"
            elif self == stock.STOCK.STOCK_ONCS:
                return "oncs"
            elif self == stock.STOCK.STOCK_ONDK:
                return "ondk"
            elif self == stock.STOCK.STOCK_ONEO:
                return "oneo"
            elif self == stock.STOCK.STOCK_ONEV:
                return "onev"
            elif self == stock.STOCK.STOCK_ONEY:
                return "oney"
            elif self == stock.STOCK.STOCK_ONP:
                return "onp"
            elif self == stock.STOCK.STOCK_ONS:
                return "ons"
            elif self == stock.STOCK.STOCK_ONSIW:
                return "onsiw"
            elif self == stock.STOCK.STOCK_ONSIZ:
                return "onsiz"
            elif self == stock.STOCK.STOCK_ONTL:
                return "ontl"
            elif self == stock.STOCK.STOCK_ONTX:
                return "ontx"
            elif self == stock.STOCK.STOCK_ONTXW:
                return "ontxw"
            elif self == stock.STOCK.STOCK_ONVI:
                return "onvi"
            elif self == stock.STOCK.STOCK_ONVO:
                return "onvo"
            elif self == stock.STOCK.STOCK_OOMA:
                return "ooma"
            elif self == stock.STOCK.STOCK_OPB:
                return "opb"
            elif self == stock.STOCK.STOCK_OPGN:
                return "opgn"
            elif self == stock.STOCK.STOCK_OPGNW:
                return "opgnw"
            elif self == stock.STOCK.STOCK_OPHC:
                return "ophc"
            elif self == stock.STOCK.STOCK_OPHT:
                return "opht"
            elif self == stock.STOCK.STOCK_OPK:
                return "opk"
            elif self == stock.STOCK.STOCK_OPNT:
                return "opnt"
            elif self == stock.STOCK.STOCK_OPOF:
                return "opof"
            elif self == stock.STOCK.STOCK_OPP:
                return "opp"
            elif self == stock.STOCK.STOCK_OPTN:
                return "optn"
            elif self == stock.STOCK.STOCK_OPTT:
                return "optt"
            elif self == stock.STOCK.STOCK_OPY:
                return "opy"
            elif self == stock.STOCK.STOCK_OR:
                return "or"
            elif self == stock.STOCK.STOCK_ORA:
                return "ora"
            elif self == stock.STOCK.STOCK_ORAN:
                return "oran"
            elif self == stock.STOCK.STOCK_ORBC:
                return "orbc"
            elif self == stock.STOCK.STOCK_ORBK:
                return "orbk"
            elif self == stock.STOCK.STOCK_ORC:
                return "orc"
            elif self == stock.STOCK.STOCK_ORCL:
                return "orcl"
            elif self == stock.STOCK.STOCK_OREX:
                return "orex"
            elif self == stock.STOCK.STOCK_ORG:
                return "org"
            elif self == stock.STOCK.STOCK_ORI:
                return "ori"
            elif self == stock.STOCK.STOCK_ORIG:
                return "orig"
            elif self == stock.STOCK.STOCK_ORIT:
                return "orit"
            elif self == stock.STOCK.STOCK_ORLY:
                return "orly"
            elif self == stock.STOCK.STOCK_ORM:
                return "orm"
            elif self == stock.STOCK.STOCK_ORMP:
                return "ormp"
            elif self == stock.STOCK.STOCK_ORN:
                return "orn"
            elif self == stock.STOCK.STOCK_ORPN:
                return "orpn"
            elif self == stock.STOCK.STOCK_ORRF:
                return "orrf"
            elif self == stock.STOCK.STOCK_OSB:
                return "osb"
            elif self == stock.STOCK.STOCK_OSBC:
                return "osbc"
            elif self == stock.STOCK.STOCK_OSBCP:
                return "osbcp"
            elif self == stock.STOCK.STOCK_OSG:
                return "osg"
            elif self == stock.STOCK.STOCK_OSIS:
                return "osis"
            elif self == stock.STOCK.STOCK_OSK:
                return "osk"
            elif self == stock.STOCK.STOCK_OSLE:
                return "osle"
            elif self == stock.STOCK.STOCK_OSN:
                return "osn"
            elif self == stock.STOCK.STOCK_OSPR:
                return "ospr"
            elif self == stock.STOCK.STOCK_OSPRU:
                return "ospru"
            elif self == stock.STOCK.STOCK_OSPRW:
                return "osprw"
            elif self == stock.STOCK.STOCK_OSTK:
                return "ostk"
            elif self == stock.STOCK.STOCK_OSUR:
                return "osur"
            elif self == stock.STOCK.STOCK_OTEL:
                return "otel"
            elif self == stock.STOCK.STOCK_OTEX:
                return "otex"
            elif self == stock.STOCK.STOCK_OTG:
                return "otg"
            elif self == stock.STOCK.STOCK_OTIC:
                return "otic"
            elif self == stock.STOCK.STOCK_OTIV:
                return "otiv"
            elif self == stock.STOCK.STOCK_OTTR:
                return "ottr"
            elif self == stock.STOCK.STOCK_OTTW:
                return "ottw"
            elif self == stock.STOCK.STOCK_OUSA:
                return "ousa"
            elif self == stock.STOCK.STOCK_OUSM:
                return "ousm"
            elif self == stock.STOCK.STOCK_OUT:
                return "out"
            elif self == stock.STOCK.STOCK_OVAS:
                return "ovas"
            elif self == stock.STOCK.STOCK_OVBC:
                return "ovbc"
            elif self == stock.STOCK.STOCK_OVID:
                return "ovid"
            elif self == stock.STOCK.STOCK_OVLY:
                return "ovly"
            elif self == stock.STOCK.STOCK_OXBR:
                return "oxbr"
            elif self == stock.STOCK.STOCK_OXBRW:
                return "oxbrw"
            elif self == stock.STOCK.STOCK_OXFD:
                return "oxfd"
            elif self == stock.STOCK.STOCK_OXLC:
                return "oxlc"
            elif self == stock.STOCK.STOCK_OXLCM:
                return "oxlcm"
            elif self == stock.STOCK.STOCK_OXLCO:
                return "oxlco"
            elif self == stock.STOCK.STOCK_OXM:
                return "oxm"
            elif self == stock.STOCK.STOCK_OXY:
                return "oxy"
            elif self == stock.STOCK.STOCK_OZM:
                return "ozm"
            elif self == stock.STOCK.STOCK_OZRK:
                return "ozrk"
            elif self == stock.STOCK.STOCK_P:
                return "p"
            elif self == stock.STOCK.STOCK_PAA:
                return "paa"
            elif self == stock.STOCK.STOCK_PAAS:
                return "paas"
            elif self == stock.STOCK.STOCK_PAC:
                return "pac"
            elif self == stock.STOCK.STOCK_PACB:
                return "pacb"
            elif self == stock.STOCK.STOCK_PACW:
                return "pacw"
            elif self == stock.STOCK.STOCK_PAG:
                return "pag"
            elif self == stock.STOCK.STOCK_PAGP:
                return "pagp"
            elif self == stock.STOCK.STOCK_PAH:
                return "pah"
            elif self == stock.STOCK.STOCK_PAHC:
                return "pahc"
            elif self == stock.STOCK.STOCK_PAI:
                return "pai"
            elif self == stock.STOCK.STOCK_PAM:
                return "pam"
            elif self == stock.STOCK.STOCK_PANL:
                return "panl"
            elif self == stock.STOCK.STOCK_PANW:
                return "panw"
            elif self == stock.STOCK.STOCK_PAR:
                return "par"
            elif self == stock.STOCK.STOCK_PARR:
                return "parr"
            elif self == stock.STOCK.STOCK_PATI:
                return "pati"
            elif self == stock.STOCK.STOCK_PATK:
                return "patk"
            elif self == stock.STOCK.STOCK_PAVE:
                return "pave"
            elif self == stock.STOCK.STOCK_PAVM:
                return "pavm"
            elif self == stock.STOCK.STOCK_PAVMW:
                return "pavmw"
            elif self == stock.STOCK.STOCK_PAY:
                return "pay"
            elif self == stock.STOCK.STOCK_PAYC:
                return "payc"
            elif self == stock.STOCK.STOCK_PAYX:
                return "payx"
            elif self == stock.STOCK.STOCK_PB:
                return "pb"
            elif self == stock.STOCK.STOCK_PBA:
                return "pba"
            elif self == stock.STOCK.STOCK_PBB:
                return "pbb"
            elif self == stock.STOCK.STOCK_PBBI:
                return "pbbi"
            elif self == stock.STOCK.STOCK_PBCT:
                return "pbct"
            elif self == stock.STOCK.STOCK_PBCTP:
                return "pbctp"
            elif self == stock.STOCK.STOCK_PBDM:
                return "pbdm"
            elif self == stock.STOCK.STOCK_PBEE:
                return "pbee"
            elif self == stock.STOCK.STOCK_PBF:
                return "pbf"
            elif self == stock.STOCK.STOCK_PBFX:
                return "pbfx"
            elif self == stock.STOCK.STOCK_PBH:
                return "pbh"
            elif self == stock.STOCK.STOCK_PBHC:
                return "pbhc"
            elif self == stock.STOCK.STOCK_PBI:
                return "pbi"
            elif self == stock.STOCK.STOCK_PBIB:
                return "pbib"
            elif self == stock.STOCK.STOCK_PBIO:
                return "pbio"
            elif self == stock.STOCK.STOCK_PBIP:
                return "pbip"
            elif self == stock.STOCK.STOCK_PBI_B:
                return "pbi_b"
            elif self == stock.STOCK.STOCK_PBMD:
                return "pbmd"
            elif self == stock.STOCK.STOCK_PBNC:
                return "pbnc"
            elif self == stock.STOCK.STOCK_PBND:
                return "pbnd"
            elif self == stock.STOCK.STOCK_PBPB:
                return "pbpb"
            elif self == stock.STOCK.STOCK_PBR-A:
                return "pbr-a"
            elif self == stock.STOCK.STOCK_PBR:
                return "pbr"
            elif self == stock.STOCK.STOCK_PBSK:
                return "pbsk"
            elif self == stock.STOCK.STOCK_PBSM:
                return "pbsm"
            elif self == stock.STOCK.STOCK_PBT:
                return "pbt"
            elif self == stock.STOCK.STOCK_PBUS:
                return "pbus"
            elif self == stock.STOCK.STOCK_PBYI:
                return "pbyi"
            elif self == stock.STOCK.STOCK_PCAR:
                return "pcar"
            elif self == stock.STOCK.STOCK_PCBK:
                return "pcbk"
            elif self == stock.STOCK.STOCK_PCF:
                return "pcf"
            elif self == stock.STOCK.STOCK_PCG:
                return "pcg"
            elif self == stock.STOCK.STOCK_PCG_A:
                return "pcg_a"
            elif self == stock.STOCK.STOCK_PCG_B:
                return "pcg_b"
            elif self == stock.STOCK.STOCK_PCG_C:
                return "pcg_c"
            elif self == stock.STOCK.STOCK_PCG_D:
                return "pcg_d"
            elif self == stock.STOCK.STOCK_PCG_E:
                return "pcg_e"
            elif self == stock.STOCK.STOCK_PCG_G:
                return "pcg_g"
            elif self == stock.STOCK.STOCK_PCG_H:
                return "pcg_h"
            elif self == stock.STOCK.STOCK_PCG_I:
                return "pcg_i"
            elif self == stock.STOCK.STOCK_PCH:
                return "pch"
            elif self == stock.STOCK.STOCK_PCI:
                return "pci"
            elif self == stock.STOCK.STOCK_PCK:
                return "pck"
            elif self == stock.STOCK.STOCK_PCLN:
                return "pcln"
            elif self == stock.STOCK.STOCK_PCM:
                return "pcm"
            elif self == stock.STOCK.STOCK_PCMI:
                return "pcmi"
            elif self == stock.STOCK.STOCK_PCN:
                return "pcn"
            elif self == stock.STOCK.STOCK_PCO:
                return "pco"
            elif self == stock.STOCK.STOCK_PCOM:
                return "pcom"
            elif self == stock.STOCK.STOCK_PCQ:
                return "pcq"
            elif self == stock.STOCK.STOCK_PCRX:
                return "pcrx"
            elif self == stock.STOCK.STOCK_PCSB:
                return "pcsb"
            elif self == stock.STOCK.STOCK_PCTI:
                return "pcti"
            elif self == stock.STOCK.STOCK_PCTY:
                return "pcty"
            elif self == stock.STOCK.STOCK_PCYG:
                return "pcyg"
            elif self == stock.STOCK.STOCK_PCYO:
                return "pcyo"
            elif self == stock.STOCK.STOCK_PDCE:
                return "pdce"
            elif self == stock.STOCK.STOCK_PDCO:
                return "pdco"
            elif self == stock.STOCK.STOCK_PDEX:
                return "pdex"
            elif self == stock.STOCK.STOCK_PDFS:
                return "pdfs"
            elif self == stock.STOCK.STOCK_PDI:
                return "pdi"
            elif self == stock.STOCK.STOCK_PDLB:
                return "pdlb"
            elif self == stock.STOCK.STOCK_PDLI:
                return "pdli"
            elif self == stock.STOCK.STOCK_PDM:
                return "pdm"
            elif self == stock.STOCK.STOCK_PDP:
                return "pdp"
            elif self == stock.STOCK.STOCK_PDS:
                return "pds"
            elif self == stock.STOCK.STOCK_PDT:
                return "pdt"
            elif self == stock.STOCK.STOCK_PDVW:
                return "pdvw"
            elif self == stock.STOCK.STOCK_PE:
                return "pe"
            elif self == stock.STOCK.STOCK_PEB:
                return "peb"
            elif self == stock.STOCK.STOCK_PEBK:
                return "pebk"
            elif self == stock.STOCK.STOCK_PEBO:
                return "pebo"
            elif self == stock.STOCK.STOCK_PEB_C:
                return "peb_c"
            elif self == stock.STOCK.STOCK_PEB_D:
                return "peb_d"
            elif self == stock.STOCK.STOCK_PED:
                return "ped"
            elif self == stock.STOCK.STOCK_PEG:
                return "peg"
            elif self == stock.STOCK.STOCK_PEGA:
                return "pega"
            elif self == stock.STOCK.STOCK_PEGI:
                return "pegi"
            elif self == stock.STOCK.STOCK_PEI:
                return "pei"
            elif self == stock.STOCK.STOCK_PEIX:
                return "peix"
            elif self == stock.STOCK.STOCK_PEI_B:
                return "pei_b"
            elif self == stock.STOCK.STOCK_PEI_C:
                return "pei_c"
            elif self == stock.STOCK.STOCK_PEI_D:
                return "pei_d"
            elif self == stock.STOCK.STOCK_PEN:
                return "pen"
            elif self == stock.STOCK.STOCK_PENN:
                return "penn"
            elif self == stock.STOCK.STOCK_PEO:
                return "peo"
            elif self == stock.STOCK.STOCK_PEP:
                return "pep"
            elif self == stock.STOCK.STOCK_PER:
                return "per"
            elif self == stock.STOCK.STOCK_PERI:
                return "peri"
            elif self == stock.STOCK.STOCK_PERY:
                return "pery"
            elif self == stock.STOCK.STOCK_PES:
                return "pes"
            elif self == stock.STOCK.STOCK_PESI:
                return "pesi"
            elif self == stock.STOCK.STOCK_PETQ:
                return "petq"
            elif self == stock.STOCK.STOCK_PETS:
                return "pets"
            elif self == stock.STOCK.STOCK_PETX:
                return "petx"
            elif self == stock.STOCK.STOCK_PETZ:
                return "petz"
            elif self == stock.STOCK.STOCK_PF:
                return "pf"
            elif self == stock.STOCK.STOCK_PFBC:
                return "pfbc"
            elif self == stock.STOCK.STOCK_PFBI:
                return "pfbi"
            elif self == stock.STOCK.STOCK_PFBX:
                return "pfbx"
            elif self == stock.STOCK.STOCK_PFD:
                return "pfd"
            elif self == stock.STOCK.STOCK_PFE:
                return "pfe"
            elif self == stock.STOCK.STOCK_PFFD:
                return "pffd"
            elif self == stock.STOCK.STOCK_PFFR:
                return "pffr"
            elif self == stock.STOCK.STOCK_PFG:
                return "pfg"
            elif self == stock.STOCK.STOCK_PFGC:
                return "pfgc"
            elif self == stock.STOCK.STOCK_PFH:
                return "pfh"
            elif self == stock.STOCK.STOCK_PFI:
                return "pfi"
            elif self == stock.STOCK.STOCK_PFIE:
                return "pfie"
            elif self == stock.STOCK.STOCK_PFIN:
                return "pfin"
            elif self == stock.STOCK.STOCK_PFIS:
                return "pfis"
            elif self == stock.STOCK.STOCK_PFK:
                return "pfk"
            elif self == stock.STOCK.STOCK_PFL:
                return "pfl"
            elif self == stock.STOCK.STOCK_PFLT:
                return "pflt"
            elif self == stock.STOCK.STOCK_PFMT:
                return "pfmt"
            elif self == stock.STOCK.STOCK_PFN:
                return "pfn"
            elif self == stock.STOCK.STOCK_PFNX:
                return "pfnx"
            elif self == stock.STOCK.STOCK_PFO:
                return "pfo"
            elif self == stock.STOCK.STOCK_PFPT:
                return "pfpt"
            elif self == stock.STOCK.STOCK_PFS:
                return "pfs"
            elif self == stock.STOCK.STOCK_PFSI:
                return "pfsi"
            elif self == stock.STOCK.STOCK_PFSW:
                return "pfsw"
            elif self == stock.STOCK.STOCK_PG:
                return "pg"
            elif self == stock.STOCK.STOCK_PGC:
                return "pgc"
            elif self == stock.STOCK.STOCK_PGEM:
                return "pgem"
            elif self == stock.STOCK.STOCK_PGH:
                return "pgh"
            elif self == stock.STOCK.STOCK_PGLC:
                return "pglc"
            elif self == stock.STOCK.STOCK_PGNX:
                return "pgnx"
            elif self == stock.STOCK.STOCK_PGP:
                return "pgp"
            elif self == stock.STOCK.STOCK_PGR:
                return "pgr"
            elif self == stock.STOCK.STOCK_PGRE:
                return "pgre"
            elif self == stock.STOCK.STOCK_PGTI:
                return "pgti"
            elif self == stock.STOCK.STOCK_PGZ:
                return "pgz"
            elif self == stock.STOCK.STOCK_PH:
                return "ph"
            elif self == stock.STOCK.STOCK_PHD:
                return "phd"
            elif self == stock.STOCK.STOCK_PHG:
                return "phg"
            elif self == stock.STOCK.STOCK_PHH:
                return "phh"
            elif self == stock.STOCK.STOCK_PHI:
                return "phi"
            elif self == stock.STOCK.STOCK_PHII:
                return "phii"
            elif self == stock.STOCK.STOCK_PHIIK:
                return "phiik"
            elif self == stock.STOCK.STOCK_PHK:
                return "phk"
            elif self == stock.STOCK.STOCK_PHM:
                return "phm"
            elif self == stock.STOCK.STOCK_PHO:
                return "pho"
            elif self == stock.STOCK.STOCK_PHT:
                return "pht"
            elif self == stock.STOCK.STOCK_PHX:
                return "phx"
            elif self == stock.STOCK.STOCK_PHYS:
                return "phys"
            elif self == stock.STOCK.STOCK_PI:
                return "pi"
            elif self == stock.STOCK.STOCK_PICO:
                return "pico"
            elif self == stock.STOCK.STOCK_PID:
                return "pid"
            elif self == stock.STOCK.STOCK_PIH:
                return "pih"
            elif self == stock.STOCK.STOCK_PII:
                return "pii"
            elif self == stock.STOCK.STOCK_PIM:
                return "pim"
            elif self == stock.STOCK.STOCK_PINC:
                return "pinc"
            elif self == stock.STOCK.STOCK_PIR:
                return "pir"
            elif self == stock.STOCK.STOCK_PIRS:
                return "pirs"
            elif self == stock.STOCK.STOCK_PIXY:
                return "pixy"
            elif self == stock.STOCK.STOCK_PIY:
                return "piy"
            elif self == stock.STOCK.STOCK_PIZ:
                return "piz"
            elif self == stock.STOCK.STOCK_PJC:
                return "pjc"
            elif self == stock.STOCK.STOCK_PJH:
                return "pjh"
            elif self == stock.STOCK.STOCK_PJT:
                return "pjt"
            elif self == stock.STOCK.STOCK_PK:
                return "pk"
            elif self == stock.STOCK.STOCK_PKBK:
                return "pkbk"
            elif self == stock.STOCK.STOCK_PKD:
                return "pkd"
            elif self == stock.STOCK.STOCK_PKE:
                return "pke"
            elif self == stock.STOCK.STOCK_PKG:
                return "pkg"
            elif self == stock.STOCK.STOCK_PKI:
                return "pki"
            elif self == stock.STOCK.STOCK_PKO:
                return "pko"
            elif self == stock.STOCK.STOCK_PKOH:
                return "pkoh"
            elif self == stock.STOCK.STOCK_PKW:
                return "pkw"
            elif self == stock.STOCK.STOCK_PKX:
                return "pkx"
            elif self == stock.STOCK.STOCK_PKY:
                return "pky"
            elif self == stock.STOCK.STOCK_PLAB:
                return "plab"
            elif self == stock.STOCK.STOCK_PLAY:
                return "play"
            elif self == stock.STOCK.STOCK_PLBC:
                return "plbc"
            elif self == stock.STOCK.STOCK_PLCE:
                return "plce"
            elif self == stock.STOCK.STOCK_PLD:
                return "pld"
            elif self == stock.STOCK.STOCK_PLG:
                return "plg"
            elif self == stock.STOCK.STOCK_PLM:
                return "plm"
            elif self == stock.STOCK.STOCK_PLNT:
                return "plnt"
            elif self == stock.STOCK.STOCK_PLOW:
                return "plow"
            elif self == stock.STOCK.STOCK_PLPC:
                return "plpc"
            elif self == stock.STOCK.STOCK_PLPM:
                return "plpm"
            elif self == stock.STOCK.STOCK_PLSE:
                return "plse"
            elif self == stock.STOCK.STOCK_PLT:
                return "plt"
            elif self == stock.STOCK.STOCK_PLUG:
                return "plug"
            elif self == stock.STOCK.STOCK_PLUS:
                return "plus"
            elif self == stock.STOCK.STOCK_PLW:
                return "plw"
            elif self == stock.STOCK.STOCK_PLX:
                return "plx"
            elif self == stock.STOCK.STOCK_PLXP:
                return "plxp"
            elif self == stock.STOCK.STOCK_PLXS:
                return "plxs"
            elif self == stock.STOCK.STOCK_PLYA:
                return "plya"
            elif self == stock.STOCK.STOCK_PLYM:
                return "plym"
            elif self == stock.STOCK.STOCK_PLYM_A:
                return "plym_a"
            elif self == stock.STOCK.STOCK_PM:
                return "pm"
            elif self == stock.STOCK.STOCK_PMBC:
                return "pmbc"
            elif self == stock.STOCK.STOCK_PMC:
                return "pmc"
            elif self == stock.STOCK.STOCK_PMD:
                return "pmd"
            elif self == stock.STOCK.STOCK_PME:
                return "pme"
            elif self == stock.STOCK.STOCK_PMF:
                return "pmf"
            elif self == stock.STOCK.STOCK_PML:
                return "pml"
            elif self == stock.STOCK.STOCK_PMM:
                return "pmm"
            elif self == stock.STOCK.STOCK_PMO:
                return "pmo"
            elif self == stock.STOCK.STOCK_PMOM:
                return "pmom"
            elif self == stock.STOCK.STOCK_PMPT:
                return "pmpt"
            elif self == stock.STOCK.STOCK_PMT:
                return "pmt"
            elif self == stock.STOCK.STOCK_PMTS:
                return "pmts"
            elif self == stock.STOCK.STOCK_PMT_A:
                return "pmt_a"
            elif self == stock.STOCK.STOCK_PMT_B:
                return "pmt_b"
            elif self == stock.STOCK.STOCK_PMX:
                return "pmx"
            elif self == stock.STOCK.STOCK_PN:
                return "pn"
            elif self == stock.STOCK.STOCK_PNBK:
                return "pnbk"
            elif self == stock.STOCK.STOCK_PNC-WS:
                return "pnc-ws"
            elif self == stock.STOCK.STOCK_PNC:
                return "pnc"
            elif self == stock.STOCK.STOCK_PNC_P:
                return "pnc_p"
            elif self == stock.STOCK.STOCK_PNC_Q:
                return "pnc_q"
            elif self == stock.STOCK.STOCK_PNF:
                return "pnf"
            elif self == stock.STOCK.STOCK_PNFP:
                return "pnfp"
            elif self == stock.STOCK.STOCK_PNI:
                return "pni"
            elif self == stock.STOCK.STOCK_PNK:
                return "pnk"
            elif self == stock.STOCK.STOCK_PNM:
                return "pnm"
            elif self == stock.STOCK.STOCK_PNNT:
                return "pnnt"
            elif self == stock.STOCK.STOCK_PNR:
                return "pnr"
            elif self == stock.STOCK.STOCK_PNRG:
                return "pnrg"
            elif self == stock.STOCK.STOCK_PNTR:
                return "pntr"
            elif self == stock.STOCK.STOCK_PNW:
                return "pnw"
            elif self == stock.STOCK.STOCK_PODD:
                return "podd"
            elif self == stock.STOCK.STOCK_POL:
                return "pol"
            elif self == stock.STOCK.STOCK_POLA:
                return "pola"
            elif self == stock.STOCK.STOCK_POOL:
                return "pool"
            elif self == stock.STOCK.STOCK_POPE:
                return "pope"
            elif self == stock.STOCK.STOCK_POR:
                return "por"
            elif self == stock.STOCK.STOCK_POST:
                return "post"
            elif self == stock.STOCK.STOCK_POT:
                return "pot"
            elif self == stock.STOCK.STOCK_POWI:
                return "powi"
            elif self == stock.STOCK.STOCK_POWL:
                return "powl"
            elif self == stock.STOCK.STOCK_PPBI:
                return "ppbi"
            elif self == stock.STOCK.STOCK_PPC:
                return "ppc"
            elif self == stock.STOCK.STOCK_PPDF:
                return "ppdf"
            elif self == stock.STOCK.STOCK_PPG:
                return "ppg"
            elif self == stock.STOCK.STOCK_PPHM:
                return "pphm"
            elif self == stock.STOCK.STOCK_PPHMP:
                return "pphmp"
            elif self == stock.STOCK.STOCK_PPIH:
                return "ppih"
            elif self == stock.STOCK.STOCK_PPL:
                return "ppl"
            elif self == stock.STOCK.STOCK_PPLN:
                return "ppln"
            elif self == stock.STOCK.STOCK_PPR:
                return "ppr"
            elif self == stock.STOCK.STOCK_PPSI:
                return "ppsi"
            elif self == stock.STOCK.STOCK_PPT:
                return "ppt"
            elif self == stock.STOCK.STOCK_PPX:
                return "ppx"
            elif self == stock.STOCK.STOCK_PQ:
                return "pq"
            elif self == stock.STOCK.STOCK_PQG:
                return "pqg"
            elif self == stock.STOCK.STOCK_PRA:
                return "pra"
            elif self == stock.STOCK.STOCK_PRAA:
                return "praa"
            elif self == stock.STOCK.STOCK_PRAH:
                return "prah"
            elif self == stock.STOCK.STOCK_PRAN:
                return "pran"
            elif self == stock.STOCK.STOCK_PRCP:
                return "prcp"
            elif self == stock.STOCK.STOCK_PREF:
                return "pref"
            elif self == stock.STOCK.STOCK_PRE_F:
                return "pre_f"
            elif self == stock.STOCK.STOCK_PRE_G:
                return "pre_g"
            elif self == stock.STOCK.STOCK_PRE_H:
                return "pre_h"
            elif self == stock.STOCK.STOCK_PRE_I:
                return "pre_i"
            elif self == stock.STOCK.STOCK_PRFT:
                return "prft"
            elif self == stock.STOCK.STOCK_PRGO:
                return "prgo"
            elif self == stock.STOCK.STOCK_PRGS:
                return "prgs"
            elif self == stock.STOCK.STOCK_PRGX:
                return "prgx"
            elif self == stock.STOCK.STOCK_PRH:
                return "prh"
            elif self == stock.STOCK.STOCK_PRI:
                return "pri"
            elif self == stock.STOCK.STOCK_PRIM:
                return "prim"
            elif self == stock.STOCK.STOCK_PRK:
                return "prk"
            elif self == stock.STOCK.STOCK_PRKR:
                return "prkr"
            elif self == stock.STOCK.STOCK_PRLB:
                return "prlb"
            elif self == stock.STOCK.STOCK_PRME:
                return "prme"
            elif self == stock.STOCK.STOCK_PRMW:
                return "prmw"
            elif self == stock.STOCK.STOCK_PRNT:
                return "prnt"
            elif self == stock.STOCK.STOCK_PRO:
                return "pro"
            elif self == stock.STOCK.STOCK_PROV:
                return "prov"
            elif self == stock.STOCK.STOCK_PRPH:
                return "prph"
            elif self == stock.STOCK.STOCK_PRPO:
                return "prpo"
            elif self == stock.STOCK.STOCK_PRQR:
                return "prqr"
            elif self == stock.STOCK.STOCK_PRSC:
                return "prsc"
            elif self == stock.STOCK.STOCK_PRSS:
                return "prss"
            elif self == stock.STOCK.STOCK_PRTA:
                return "prta"
            elif self == stock.STOCK.STOCK_PRTK:
                return "prtk"
            elif self == stock.STOCK.STOCK_PRTO:
                return "prto"
            elif self == stock.STOCK.STOCK_PRTS:
                return "prts"
            elif self == stock.STOCK.STOCK_PRTY:
                return "prty"
            elif self == stock.STOCK.STOCK_PRU:
                return "pru"
            elif self == stock.STOCK.STOCK_PSA:
                return "psa"
            elif self == stock.STOCK.STOCK_PSA_A:
                return "psa_a"
            elif self == stock.STOCK.STOCK_PSA_B:
                return "psa_b"
            elif self == stock.STOCK.STOCK_PSA_C:
                return "psa_c"
            elif self == stock.STOCK.STOCK_PSA_D:
                return "psa_d"
            elif self == stock.STOCK.STOCK_PSA_E:
                return "psa_e"
            elif self == stock.STOCK.STOCK_PSA_F:
                return "psa_f"
            elif self == stock.STOCK.STOCK_PSA_G:
                return "psa_g"
            elif self == stock.STOCK.STOCK_PSA_U:
                return "psa_u"
            elif self == stock.STOCK.STOCK_PSA_V:
                return "psa_v"
            elif self == stock.STOCK.STOCK_PSA_W:
                return "psa_w"
            elif self == stock.STOCK.STOCK_PSA_X:
                return "psa_x"
            elif self == stock.STOCK.STOCK_PSA_Y:
                return "psa_y"
            elif self == stock.STOCK.STOCK_PSA_Z:
                return "psa_z"
            elif self == stock.STOCK.STOCK_PSB:
                return "psb"
            elif self == stock.STOCK.STOCK_PSB_T:
                return "psb_t"
            elif self == stock.STOCK.STOCK_PSB_U:
                return "psb_u"
            elif self == stock.STOCK.STOCK_PSB_V:
                return "psb_v"
            elif self == stock.STOCK.STOCK_PSB_W:
                return "psb_w"
            elif self == stock.STOCK.STOCK_PSB_X:
                return "psb_x"
            elif self == stock.STOCK.STOCK_PSC:
                return "psc"
            elif self == stock.STOCK.STOCK_PSDO:
                return "psdo"
            elif self == stock.STOCK.STOCK_PSDV:
                return "psdv"
            elif self == stock.STOCK.STOCK_PSEC:
                return "psec"
            elif self == stock.STOCK.STOCK_PSET:
                return "pset"
            elif self == stock.STOCK.STOCK_PSF:
                return "psf"
            elif self == stock.STOCK.STOCK_PSL:
                return "psl"
            elif self == stock.STOCK.STOCK_PSLV:
                return "pslv"
            elif self == stock.STOCK.STOCK_PSMB:
                return "psmb"
            elif self == stock.STOCK.STOCK_PSMC:
                return "psmc"
            elif self == stock.STOCK.STOCK_PSMG:
                return "psmg"
            elif self == stock.STOCK.STOCK_PSMM:
                return "psmm"
            elif self == stock.STOCK.STOCK_PSMT:
                return "psmt"
            elif self == stock.STOCK.STOCK_PSO:
                return "pso"
            elif self == stock.STOCK.STOCK_PSTB:
                return "pstb"
            elif self == stock.STOCK.STOCK_PSTG:
                return "pstg"
            elif self == stock.STOCK.STOCK_PSTI:
                return "psti"
            elif self == stock.STOCK.STOCK_PSX:
                return "psx"
            elif self == stock.STOCK.STOCK_PSXP:
                return "psxp"
            elif self == stock.STOCK.STOCK_PTC:
                return "ptc"
            elif self == stock.STOCK.STOCK_PTCT:
                return "ptct"
            elif self == stock.STOCK.STOCK_PTEN:
                return "pten"
            elif self == stock.STOCK.STOCK_PTEU:
                return "pteu"
            elif self == stock.STOCK.STOCK_PTF:
                return "ptf"
            elif self == stock.STOCK.STOCK_PTGX:
                return "ptgx"
            elif self == stock.STOCK.STOCK_PTH:
                return "pth"
            elif self == stock.STOCK.STOCK_PTI:
                return "pti"
            elif self == stock.STOCK.STOCK_PTIE:
                return "ptie"
            elif self == stock.STOCK.STOCK_PTLA:
                return "ptla"
            elif self == stock.STOCK.STOCK_PTLC:
                return "ptlc"
            elif self == stock.STOCK.STOCK_PTMC:
                return "ptmc"
            elif self == stock.STOCK.STOCK_PTN:
                return "ptn"
            elif self == stock.STOCK.STOCK_PTNQ:
                return "ptnq"
            elif self == stock.STOCK.STOCK_PTNR:
                return "ptnr"
            elif self == stock.STOCK.STOCK_PTR:
                return "ptr"
            elif self == stock.STOCK.STOCK_PTSI:
                return "ptsi"
            elif self == stock.STOCK.STOCK_PTX:
                return "ptx"
            elif self == stock.STOCK.STOCK_PTY:
                return "pty"
            elif self == stock.STOCK.STOCK_PUB:
                return "pub"
            elif self == stock.STOCK.STOCK_PUI:
                return "pui"
            elif self == stock.STOCK.STOCK_PUK:
                return "puk"
            elif self == stock.STOCK.STOCK_PUK_:
                return "puk_"
            elif self == stock.STOCK.STOCK_PUK_A:
                return "puk_a"
            elif self == stock.STOCK.STOCK_PULM:
                return "pulm"
            elif self == stock.STOCK.STOCK_PUMP:
                return "pump"
            elif self == stock.STOCK.STOCK_PUTW:
                return "putw"
            elif self == stock.STOCK.STOCK_PVAC:
                return "pvac"
            elif self == stock.STOCK.STOCK_PVAL:
                return "pval"
            elif self == stock.STOCK.STOCK_PVBC:
                return "pvbc"
            elif self == stock.STOCK.STOCK_PVG:
                return "pvg"
            elif self == stock.STOCK.STOCK_PVH:
                return "pvh"
            elif self == stock.STOCK.STOCK_PW:
                return "pw"
            elif self == stock.STOCK.STOCK_PWOD:
                return "pwod"
            elif self == stock.STOCK.STOCK_PWR:
                return "pwr"
            elif self == stock.STOCK.STOCK_PW_A:
                return "pw_a"
            elif self == stock.STOCK.STOCK_PX:
                return "px"
            elif self == stock.STOCK.STOCK_PXD:
                return "pxd"
            elif self == stock.STOCK.STOCK_PXI:
                return "pxi"
            elif self == stock.STOCK.STOCK_PXLW:
                return "pxlw"
            elif self == stock.STOCK.STOCK_PXS:
                return "pxs"
            elif self == stock.STOCK.STOCK_PXUS:
                return "pxus"
            elif self == stock.STOCK.STOCK_PY:
                return "py"
            elif self == stock.STOCK.STOCK_PYDS:
                return "pyds"
            elif self == stock.STOCK.STOCK_PYN:
                return "pyn"
            elif self == stock.STOCK.STOCK_PYPL:
                return "pypl"
            elif self == stock.STOCK.STOCK_PYS:
                return "pys"
            elif self == stock.STOCK.STOCK_PYT:
                return "pyt"
            elif self == stock.STOCK.STOCK_PYZ:
                return "pyz"
            elif self == stock.STOCK.STOCK_PZC:
                return "pzc"
            elif self == stock.STOCK.STOCK_PZE:
                return "pze"
            elif self == stock.STOCK.STOCK_PZG:
                return "pzg"
            elif self == stock.STOCK.STOCK_PZN:
                return "pzn"
            elif self == stock.STOCK.STOCK_PZRX:
                return "pzrx"
            elif self == stock.STOCK.STOCK_PZZA:
                return "pzza"
            elif self == stock.STOCK.STOCK_Q:
                return "q"
            elif self == stock.STOCK.STOCK_QADA:
                return "qada"
            elif self == stock.STOCK.STOCK_QADB:
                return "qadb"
            elif self == stock.STOCK.STOCK_QBAK:
                return "qbak"
            elif self == stock.STOCK.STOCK_QCOM:
                return "qcom"
            elif self == stock.STOCK.STOCK_QCP:
                return "qcp"
            elif self == stock.STOCK.STOCK_QCRH:
                return "qcrh"
            elif self == stock.STOCK.STOCK_QD:
                return "qd"
            elif self == stock.STOCK.STOCK_QDEL:
                return "qdel"
            elif self == stock.STOCK.STOCK_QEP:
                return "qep"
            elif self == stock.STOCK.STOCK_QGEN:
                return "qgen"
            elif self == stock.STOCK.STOCK_QGTA:
                return "qgta"
            elif self == stock.STOCK.STOCK_QHC:
                return "qhc"
            elif self == stock.STOCK.STOCK_QIWI:
                return "qiwi"
            elif self == stock.STOCK.STOCK_QLC:
                return "qlc"
            elif self == stock.STOCK.STOCK_QLYS:
                return "qlys"
            elif self == stock.STOCK.STOCK_QMOM:
                return "qmom"
            elif self == stock.STOCK.STOCK_QNST:
                return "qnst"
            elif self == stock.STOCK.STOCK_QQQX:
                return "qqqx"
            elif self == stock.STOCK.STOCK_QRHC:
                return "qrhc"
            elif self == stock.STOCK.STOCK_QRVO:
                return "qrvo"
            elif self == stock.STOCK.STOCK_QSII:
                return "qsii"
            elif self == stock.STOCK.STOCK_QSR:
                return "qsr"
            elif self == stock.STOCK.STOCK_QTM:
                return "qtm"
            elif self == stock.STOCK.STOCK_QTNA:
                return "qtna"
            elif self == stock.STOCK.STOCK_QTNT:
                return "qtnt"
            elif self == stock.STOCK.STOCK_QTRH:
                return "qtrh"
            elif self == stock.STOCK.STOCK_QTS:
                return "qts"
            elif self == stock.STOCK.STOCK_QTWO:
                return "qtwo"
            elif self == stock.STOCK.STOCK_QUAD:
                return "quad"
            elif self == stock.STOCK.STOCK_QUIK:
                return "quik"
            elif self == stock.STOCK.STOCK_QUMU:
                return "qumu"
            elif self == stock.STOCK.STOCK_QUOT:
                return "quot"
            elif self == stock.STOCK.STOCK_QURE:
                return "qure"
            elif self == stock.STOCK.STOCK_QVAL:
                return "qval"
            elif self == stock.STOCK.STOCK_QVCA:
                return "qvca"
            elif self == stock.STOCK.STOCK_QVCB:
                return "qvcb"
            elif self == stock.STOCK.STOCK_QVM:
                return "qvm"
            elif self == stock.STOCK.STOCK_QXGG:
                return "qxgg"
            elif self == stock.STOCK.STOCK_QXMI:
                return "qxmi"
            elif self == stock.STOCK.STOCK_QXRR:
                return "qxrr"
            elif self == stock.STOCK.STOCK_QXTR:
                return "qxtr"
            elif self == stock.STOCK.STOCK_R:
                return "r"
            elif self == stock.STOCK.STOCK_RA:
                return "ra"
            elif self == stock.STOCK.STOCK_RACE:
                return "race"
            elif self == stock.STOCK.STOCK_RAD:
                return "rad"
            elif self == stock.STOCK.STOCK_RADA:
                return "rada"
            elif self == stock.STOCK.STOCK_RAIL:
                return "rail"
            elif self == stock.STOCK.STOCK_RAND:
                return "rand"
            elif self == stock.STOCK.STOCK_RARE:
                return "rare"
            elif self == stock.STOCK.STOCK_RARX:
                return "rarx"
            elif self == stock.STOCK.STOCK_RAS:
                return "ras"
            elif self == stock.STOCK.STOCK_RAS_A:
                return "ras_a"
            elif self == stock.STOCK.STOCK_RAS_B:
                return "ras_b"
            elif self == stock.STOCK.STOCK_RAS_C:
                return "ras_c"
            elif self == stock.STOCK.STOCK_RATE:
                return "rate"
            elif self == stock.STOCK.STOCK_RAVE:
                return "rave"
            elif self == stock.STOCK.STOCK_RAVN:
                return "ravn"
            elif self == stock.STOCK.STOCK_RBA:
                return "rba"
            elif self == stock.STOCK.STOCK_RBB:
                return "rbb"
            elif self == stock.STOCK.STOCK_RBC:
                return "rbc"
            elif self == stock.STOCK.STOCK_RBCAA:
                return "rbcaa"
            elif self == stock.STOCK.STOCK_RBCN:
                return "rbcn"
            elif self == stock.STOCK.STOCK_RBIN:
                return "rbin"
            elif self == stock.STOCK.STOCK_RBIO:
                return "rbio"
            elif self == stock.STOCK.STOCK_RBPAA:
                return "rbpaa"
            elif self == stock.STOCK.STOCK_RBS:
                return "rbs"
            elif self == stock.STOCK.STOCK_RBS_S:
                return "rbs_s"
            elif self == stock.STOCK.STOCK_RBUS:
                return "rbus"
            elif self == stock.STOCK.STOCK_RCG:
                return "rcg"
            elif self == stock.STOCK.STOCK_RCI:
                return "rci"
            elif self == stock.STOCK.STOCK_RCII:
                return "rcii"
            elif self == stock.STOCK.STOCK_RCKY:
                return "rcky"
            elif self == stock.STOCK.STOCK_RCL:
                return "rcl"
            elif self == stock.STOCK.STOCK_RCM:
                return "rcm"
            elif self == stock.STOCK.STOCK_RCMT:
                return "rcmt"
            elif self == stock.STOCK.STOCK_RCOM:
                return "rcom"
            elif self == stock.STOCK.STOCK_RCON:
                return "rcon"
            elif self == stock.STOCK.STOCK_RCS:
                return "rcs"
            elif self == stock.STOCK.STOCK_RDC:
                return "rdc"
            elif self == stock.STOCK.STOCK_RDCM:
                return "rdcm"
            elif self == stock.STOCK.STOCK_RDFN:
                return "rdfn"
            elif self == stock.STOCK.STOCK_RDHL:
                return "rdhl"
            elif self == stock.STOCK.STOCK_RDI:
                return "rdi"
            elif self == stock.STOCK.STOCK_RDIB:
                return "rdib"
            elif self == stock.STOCK.STOCK_RDN:
                return "rdn"
            elif self == stock.STOCK.STOCK_RDNT:
                return "rdnt"
            elif self == stock.STOCK.STOCK_RDS-A:
                return "rds-a"
            elif self == stock.STOCK.STOCK_RDS-B:
                return "rds-b"
            elif self == stock.STOCK.STOCK_RDUS:
                return "rdus"
            elif self == stock.STOCK.STOCK_RDWR:
                return "rdwr"
            elif self == stock.STOCK.STOCK_RDY:
                return "rdy"
            elif self == stock.STOCK.STOCK_RE:
                return "re"
            elif self == stock.STOCK.STOCK_RECN:
                return "recn"
            elif self == stock.STOCK.STOCK_REDU:
                return "redu"
            elif self == stock.STOCK.STOCK_REED:
                return "reed"
            elif self == stock.STOCK.STOCK_REEM:
                return "reem"
            elif self == stock.STOCK.STOCK_REFA:
                return "refa"
            elif self == stock.STOCK.STOCK_REFR:
                return "refr"
            elif self == stock.STOCK.STOCK_REG:
                return "reg"
            elif self == stock.STOCK.STOCK_REGI:
                return "regi"
            elif self == stock.STOCK.STOCK_REGN:
                return "regn"
            elif self == stock.STOCK.STOCK_REI:
                return "rei"
            elif self == stock.STOCK.STOCK_REIS:
                return "reis"
            elif self == stock.STOCK.STOCK_RELL:
                return "rell"
            elif self == stock.STOCK.STOCK_RELV:
                return "relv"
            elif self == stock.STOCK.STOCK_RELX:
                return "relx"
            elif self == stock.STOCK.STOCK_RELY:
                return "rely"
            elif self == stock.STOCK.STOCK_REML:
                return "reml"
            elif self == stock.STOCK.STOCK_REN:
                return "ren"
            elif self == stock.STOCK.STOCK_RENN:
                return "renn"
            elif self == stock.STOCK.STOCK_RENX:
                return "renx"
            elif self == stock.STOCK.STOCK_REPH:
                return "reph"
            elif self == stock.STOCK.STOCK_RES:
                return "res"
            elif self == stock.STOCK.STOCK_RESI:
                return "resi"
            elif self == stock.STOCK.STOCK_RESN:
                return "resn"
            elif self == stock.STOCK.STOCK_RETA:
                return "reta"
            elif self == stock.STOCK.STOCK_REV:
                return "rev"
            elif self == stock.STOCK.STOCK_REVG:
                return "revg"
            elif self == stock.STOCK.STOCK_REX:
                return "rex"
            elif self == stock.STOCK.STOCK_REXR:
                return "rexr"
            elif self == stock.STOCK.STOCK_REXR_A:
                return "rexr_a"
            elif self == stock.STOCK.STOCK_REXX:
                return "rexx"
            elif self == stock.STOCK.STOCK_RF:
                return "rf"
            elif self == stock.STOCK.STOCK_RFAP:
                return "rfap"
            elif self == stock.STOCK.STOCK_RFCI:
                return "rfci"
            elif self == stock.STOCK.STOCK_RFDA:
                return "rfda"
            elif self == stock.STOCK.STOCK_RFDI:
                return "rfdi"
            elif self == stock.STOCK.STOCK_RFEM:
                return "rfem"
            elif self == stock.STOCK.STOCK_RFEU:
                return "rfeu"
            elif self == stock.STOCK.STOCK_RFFC:
                return "rffc"
            elif self == stock.STOCK.STOCK_RFI:
                return "rfi"
            elif self == stock.STOCK.STOCK_RFIL:
                return "rfil"
            elif self == stock.STOCK.STOCK_RFP:
                return "rfp"
            elif self == stock.STOCK.STOCK_RFT:
                return "rft"
            elif self == stock.STOCK.STOCK_RFTA:
                return "rfta"
            elif self == stock.STOCK.STOCK_RFUN:
                return "rfun"
            elif self == stock.STOCK.STOCK_RF_A:
                return "rf_a"
            elif self == stock.STOCK.STOCK_RF_B:
                return "rf_b"
            elif self == stock.STOCK.STOCK_RGA:
                return "rga"
            elif self == stock.STOCK.STOCK_RGC:
                return "rgc"
            elif self == stock.STOCK.STOCK_RGCO:
                return "rgco"
            elif self == stock.STOCK.STOCK_RGEN:
                return "rgen"
            elif self == stock.STOCK.STOCK_RGLB:
                return "rglb"
            elif self == stock.STOCK.STOCK_RGLD:
                return "rgld"
            elif self == stock.STOCK.STOCK_RGLS:
                return "rgls"
            elif self == stock.STOCK.STOCK_RGNX:
                return "rgnx"
            elif self == stock.STOCK.STOCK_RGR:
                return "rgr"
            elif self == stock.STOCK.STOCK_RGS:
                return "rgs"
            elif self == stock.STOCK.STOCK_RGSE:
                return "rgse"
            elif self == stock.STOCK.STOCK_RGT:
                return "rgt"
            elif self == stock.STOCK.STOCK_RH:
                return "rh"
            elif self == stock.STOCK.STOCK_RHE:
                return "rhe"
            elif self == stock.STOCK.STOCK_RHE_A:
                return "rhe_a"
            elif self == stock.STOCK.STOCK_RHI:
                return "rhi"
            elif self == stock.STOCK.STOCK_RHP:
                return "rhp"
            elif self == stock.STOCK.STOCK_RHT:
                return "rht"
            elif self == stock.STOCK.STOCK_RIBT:
                return "ribt"
            elif self == stock.STOCK.STOCK_RIBTW:
                return "ribtw"
            elif self == stock.STOCK.STOCK_RIC:
                return "ric"
            elif self == stock.STOCK.STOCK_RICE:
                return "rice"
            elif self == stock.STOCK.STOCK_RICK:
                return "rick"
            elif self == stock.STOCK.STOCK_RIF:
                return "rif"
            elif self == stock.STOCK.STOCK_RIG:
                return "rig"
            elif self == stock.STOCK.STOCK_RIGL:
                return "rigl"
            elif self == stock.STOCK.STOCK_RILY:
                return "rily"
            elif self == stock.STOCK.STOCK_RILYL:
                return "rilyl"
            elif self == stock.STOCK.STOCK_RILYZ:
                return "rilyz"
            elif self == stock.STOCK.STOCK_RIO:
                return "rio"
            elif self == stock.STOCK.STOCK_RIOT:
                return "riot"
            elif self == stock.STOCK.STOCK_RISE:
                return "rise"
            elif self == stock.STOCK.STOCK_RIV:
                return "riv"
            elif self == stock.STOCK.STOCK_RIVR:
                return "rivr"
            elif self == stock.STOCK.STOCK_RIVRW:
                return "rivrw"
            elif self == stock.STOCK.STOCK_RJF:
                return "rjf"
            elif self == stock.STOCK.STOCK_RKDA:
                return "rkda"
            elif self == stock.STOCK.STOCK_RL:
                return "rl"
            elif self == stock.STOCK.STOCK_RLGT:
                return "rlgt"
            elif self == stock.STOCK.STOCK_RLGT_A:
                return "rlgt_a"
            elif self == stock.STOCK.STOCK_RLGY:
                return "rlgy"
            elif self == stock.STOCK.STOCK_RLH:
                return "rlh"
            elif self == stock.STOCK.STOCK_RLI:
                return "rli"
            elif self == stock.STOCK.STOCK_RLJ:
                return "rlj"
            elif self == stock.STOCK.STOCK_RLJE:
                return "rlje"
            elif self == stock.STOCK.STOCK_RLJ_A:
                return "rlj_a"
            elif self == stock.STOCK.STOCK_RLOG:
                return "rlog"
            elif self == stock.STOCK.STOCK_RM:
                return "rm"
            elif self == stock.STOCK.STOCK_RMAX:
                return "rmax"
            elif self == stock.STOCK.STOCK_RMBL:
                return "rmbl"
            elif self == stock.STOCK.STOCK_RMBS:
                return "rmbs"
            elif self == stock.STOCK.STOCK_RMCF:
                return "rmcf"
            elif self == stock.STOCK.STOCK_RMD:
                return "rmd"
            elif self == stock.STOCK.STOCK_RMGN:
                return "rmgn"
            elif self == stock.STOCK.STOCK_RMNI:
                return "rmni"
            elif self == stock.STOCK.STOCK_RMNIU:
                return "rmniu"
            elif self == stock.STOCK.STOCK_RMNIW:
                return "rmniw"
            elif self == stock.STOCK.STOCK_RMP:
                return "rmp"
            elif self == stock.STOCK.STOCK_RMPL_:
                return "rmpl_"
            elif self == stock.STOCK.STOCK_RMR:
                return "rmr"
            elif self == stock.STOCK.STOCK_RMT:
                return "rmt"
            elif self == stock.STOCK.STOCK_RMTI:
                return "rmti"
            elif self == stock.STOCK.STOCK_RNDB:
                return "rndb"
            elif self == stock.STOCK.STOCK_RNDM:
                return "rndm"
            elif self == stock.STOCK.STOCK_RNDV:
                return "rndv"
            elif self == stock.STOCK.STOCK_RNEM:
                return "rnem"
            elif self == stock.STOCK.STOCK_RNET:
                return "rnet"
            elif self == stock.STOCK.STOCK_RNG:
                return "rng"
            elif self == stock.STOCK.STOCK_RNGR:
                return "rngr"
            elif self == stock.STOCK.STOCK_RNLC:
                return "rnlc"
            elif self == stock.STOCK.STOCK_RNMC:
                return "rnmc"
            elif self == stock.STOCK.STOCK_RNN:
                return "rnn"
            elif self == stock.STOCK.STOCK_RNP:
                return "rnp"
            elif self == stock.STOCK.STOCK_RNR:
                return "rnr"
            elif self == stock.STOCK.STOCK_RNR_C:
                return "rnr_c"
            elif self == stock.STOCK.STOCK_RNR_E:
                return "rnr_e"
            elif self == stock.STOCK.STOCK_RNSC:
                return "rnsc"
            elif self == stock.STOCK.STOCK_RNST:
                return "rnst"
            elif self == stock.STOCK.STOCK_RNVA:
                return "rnva"
            elif self == stock.STOCK.STOCK_RNVAZ:
                return "rnvaz"
            elif self == stock.STOCK.STOCK_RNWK:
                return "rnwk"
            elif self == stock.STOCK.STOCK_ROAM:
                return "roam"
            elif self == stock.STOCK.STOCK_ROCK:
                return "rock"
            elif self == stock.STOCK.STOCK_RODM:
                return "rodm"
            elif self == stock.STOCK.STOCK_ROG:
                return "rog"
            elif self == stock.STOCK.STOCK_ROGS:
                return "rogs"
            elif self == stock.STOCK.STOCK_ROIC:
                return "roic"
            elif self == stock.STOCK.STOCK_ROK:
                return "rok"
            elif self == stock.STOCK.STOCK_ROKA:
                return "roka"
            elif self == stock.STOCK.STOCK_ROKU:
                return "roku"
            elif self == stock.STOCK.STOCK_ROL:
                return "rol"
            elif self == stock.STOCK.STOCK_ROLL:
                return "roll"
            elif self == stock.STOCK.STOCK_ROP:
                return "rop"
            elif self == stock.STOCK.STOCK_RORE:
                return "rore"
            elif self == stock.STOCK.STOCK_ROSE:
                return "rose"
            elif self == stock.STOCK.STOCK_ROSEU:
                return "roseu"
            elif self == stock.STOCK.STOCK_ROSEW:
                return "rosew"
            elif self == stock.STOCK.STOCK_ROSG:
                return "rosg"
            elif self == stock.STOCK.STOCK_ROST:
                return "rost"
            elif self == stock.STOCK.STOCK_ROUS:
                return "rous"
            elif self == stock.STOCK.STOCK_ROX:
                return "rox"
            elif self == stock.STOCK.STOCK_ROYT:
                return "royt"
            elif self == stock.STOCK.STOCK_RP:
                return "rp"
            elif self == stock.STOCK.STOCK_RPAI:
                return "rpai"
            elif self == stock.STOCK.STOCK_RPAI_A-CL:
                return "rpai_a-cl"
            elif self == stock.STOCK.STOCK_RPAI_A:
                return "rpai_a"
            elif self == stock.STOCK.STOCK_RPD:
                return "rpd"
            elif self == stock.STOCK.STOCK_RPM:
                return "rpm"
            elif self == stock.STOCK.STOCK_RPRX:
                return "rprx"
            elif self == stock.STOCK.STOCK_RPT:
                return "rpt"
            elif self == stock.STOCK.STOCK_RPT_D:
                return "rpt_d"
            elif self == stock.STOCK.STOCK_RPXC:
                return "rpxc"
            elif self == stock.STOCK.STOCK_RQI:
                return "rqi"
            elif self == stock.STOCK.STOCK_RRC:
                return "rrc"
            elif self == stock.STOCK.STOCK_RRD:
                return "rrd"
            elif self == stock.STOCK.STOCK_RRGB:
                return "rrgb"
            elif self == stock.STOCK.STOCK_RRR:
                return "rrr"
            elif self == stock.STOCK.STOCK_RRTS:
                return "rrts"
            elif self == stock.STOCK.STOCK_RS:
                return "rs"
            elif self == stock.STOCK.STOCK_RSG:
                return "rsg"
            elif self == stock.STOCK.STOCK_RSLS:
                return "rsls"
            elif self == stock.STOCK.STOCK_RSO:
                return "rso"
            elif self == stock.STOCK.STOCK_RSO_A:
                return "rso_a"
            elif self == stock.STOCK.STOCK_RSO_B:
                return "rso_b"
            elif self == stock.STOCK.STOCK_RSO_C:
                return "rso_c"
            elif self == stock.STOCK.STOCK_RSPP:
                return "rspp"
            elif self == stock.STOCK.STOCK_RST:
                return "rst"
            elif self == stock.STOCK.STOCK_RSYS:
                return "rsys"
            elif self == stock.STOCK.STOCK_RT:
                return "rt"
            elif self == stock.STOCK.STOCK_RTEC:
                return "rtec"
            elif self == stock.STOCK.STOCK_RTIX:
                return "rtix"
            elif self == stock.STOCK.STOCK_RTK:
                return "rtk"
            elif self == stock.STOCK.STOCK_RTN:
                return "rtn"
            elif self == stock.STOCK.STOCK_RTNB:
                return "rtnb"
            elif self == stock.STOCK.STOCK_RTRX:
                return "rtrx"
            elif self == stock.STOCK.STOCK_RTTR:
                return "rttr"
            elif self == stock.STOCK.STOCK_RUBI:
                return "rubi"
            elif self == stock.STOCK.STOCK_RUN:
                return "run"
            elif self == stock.STOCK.STOCK_RUSHA:
                return "rusha"
            elif self == stock.STOCK.STOCK_RUSHB:
                return "rushb"
            elif self == stock.STOCK.STOCK_RUTH:
                return "ruth"
            elif self == stock.STOCK.STOCK_RVEN:
                return "rven"
            elif self == stock.STOCK.STOCK_RVLT:
                return "rvlt"
            elif self == stock.STOCK.STOCK_RVNC:
                return "rvnc"
            elif self == stock.STOCK.STOCK_RVP:
                return "rvp"
            elif self == stock.STOCK.STOCK_RVRS:
                return "rvrs"
            elif self == stock.STOCK.STOCK_RVSB:
                return "rvsb"
            elif self == stock.STOCK.STOCK_RVT:
                return "rvt"
            elif self == stock.STOCK.STOCK_RWC:
                return "rwc"
            elif self == stock.STOCK.STOCK_RWLK:
                return "rwlk"
            elif self == stock.STOCK.STOCK_RWT:
                return "rwt"
            elif self == stock.STOCK.STOCK_RXDX:
                return "rxdx"
            elif self == stock.STOCK.STOCK_RXII:
                return "rxii"
            elif self == stock.STOCK.STOCK_RXIIW:
                return "rxiiw"
            elif self == stock.STOCK.STOCK_RXN:
                return "rxn"
            elif self == stock.STOCK.STOCK_RXN_A:
                return "rxn_a"
            elif self == stock.STOCK.STOCK_RY:
                return "ry"
            elif self == stock.STOCK.STOCK_RYAAY:
                return "ryaay"
            elif self == stock.STOCK.STOCK_RYAM:
                return "ryam"
            elif self == stock.STOCK.STOCK_RYAM_A:
                return "ryam_a"
            elif self == stock.STOCK.STOCK_RYB:
                return "ryb"
            elif self == stock.STOCK.STOCK_RYI:
                return "ryi"
            elif self == stock.STOCK.STOCK_RYN:
                return "ryn"
            elif self == stock.STOCK.STOCK_RYTM:
                return "rytm"
            elif self == stock.STOCK.STOCK_RY_S-CL:
                return "ry_s-cl"
            elif self == stock.STOCK.STOCK_RY_T:
                return "ry_t"
            elif self == stock.STOCK.STOCK_RZA:
                return "rza"
            elif self == stock.STOCK.STOCK_RZB:
                return "rzb"
            elif self == stock.STOCK.STOCK_S:
                return "s"
            elif self == stock.STOCK.STOCK_SA:
                return "sa"
            elif self == stock.STOCK.STOCK_SAB:
                return "sab"
            elif self == stock.STOCK.STOCK_SABR:
                return "sabr"
            elif self == stock.STOCK.STOCK_SACH:
                return "sach"
            elif self == stock.STOCK.STOCK_SAEX:
                return "saex"
            elif self == stock.STOCK.STOCK_SAFE:
                return "safe"
            elif self == stock.STOCK.STOCK_SAFM:
                return "safm"
            elif self == stock.STOCK.STOCK_SAFT:
                return "saft"
            elif self == stock.STOCK.STOCK_SAGE:
                return "sage"
            elif self == stock.STOCK.STOCK_SAH:
                return "sah"
            elif self == stock.STOCK.STOCK_SAIA:
                return "saia"
            elif self == stock.STOCK.STOCK_SAIC:
                return "saic"
            elif self == stock.STOCK.STOCK_SAIL:
                return "sail"
            elif self == stock.STOCK.STOCK_SAL:
                return "sal"
            elif self == stock.STOCK.STOCK_SALM:
                return "salm"
            elif self == stock.STOCK.STOCK_SALT:
                return "salt"
            elif self == stock.STOCK.STOCK_SAM:
                return "sam"
            elif self == stock.STOCK.STOCK_SAMG:
                return "samg"
            elif self == stock.STOCK.STOCK_SAN:
                return "san"
            elif self == stock.STOCK.STOCK_SAND:
                return "sand"
            elif self == stock.STOCK.STOCK_SANM:
                return "sanm"
            elif self == stock.STOCK.STOCK_SANW:
                return "sanw"
            elif self == stock.STOCK.STOCK_SAN_A:
                return "san_a"
            elif self == stock.STOCK.STOCK_SAN_B:
                return "san_b"
            elif self == stock.STOCK.STOCK_SAN_C:
                return "san_c"
            elif self == stock.STOCK.STOCK_SAN_I:
                return "san_i"
            elif self == stock.STOCK.STOCK_SAP:
                return "sap"
            elif self == stock.STOCK.STOCK_SAR:
                return "sar"
            elif self == stock.STOCK.STOCK_SASR:
                return "sasr"
            elif self == stock.STOCK.STOCK_SATS:
                return "sats"
            elif self == stock.STOCK.STOCK_SAUC:
                return "sauc"
            elif self == stock.STOCK.STOCK_SAVE:
                return "save"
            elif self == stock.STOCK.STOCK_SB:
                return "sb"
            elif self == stock.STOCK.STOCK_SBAC:
                return "sbac"
            elif self == stock.STOCK.STOCK_SBBC:
                return "sbbc"
            elif self == stock.STOCK.STOCK_SBBP:
                return "sbbp"
            elif self == stock.STOCK.STOCK_SBBX:
                return "sbbx"
            elif self == stock.STOCK.STOCK_SBCF:
                return "sbcf"
            elif self == stock.STOCK.STOCK_SBCP:
                return "sbcp"
            elif self == stock.STOCK.STOCK_SBFG:
                return "sbfg"
            elif self == stock.STOCK.STOCK_SBFGP:
                return "sbfgp"
            elif self == stock.STOCK.STOCK_SBGI:
                return "sbgi"
            elif self == stock.STOCK.STOCK_SBGL:
                return "sbgl"
            elif self == stock.STOCK.STOCK_SBH:
                return "sbh"
            elif self == stock.STOCK.STOCK_SBI:
                return "sbi"
            elif self == stock.STOCK.STOCK_SBLK:
                return "sblk"
            elif self == stock.STOCK.STOCK_SBLKL:
                return "sblkl"
            elif self == stock.STOCK.STOCK_SBNA:
                return "sbna"
            elif self == stock.STOCK.STOCK_SBNB:
                return "sbnb"
            elif self == stock.STOCK.STOCK_SBNY:
                return "sbny"
            elif self == stock.STOCK.STOCK_SBNYW:
                return "sbnyw"
            elif self == stock.STOCK.STOCK_SBOT:
                return "sbot"
            elif self == stock.STOCK.STOCK_SBOW:
                return "sbow"
            elif self == stock.STOCK.STOCK_SBPH:
                return "sbph"
            elif self == stock.STOCK.STOCK_SBR:
                return "sbr"
            elif self == stock.STOCK.STOCK_SBRA:
                return "sbra"
            elif self == stock.STOCK.STOCK_SBRAP:
                return "sbrap"
            elif self == stock.STOCK.STOCK_SBS:
                return "sbs"
            elif self == stock.STOCK.STOCK_SBSI:
                return "sbsi"
            elif self == stock.STOCK.STOCK_SBT:
                return "sbt"
            elif self == stock.STOCK.STOCK_SBUX:
                return "sbux"
            elif self == stock.STOCK.STOCK_SB_B:
                return "sb_b"
            elif self == stock.STOCK.STOCK_SB_C:
                return "sb_c"
            elif self == stock.STOCK.STOCK_SB_D:
                return "sb_d"
            elif self == stock.STOCK.STOCK_SC:
                return "sc"
            elif self == stock.STOCK.STOCK_SCA:
                return "sca"
            elif self == stock.STOCK.STOCK_SCAC:
                return "scac"
            elif self == stock.STOCK.STOCK_SCACU:
                return "scacu"
            elif self == stock.STOCK.STOCK_SCACW:
                return "scacw"
            elif self == stock.STOCK.STOCK_SCAP:
                return "scap"
            elif self == stock.STOCK.STOCK_SCCI:
                return "scci"
            elif self == stock.STOCK.STOCK_SCCO:
                return "scco"
            elif self == stock.STOCK.STOCK_SCD:
                return "scd"
            elif self == stock.STOCK.STOCK_SCE_B:
                return "sce_b"
            elif self == stock.STOCK.STOCK_SCE_C:
                return "sce_c"
            elif self == stock.STOCK.STOCK_SCE_D:
                return "sce_d"
            elif self == stock.STOCK.STOCK_SCE_E:
                return "sce_e"
            elif self == stock.STOCK.STOCK_SCE_G:
                return "sce_g"
            elif self == stock.STOCK.STOCK_SCE_H:
                return "sce_h"
            elif self == stock.STOCK.STOCK_SCE_J:
                return "sce_j"
            elif self == stock.STOCK.STOCK_SCE_K:
                return "sce_k"
            elif self == stock.STOCK.STOCK_SCE_L:
                return "sce_l"
            elif self == stock.STOCK.STOCK_SCG:
                return "scg"
            elif self == stock.STOCK.STOCK_SCHK:
                return "schk"
            elif self == stock.STOCK.STOCK_SCHL:
                return "schl"
            elif self == stock.STOCK.STOCK_SCHN:
                return "schn"
            elif self == stock.STOCK.STOCK_SCHW:
                return "schw"
            elif self == stock.STOCK.STOCK_SCHW_B-CL:
                return "schw_b-cl"
            elif self == stock.STOCK.STOCK_SCHW_B:
                return "schw_b"
            elif self == stock.STOCK.STOCK_SCHW_C:
                return "schw_c"
            elif self == stock.STOCK.STOCK_SCHW_D:
                return "schw_d"
            elif self == stock.STOCK.STOCK_SCI:
                return "sci"
            elif self == stock.STOCK.STOCK_SCKT:
                return "sckt"
            elif self == stock.STOCK.STOCK_SCL:
                return "scl"
            elif self == stock.STOCK.STOCK_SCLN:
                return "scln"
            elif self == stock.STOCK.STOCK_SCM:
                return "scm"
            elif self == stock.STOCK.STOCK_SCMP:
                return "scmp"
            elif self == stock.STOCK.STOCK_SCON:
                return "scon"
            elif self == stock.STOCK.STOCK_SCPH:
                return "scph"
            elif self == stock.STOCK.STOCK_SCS:
                return "scs"
            elif self == stock.STOCK.STOCK_SCSC:
                return "scsc"
            elif self == stock.STOCK.STOCK_SCVL:
                return "scvl"
            elif self == stock.STOCK.STOCK_SCWX:
                return "scwx"
            elif self == stock.STOCK.STOCK_SCX:
                return "scx"
            elif self == stock.STOCK.STOCK_SCYX:
                return "scyx"
            elif self == stock.STOCK.STOCK_SD:
                return "sd"
            elif self == stock.STOCK.STOCK_SDLP:
                return "sdlp"
            elif self == stock.STOCK.STOCK_SDPI:
                return "sdpi"
            elif self == stock.STOCK.STOCK_SDR:
                return "sdr"
            elif self == stock.STOCK.STOCK_SDRL:
                return "sdrl"
            elif self == stock.STOCK.STOCK_SDT:
                return "sdt"
            elif self == stock.STOCK.STOCK_SDVY:
                return "sdvy"
            elif self == stock.STOCK.STOCK_SE:
                return "se"
            elif self == stock.STOCK.STOCK_SEAC:
                return "seac"
            elif self == stock.STOCK.STOCK_SEAS:
                return "seas"
            elif self == stock.STOCK.STOCK_SEB:
                return "seb"
            elif self == stock.STOCK.STOCK_SECO:
                return "seco"
            elif self == stock.STOCK.STOCK_SECT:
                return "sect"
            elif self == stock.STOCK.STOCK_SEDG:
                return "sedg"
            elif self == stock.STOCK.STOCK_SEE:
                return "see"
            elif self == stock.STOCK.STOCK_SEED:
                return "seed"
            elif self == stock.STOCK.STOCK_SEIC:
                return "seic"
            elif self == stock.STOCK.STOCK_SELB:
                return "selb"
            elif self == stock.STOCK.STOCK_SELF:
                return "self"
            elif self == stock.STOCK.STOCK_SEM:
                return "sem"
            elif self == stock.STOCK.STOCK_SEMG:
                return "semg"
            elif self == stock.STOCK.STOCK_SEND:
                return "send"
            elif self == stock.STOCK.STOCK_SENEA:
                return "senea"
            elif self == stock.STOCK.STOCK_SENEB:
                return "seneb"
            elif self == stock.STOCK.STOCK_SENS:
                return "sens"
            elif self == stock.STOCK.STOCK_SEP:
                return "sep"
            elif self == stock.STOCK.STOCK_SERV:
                return "serv"
            elif self == stock.STOCK.STOCK_SF:
                return "sf"
            elif self == stock.STOCK.STOCK_SFB:
                return "sfb"
            elif self == stock.STOCK.STOCK_SFBC:
                return "sfbc"
            elif self == stock.STOCK.STOCK_SFBS:
                return "sfbs"
            elif self == stock.STOCK.STOCK_SFE:
                return "sfe"
            elif self == stock.STOCK.STOCK_SFHY:
                return "sfhy"
            elif self == stock.STOCK.STOCK_SFIG:
                return "sfig"
            elif self == stock.STOCK.STOCK_SFIX:
                return "sfix"
            elif self == stock.STOCK.STOCK_SFL:
                return "sfl"
            elif self == stock.STOCK.STOCK_SFLY:
                return "sfly"
            elif self == stock.STOCK.STOCK_SFM:
                return "sfm"
            elif self == stock.STOCK.STOCK_SFNC:
                return "sfnc"
            elif self == stock.STOCK.STOCK_SFR:
                return "sfr"
            elif self == stock.STOCK.STOCK_SFS:
                return "sfs"
            elif self == stock.STOCK.STOCK_SFST:
                return "sfst"
            elif self == stock.STOCK.STOCK_SFUN:
                return "sfun"
            elif self == stock.STOCK.STOCK_SF_A:
                return "sf_a"
            elif self == stock.STOCK.STOCK_SGA:
                return "sga"
            elif self == stock.STOCK.STOCK_SGB:
                return "sgb"
            elif self == stock.STOCK.STOCK_SGBX:
                return "sgbx"
            elif self == stock.STOCK.STOCK_SGC:
                return "sgc"
            elif self == stock.STOCK.STOCK_SGEN:
                return "sgen"
            elif self == stock.STOCK.STOCK_SGF:
                return "sgf"
            elif self == stock.STOCK.STOCK_SGH:
                return "sgh"
            elif self == stock.STOCK.STOCK_SGLB:
                return "sglb"
            elif self == stock.STOCK.STOCK_SGLBW:
                return "sglbw"
            elif self == stock.STOCK.STOCK_SGMA:
                return "sgma"
            elif self == stock.STOCK.STOCK_SGMO:
                return "sgmo"
            elif self == stock.STOCK.STOCK_SGMS:
                return "sgms"
            elif self == stock.STOCK.STOCK_SGOC:
                return "sgoc"
            elif self == stock.STOCK.STOCK_SGQI:
                return "sgqi"
            elif self == stock.STOCK.STOCK_SGRP:
                return "sgrp"
            elif self == stock.STOCK.STOCK_SGRY:
                return "sgry"
            elif self == stock.STOCK.STOCK_SGU:
                return "sgu"
            elif self == stock.STOCK.STOCK_SGY-WS:
                return "sgy-ws"
            elif self == stock.STOCK.STOCK_SGY:
                return "sgy"
            elif self == stock.STOCK.STOCK_SGYP:
                return "sgyp"
            elif self == stock.STOCK.STOCK_SGZA:
                return "sgza"
            elif self == stock.STOCK.STOCK_SHAG:
                return "shag"
            elif self == stock.STOCK.STOCK_SHAK:
                return "shak"
            elif self == stock.STOCK.STOCK_SHBI:
                return "shbi"
            elif self == stock.STOCK.STOCK_SHE:
                return "she"
            elif self == stock.STOCK.STOCK_SHEN:
                return "shen"
            elif self == stock.STOCK.STOCK_SHG:
                return "shg"
            elif self == stock.STOCK.STOCK_SHI:
                return "shi"
            elif self == stock.STOCK.STOCK_SHIP:
                return "ship"
            elif self == stock.STOCK.STOCK_SHIPW:
                return "shipw"
            elif self == stock.STOCK.STOCK_SHLD:
                return "shld"
            elif self == stock.STOCK.STOCK_SHLDW:
                return "shldw"
            elif self == stock.STOCK.STOCK_SHLM:
                return "shlm"
            elif self == stock.STOCK.STOCK_SHLO:
                return "shlo"
            elif self == stock.STOCK.STOCK_SHLX:
                return "shlx"
            elif self == stock.STOCK.STOCK_SHNY:
                return "shny"
            elif self == stock.STOCK.STOCK_SHO:
                return "sho"
            elif self == stock.STOCK.STOCK_SHOO:
                return "shoo"
            elif self == stock.STOCK.STOCK_SHOP:
                return "shop"
            elif self == stock.STOCK.STOCK_SHOS:
                return "shos"
            elif self == stock.STOCK.STOCK_SHO_E:
                return "sho_e"
            elif self == stock.STOCK.STOCK_SHO_F:
                return "sho_f"
            elif self == stock.STOCK.STOCK_SHPG:
                return "shpg"
            elif self == stock.STOCK.STOCK_SHSP:
                return "shsp"
            elif self == stock.STOCK.STOCK_SHW:
                return "shw"
            elif self == stock.STOCK.STOCK_SID:
                return "sid"
            elif self == stock.STOCK.STOCK_SIEB:
                return "sieb"
            elif self == stock.STOCK.STOCK_SIEN:
                return "sien"
            elif self == stock.STOCK.STOCK_SIF:
                return "sif"
            elif self == stock.STOCK.STOCK_SIFI:
                return "sifi"
            elif self == stock.STOCK.STOCK_SIFY:
                return "sify"
            elif self == stock.STOCK.STOCK_SIG:
                return "sig"
            elif self == stock.STOCK.STOCK_SIGI:
                return "sigi"
            elif self == stock.STOCK.STOCK_SIGM:
                return "sigm"
            elif self == stock.STOCK.STOCK_SILC:
                return "silc"
            elif self == stock.STOCK.STOCK_SIM:
                return "sim"
            elif self == stock.STOCK.STOCK_SIMO:
                return "simo"
            elif self == stock.STOCK.STOCK_SINA:
                return "sina"
            elif self == stock.STOCK.STOCK_SINO:
                return "sino"
            elif self == stock.STOCK.STOCK_SIR:
                return "sir"
            elif self == stock.STOCK.STOCK_SIRI:
                return "siri"
            elif self == stock.STOCK.STOCK_SITE:
                return "site"
            elif self == stock.STOCK.STOCK_SITO:
                return "sito"
            elif self == stock.STOCK.STOCK_SIVB:
                return "sivb"
            elif self == stock.STOCK.STOCK_SIVBO:
                return "sivbo"
            elif self == stock.STOCK.STOCK_SIX:
                return "six"
            elif self == stock.STOCK.STOCK_SJI:
                return "sji"
            elif self == stock.STOCK.STOCK_SJM:
                return "sjm"
            elif self == stock.STOCK.STOCK_SJR:
                return "sjr"
            elif self == stock.STOCK.STOCK_SJT:
                return "sjt"
            elif self == stock.STOCK.STOCK_SJW:
                return "sjw"
            elif self == stock.STOCK.STOCK_SKIS:
                return "skis"
            elif self == stock.STOCK.STOCK_SKLN:
                return "skln"
            elif self == stock.STOCK.STOCK_SKM:
                return "skm"
            elif self == stock.STOCK.STOCK_SKT:
                return "skt"
            elif self == stock.STOCK.STOCK_SKX:
                return "skx"
            elif self == stock.STOCK.STOCK_SKY:
                return "sky"
            elif self == stock.STOCK.STOCK_SKYS:
                return "skys"
            elif self == stock.STOCK.STOCK_SKYW:
                return "skyw"
            elif self == stock.STOCK.STOCK_SLAB:
                return "slab"
            elif self == stock.STOCK.STOCK_SLB:
                return "slb"
            elif self == stock.STOCK.STOCK_SLCA:
                return "slca"
            elif self == stock.STOCK.STOCK_SLCT:
                return "slct"
            elif self == stock.STOCK.STOCK_SLD:
                return "sld"
            elif self == stock.STOCK.STOCK_SLDA:
                return "slda"
            elif self == stock.STOCK.STOCK_SLF:
                return "slf"
            elif self == stock.STOCK.STOCK_SLG:
                return "slg"
            elif self == stock.STOCK.STOCK_SLGN:
                return "slgn"
            elif self == stock.STOCK.STOCK_SLG_I:
                return "slg_i"
            elif self == stock.STOCK.STOCK_SLIM:
                return "slim"
            elif self == stock.STOCK.STOCK_SLM:
                return "slm"
            elif self == stock.STOCK.STOCK_SLMBP:
                return "slmbp"
            elif self == stock.STOCK.STOCK_SLNO:
                return "slno"
            elif self == stock.STOCK.STOCK_SLNOW:
                return "slnow"
            elif self == stock.STOCK.STOCK_SLP:
                return "slp"
            elif self == stock.STOCK.STOCK_SLRA:
                return "slra"
            elif self == stock.STOCK.STOCK_SLRC:
                return "slrc"
            elif self == stock.STOCK.STOCK_SLTB:
                return "sltb"
            elif self == stock.STOCK.STOCK_SM:
                return "sm"
            elif self == stock.STOCK.STOCK_SMBC:
                return "smbc"
            elif self == stock.STOCK.STOCK_SMBK:
                return "smbk"
            elif self == stock.STOCK.STOCK_SMCI:
                return "smci"
            elif self == stock.STOCK.STOCK_SMCP:
                return "smcp"
            elif self == stock.STOCK.STOCK_SMED:
                return "smed"
            elif self == stock.STOCK.STOCK_SMFG:
                return "smfg"
            elif self == stock.STOCK.STOCK_SMG:
                return "smg"
            elif self == stock.STOCK.STOCK_SMHD:
                return "smhd"
            elif self == stock.STOCK.STOCK_SMHI:
                return "smhi"
            elif self == stock.STOCK.STOCK_SMI:
                return "smi"
            elif self == stock.STOCK.STOCK_SMIN:
                return "smin"
            elif self == stock.STOCK.STOCK_SMIT:
                return "smit"
            elif self == stock.STOCK.STOCK_SMLP:
                return "smlp"
            elif self == stock.STOCK.STOCK_SMM:
                return "smm"
            elif self == stock.STOCK.STOCK_SMMD:
                return "smmd"
            elif self == stock.STOCK.STOCK_SMMF:
                return "smmf"
            elif self == stock.STOCK.STOCK_SMMT:
                return "smmt"
            elif self == stock.STOCK.STOCK_SMMV:
                return "smmv"
            elif self == stock.STOCK.STOCK_SMP:
                return "smp"
            elif self == stock.STOCK.STOCK_SMPL:
                return "smpl"
            elif self == stock.STOCK.STOCK_SMPLW:
                return "smplw"
            elif self == stock.STOCK.STOCK_SMRT:
                return "smrt"
            elif self == stock.STOCK.STOCK_SMSI:
                return "smsi"
            elif self == stock.STOCK.STOCK_SMTC:
                return "smtc"
            elif self == stock.STOCK.STOCK_SMTS:
                return "smts"
            elif self == stock.STOCK.STOCK_SMTX:
                return "smtx"
            elif self == stock.STOCK.STOCK_SN:
                return "sn"
            elif self == stock.STOCK.STOCK_SNA:
                return "sna"
            elif self == stock.STOCK.STOCK_SNAK:
                return "snak"
            elif self == stock.STOCK.STOCK_SNAP:
                return "snap"
            elif self == stock.STOCK.STOCK_SNBC:
                return "snbc"
            elif self == stock.STOCK.STOCK_SNBR:
                return "snbr"
            elif self == stock.STOCK.STOCK_SNC:
                return "snc"
            elif self == stock.STOCK.STOCK_SNCR:
                return "sncr"
            elif self == stock.STOCK.STOCK_SND:
                return "snd"
            elif self == stock.STOCK.STOCK_SNDE:
                return "snde"
            elif self == stock.STOCK.STOCK_SNDR:
                return "sndr"
            elif self == stock.STOCK.STOCK_SNDX:
                return "sndx"
            elif self == stock.STOCK.STOCK_SNE:
                return "sne"
            elif self == stock.STOCK.STOCK_SNES:
                return "snes"
            elif self == stock.STOCK.STOCK_SNFCA:
                return "snfca"
            elif self == stock.STOCK.STOCK_SNGX:
                return "sngx"
            elif self == stock.STOCK.STOCK_SNGXW:
                return "sngxw"
            elif self == stock.STOCK.STOCK_SNH:
                return "snh"
            elif self == stock.STOCK.STOCK_SNHNI:
                return "snhni"
            elif self == stock.STOCK.STOCK_SNHNL:
                return "snhnl"
            elif self == stock.STOCK.STOCK_SNHY:
                return "snhy"
            elif self == stock.STOCK.STOCK_SNI:
                return "sni"
            elif self == stock.STOCK.STOCK_SNMP:
                return "snmp"
            elif self == stock.STOCK.STOCK_SNMX:
                return "snmx"
            elif self == stock.STOCK.STOCK_SNN:
                return "snn"
            elif self == stock.STOCK.STOCK_SNNA:
                return "snna"
            elif self == stock.STOCK.STOCK_SNOA:
                return "snoa"
            elif self == stock.STOCK.STOCK_SNOAW:
                return "snoaw"
            elif self == stock.STOCK.STOCK_SNP:
                return "snp"
            elif self == stock.STOCK.STOCK_SNPS:
                return "snps"
            elif self == stock.STOCK.STOCK_SNR:
                return "snr"
            elif self == stock.STOCK.STOCK_SNSR:
                return "snsr"
            elif self == stock.STOCK.STOCK_SNSS:
                return "snss"
            elif self == stock.STOCK.STOCK_SNV:
                return "snv"
            elif self == stock.STOCK.STOCK_SNV_C:
                return "snv_c"
            elif self == stock.STOCK.STOCK_SNX:
                return "snx"
            elif self == stock.STOCK.STOCK_SNY:
                return "sny"
            elif self == stock.STOCK.STOCK_SO:
                return "so"
            elif self == stock.STOCK.STOCK_SODA:
                return "soda"
            elif self == stock.STOCK.STOCK_SOFO:
                return "sofo"
            elif self == stock.STOCK.STOCK_SOGO:
                return "sogo"
            elif self == stock.STOCK.STOCK_SOHO:
                return "soho"
            elif self == stock.STOCK.STOCK_SOHOB:
                return "sohob"
            elif self == stock.STOCK.STOCK_SOHOM:
                return "sohom"
            elif self == stock.STOCK.STOCK_SOHOO:
                return "sohoo"
            elif self == stock.STOCK.STOCK_SOHU:
                return "sohu"
            elif self == stock.STOCK.STOCK_SOI:
                return "soi"
            elif self == stock.STOCK.STOCK_SOJA:
                return "soja"
            elif self == stock.STOCK.STOCK_SOJB:
                return "sojb"
            elif self == stock.STOCK.STOCK_SOL:
                return "sol"
            elif self == stock.STOCK.STOCK_SON:
                return "son"
            elif self == stock.STOCK.STOCK_SONA:
                return "sona"
            elif self == stock.STOCK.STOCK_SONC:
                return "sonc"
            elif self == stock.STOCK.STOCK_SONS:
                return "sons"
            elif self == stock.STOCK.STOCK_SOR:
                return "sor"
            elif self == stock.STOCK.STOCK_SORL:
                return "sorl"
            elif self == stock.STOCK.STOCK_SOVB:
                return "sovb"
            elif self == stock.STOCK.STOCK_SOV_C:
                return "sov_c"
            elif self == stock.STOCK.STOCK_SP:
                return "sp"
            elif self == stock.STOCK.STOCK_SPA:
                return "spa"
            elif self == stock.STOCK.STOCK_SPAB:
                return "spab"
            elif self == stock.STOCK.STOCK_SPAR:
                return "spar"
            elif self == stock.STOCK.STOCK_SPB:
                return "spb"
            elif self == stock.STOCK.STOCK_SPCB:
                return "spcb"
            elif self == stock.STOCK.STOCK_SPDN:
                return "spdn"
            elif self == stock.STOCK.STOCK_SPDW:
                return "spdw"
            elif self == stock.STOCK.STOCK_SPE:
                return "spe"
            elif self == stock.STOCK.STOCK_SPEM:
                return "spem"
            elif self == stock.STOCK.STOCK_SPEX:
                return "spex"
            elif self == stock.STOCK.STOCK_SPE_B:
                return "spe_b"
            elif self == stock.STOCK.STOCK_SPG:
                return "spg"
            elif self == stock.STOCK.STOCK_SPGI:
                return "spgi"
            elif self == stock.STOCK.STOCK_SPG_J:
                return "spg_j"
            elif self == stock.STOCK.STOCK_SPH:
                return "sph"
            elif self == stock.STOCK.STOCK_SPHS:
                return "sphs"
            elif self == stock.STOCK.STOCK_SPI:
                return "spi"
            elif self == stock.STOCK.STOCK_SPIB:
                return "spib"
            elif self == stock.STOCK.STOCK_SPIL:
                return "spil"
            elif self == stock.STOCK.STOCK_SPKE:
                return "spke"
            elif self == stock.STOCK.STOCK_SPKEP:
                return "spkep"
            elif self == stock.STOCK.STOCK_SPLB:
                return "splb"
            elif self == stock.STOCK.STOCK_SPLG:
                return "splg"
            elif self == stock.STOCK.STOCK_SPLK:
                return "splk"
            elif self == stock.STOCK.STOCK_SPLP:
                return "splp"
            elif self == stock.STOCK.STOCK_SPLP_A:
                return "splp_a"
            elif self == stock.STOCK.STOCK_SPLP_T:
                return "splp_t"
            elif self == stock.STOCK.STOCK_SPMD:
                return "spmd"
            elif self == stock.STOCK.STOCK_SPMO:
                return "spmo"
            elif self == stock.STOCK.STOCK_SPMV:
                return "spmv"
            elif self == stock.STOCK.STOCK_SPN:
                return "spn"
            elif self == stock.STOCK.STOCK_SPNE:
                return "spne"
            elif self == stock.STOCK.STOCK_SPNS:
                return "spns"
            elif self == stock.STOCK.STOCK_SPOK:
                return "spok"
            elif self == stock.STOCK.STOCK_SPPI:
                return "sppi"
            elif self == stock.STOCK.STOCK_SPPP:
                return "sppp"
            elif self == stock.STOCK.STOCK_SPR:
                return "spr"
            elif self == stock.STOCK.STOCK_SPRO:
                return "spro"
            elif self == stock.STOCK.STOCK_SPRT:
                return "sprt"
            elif self == stock.STOCK.STOCK_SPSB:
                return "spsb"
            elif self == stock.STOCK.STOCK_SPSC:
                return "spsc"
            elif self == stock.STOCK.STOCK_SPSM:
                return "spsm"
            elif self == stock.STOCK.STOCK_SPTL:
                return "sptl"
            elif self == stock.STOCK.STOCK_SPTM:
                return "sptm"
            elif self == stock.STOCK.STOCK_SPTN:
                return "sptn"
            elif self == stock.STOCK.STOCK_SPTS:
                return "spts"
            elif self == stock.STOCK.STOCK_SPUN:
                return "spun"
            elif self == stock.STOCK.STOCK_SPVM:
                return "spvm"
            elif self == stock.STOCK.STOCK_SPVU:
                return "spvu"
            elif self == stock.STOCK.STOCK_SPWH:
                return "spwh"
            elif self == stock.STOCK.STOCK_SPWR:
                return "spwr"
            elif self == stock.STOCK.STOCK_SPXC:
                return "spxc"
            elif self == stock.STOCK.STOCK_SPXE:
                return "spxe"
            elif self == stock.STOCK.STOCK_SPXN:
                return "spxn"
            elif self == stock.STOCK.STOCK_SPXT:
                return "spxt"
            elif self == stock.STOCK.STOCK_SPXV:
                return "spxv"
            elif self == stock.STOCK.STOCK_SPXX:
                return "spxx"
            elif self == stock.STOCK.STOCK_SPYD:
                return "spyd"
            elif self == stock.STOCK.STOCK_SPYX:
                return "spyx"
            elif self == stock.STOCK.STOCK_SQ:
                return "sq"
            elif self == stock.STOCK.STOCK_SQBG:
                return "sqbg"
            elif self == stock.STOCK.STOCK_SQLV:
                return "sqlv"
            elif self == stock.STOCK.STOCK_SQM:
                return "sqm"
            elif self == stock.STOCK.STOCK_SQNS:
                return "sqns"
            elif self == stock.STOCK.STOCK_SQZZ:
                return "sqzz"
            elif self == stock.STOCK.STOCK_SR:
                return "sr"
            elif self == stock.STOCK.STOCK_SRAX:
                return "srax"
            elif self == stock.STOCK.STOCK_SRC:
                return "src"
            elif self == stock.STOCK.STOCK_SRCE:
                return "srce"
            elif self == stock.STOCK.STOCK_SRCI:
                return "srci"
            elif self == stock.STOCK.STOCK_SRCL:
                return "srcl"
            elif self == stock.STOCK.STOCK_SRCLP:
                return "srclp"
            elif self == stock.STOCK.STOCK_SRC_A:
                return "src_a"
            elif self == stock.STOCK.STOCK_SRDX:
                return "srdx"
            elif self == stock.STOCK.STOCK_SRE:
                return "sre"
            elif self == stock.STOCK.STOCK_SREV:
                return "srev"
            elif self == stock.STOCK.STOCK_SRF:
                return "srf"
            elif self == stock.STOCK.STOCK_SRG:
                return "srg"
            elif self == stock.STOCK.STOCK_SRI:
                return "sri"
            elif self == stock.STOCK.STOCK_SRLP:
                return "srlp"
            elif self == stock.STOCK.STOCK_SRNE:
                return "srne"
            elif self == stock.STOCK.STOCK_SRPT:
                return "srpt"
            elif self == stock.STOCK.STOCK_SRRA:
                return "srra"
            elif self == stock.STOCK.STOCK_SRT:
                return "srt"
            elif self == stock.STOCK.STOCK_SRTS:
                return "srts"
            elif self == stock.STOCK.STOCK_SRTSW:
                return "srtsw"
            elif self == stock.STOCK.STOCK_SRUN:
                return "srun"
            elif self == stock.STOCK.STOCK_SRUNU:
                return "srunu"
            elif self == stock.STOCK.STOCK_SRUNW:
                return "srunw"
            elif self == stock.STOCK.STOCK_SRV:
                return "srv"
            elif self == stock.STOCK.STOCK_SRVA:
                return "srva"
            elif self == stock.STOCK.STOCK_SSB:
                return "ssb"
            elif self == stock.STOCK.STOCK_SSBI:
                return "ssbi"
            elif self == stock.STOCK.STOCK_SSC:
                return "ssc"
            elif self == stock.STOCK.STOCK_SSD:
                return "ssd"
            elif self == stock.STOCK.STOCK_SSFN:
                return "ssfn"
            elif self == stock.STOCK.STOCK_SSI:
                return "ssi"
            elif self == stock.STOCK.STOCK_SSKN:
                return "sskn"
            elif self == stock.STOCK.STOCK_SSL:
                return "ssl"
            elif self == stock.STOCK.STOCK_SSN:
                return "ssn"
            elif self == stock.STOCK.STOCK_SSNC:
                return "ssnc"
            elif self == stock.STOCK.STOCK_SSNI:
                return "ssni"
            elif self == stock.STOCK.STOCK_SSNT:
                return "ssnt"
            elif self == stock.STOCK.STOCK_SSP:
                return "ssp"
            elif self == stock.STOCK.STOCK_SSRM:
                return "ssrm"
            elif self == stock.STOCK.STOCK_SSTI:
                return "ssti"
            elif self == stock.STOCK.STOCK_SSTK:
                return "sstk"
            elif self == stock.STOCK.STOCK_SSW:
                return "ssw"
            elif self == stock.STOCK.STOCK_SSWA:
                return "sswa"
            elif self == stock.STOCK.STOCK_SSWN:
                return "sswn"
            elif self == stock.STOCK.STOCK_SSW_D:
                return "ssw_d"
            elif self == stock.STOCK.STOCK_SSW_E:
                return "ssw_e"
            elif self == stock.STOCK.STOCK_SSW_G:
                return "ssw_g"
            elif self == stock.STOCK.STOCK_SSW_H:
                return "ssw_h"
            elif self == stock.STOCK.STOCK_SSY:
                return "ssy"
            elif self == stock.STOCK.STOCK_SSYS:
                return "ssys"
            elif self == stock.STOCK.STOCK_ST:
                return "st"
            elif self == stock.STOCK.STOCK_STAA:
                return "staa"
            elif self == stock.STOCK.STOCK_STAF:
                return "staf"
            elif self == stock.STOCK.STOCK_STAG:
                return "stag"
            elif self == stock.STOCK.STOCK_STAG_B:
                return "stag_b"
            elif self == stock.STOCK.STOCK_STAG_C:
                return "stag_c"
            elif self == stock.STOCK.STOCK_STAR:
                return "star"
            elif self == stock.STOCK.STOCK_STAR_D:
                return "star_d"
            elif self == stock.STOCK.STOCK_STAR_E:
                return "star_e"
            elif self == stock.STOCK.STOCK_STAR_F:
                return "star_f"
            elif self == stock.STOCK.STOCK_STAR_G:
                return "star_g"
            elif self == stock.STOCK.STOCK_STAR_I:
                return "star_i"
            elif self == stock.STOCK.STOCK_STAY:
                return "stay"
            elif self == stock.STOCK.STOCK_STB:
                return "stb"
            elif self == stock.STOCK.STOCK_STBA:
                return "stba"
            elif self == stock.STOCK.STOCK_STBZ:
                return "stbz"
            elif self == stock.STOCK.STOCK_STC:
                return "stc"
            elif self == stock.STOCK.STOCK_STDY:
                return "stdy"
            elif self == stock.STOCK.STOCK_STE:
                return "ste"
            elif self == stock.STOCK.STOCK_STFC:
                return "stfc"
            elif self == stock.STOCK.STOCK_STI-WS-A:
                return "sti-ws-a"
            elif self == stock.STOCK.STOCK_STI-WS-B:
                return "sti-ws-b"
            elif self == stock.STOCK.STOCK_STI:
                return "sti"
            elif self == stock.STOCK.STOCK_STI_A:
                return "sti_a"
            elif self == stock.STOCK.STOCK_STI_E:
                return "sti_e"
            elif self == stock.STOCK.STOCK_STK:
                return "stk"
            elif self == stock.STOCK.STOCK_STKL:
                return "stkl"
            elif self == stock.STOCK.STOCK_STKS:
                return "stks"
            elif self == stock.STOCK.STOCK_STL:
                return "stl"
            elif self == stock.STOCK.STOCK_STLD:
                return "stld"
            elif self == stock.STOCK.STOCK_STLR:
                return "stlr"
            elif self == stock.STOCK.STOCK_STLRU:
                return "stlru"
            elif self == stock.STOCK.STOCK_STLRW:
                return "stlrw"
            elif self == stock.STOCK.STOCK_STLY:
                return "stly"
            elif self == stock.STOCK.STOCK_STL_A:
                return "stl_a"
            elif self == stock.STOCK.STOCK_STM:
                return "stm"
            elif self == stock.STOCK.STOCK_STML:
                return "stml"
            elif self == stock.STOCK.STOCK_STMP:
                return "stmp"
            elif self == stock.STOCK.STOCK_STN:
                return "stn"
            elif self == stock.STOCK.STOCK_STNG:
                return "stng"
            elif self == stock.STOCK.STOCK_STNL:
                return "stnl"
            elif self == stock.STOCK.STOCK_STNLU:
                return "stnlu"
            elif self == stock.STOCK.STOCK_STO:
                return "sto"
            elif self == stock.STOCK.STOCK_STON:
                return "ston"
            elif self == stock.STOCK.STOCK_STOR:
                return "stor"
            elif self == stock.STOCK.STOCK_STOT:
                return "stot"
            elif self == stock.STOCK.STOCK_STPP:
                return "stpp"
            elif self == stock.STOCK.STOCK_STRA:
                return "stra"
            elif self == stock.STOCK.STOCK_STRL:
                return "strl"
            elif self == stock.STOCK.STOCK_STRM:
                return "strm"
            elif self == stock.STOCK.STOCK_STRP:
                return "strp"
            elif self == stock.STOCK.STOCK_STRS:
                return "strs"
            elif self == stock.STOCK.STOCK_STRT:
                return "strt"
            elif self == stock.STOCK.STOCK_STT:
                return "stt"
            elif self == stock.STOCK.STOCK_STT_C:
                return "stt_c"
            elif self == stock.STOCK.STOCK_STT_D:
                return "stt_d"
            elif self == stock.STOCK.STOCK_STT_E:
                return "stt_e"
            elif self == stock.STOCK.STOCK_STT_G:
                return "stt_g"
            elif self == stock.STOCK.STOCK_STWD:
                return "stwd"
            elif self == stock.STOCK.STOCK_STX:
                return "stx"
            elif self == stock.STOCK.STOCK_STZ-B:
                return "stz-b"
            elif self == stock.STOCK.STOCK_STZ:
                return "stz"
            elif self == stock.STOCK.STOCK_SU:
                return "su"
            elif self == stock.STOCK.STOCK_SUI:
                return "sui"
            elif self == stock.STOCK.STOCK_SUI_A:
                return "sui_a"
            elif self == stock.STOCK.STOCK_SUM:
                return "sum"
            elif self == stock.STOCK.STOCK_SUMR:
                return "sumr"
            elif self == stock.STOCK.STOCK_SUN:
                return "sun"
            elif self == stock.STOCK.STOCK_SUNS:
                return "suns"
            elif self == stock.STOCK.STOCK_SUNW:
                return "sunw"
            elif self == stock.STOCK.STOCK_SUP:
                return "sup"
            elif self == stock.STOCK.STOCK_SUPN:
                return "supn"
            elif self == stock.STOCK.STOCK_SUPV:
                return "supv"
            elif self == stock.STOCK.STOCK_SUSA:
                return "susa"
            elif self == stock.STOCK.STOCK_SUSB:
                return "susb"
            elif self == stock.STOCK.STOCK_SUSC:
                return "susc"
            elif self == stock.STOCK.STOCK_SVA:
                return "sva"
            elif self == stock.STOCK.STOCK_SVBI:
                return "svbi"
            elif self == stock.STOCK.STOCK_SVM:
                return "svm"
            elif self == stock.STOCK.STOCK_SVRA:
                return "svra"
            elif self == stock.STOCK.STOCK_SVT:
                return "svt"
            elif self == stock.STOCK.STOCK_SVU:
                return "svu"
            elif self == stock.STOCK.STOCK_SVVC:
                return "svvc"
            elif self == stock.STOCK.STOCK_SWCH:
                return "swch"
            elif self == stock.STOCK.STOCK_SWIN:
                return "swin"
            elif self == stock.STOCK.STOCK_SWIR:
                return "swir"
            elif self == stock.STOCK.STOCK_SWJ:
                return "swj"
            elif self == stock.STOCK.STOCK_SWK:
                return "swk"
            elif self == stock.STOCK.STOCK_SWKS:
                return "swks"
            elif self == stock.STOCK.STOCK_SWM:
                return "swm"
            elif self == stock.STOCK.STOCK_SWN:
                return "swn"
            elif self == stock.STOCK.STOCK_SWNC:
                return "swnc"
            elif self == stock.STOCK.STOCK_SWP:
                return "swp"
            elif self == stock.STOCK.STOCK_SWX:
                return "swx"
            elif self == stock.STOCK.STOCK_SWZ:
                return "swz"
            elif self == stock.STOCK.STOCK_SXC:
                return "sxc"
            elif self == stock.STOCK.STOCK_SXCP:
                return "sxcp"
            elif self == stock.STOCK.STOCK_SXE:
                return "sxe"
            elif self == stock.STOCK.STOCK_SXI:
                return "sxi"
            elif self == stock.STOCK.STOCK_SXT:
                return "sxt"
            elif self == stock.STOCK.STOCK_SYBT:
                return "sybt"
            elif self == stock.STOCK.STOCK_SYBX:
                return "sybx"
            elif self == stock.STOCK.STOCK_SYF:
                return "syf"
            elif self == stock.STOCK.STOCK_SYK:
                return "syk"
            elif self == stock.STOCK.STOCK_SYKE:
                return "syke"
            elif self == stock.STOCK.STOCK_SYMC:
                return "symc"
            elif self == stock.STOCK.STOCK_SYMX:
                return "symx"
            elif self == stock.STOCK.STOCK_SYN:
                return "syn"
            elif self == stock.STOCK.STOCK_SYNA:
                return "syna"
            elif self == stock.STOCK.STOCK_SYNC:
                return "sync"
            elif self == stock.STOCK.STOCK_SYNL:
                return "synl"
            elif self == stock.STOCK.STOCK_SYNT:
                return "synt"
            elif self == stock.STOCK.STOCK_SYPR:
                return "sypr"
            elif self == stock.STOCK.STOCK_SYRS:
                return "syrs"
            elif self == stock.STOCK.STOCK_SYT:
                return "syt"
            elif self == stock.STOCK.STOCK_SYX:
                return "syx"
            elif self == stock.STOCK.STOCK_SYY:
                return "syy"
            elif self == stock.STOCK.STOCK_SZC:
                return "szc"
            elif self == stock.STOCK.STOCK_T:
                return "t"
            elif self == stock.STOCK.STOCK_TA:
                return "ta"
            elif self == stock.STOCK.STOCK_TAC:
                return "tac"
            elif self == stock.STOCK.STOCK_TACO:
                return "taco"
            elif self == stock.STOCK.STOCK_TACOW:
                return "tacow"
            elif self == stock.STOCK.STOCK_TACT:
                return "tact"
            elif self == stock.STOCK.STOCK_TAHO:
                return "taho"
            elif self == stock.STOCK.STOCK_TAIL:
                return "tail"
            elif self == stock.STOCK.STOCK_TAIT:
                return "tait"
            elif self == stock.STOCK.STOCK_TAL:
                return "tal"
            elif self == stock.STOCK.STOCK_TANH:
                return "tanh"
            elif self == stock.STOCK.STOCK_TANNI:
                return "tanni"
            elif self == stock.STOCK.STOCK_TANNL:
                return "tannl"
            elif self == stock.STOCK.STOCK_TANNZ:
                return "tannz"
            elif self == stock.STOCK.STOCK_TAP-A:
                return "tap-a"
            elif self == stock.STOCK.STOCK_TAP:
                return "tap"
            elif self == stock.STOCK.STOCK_TAPR:
                return "tapr"
            elif self == stock.STOCK.STOCK_TARO:
                return "taro"
            elif self == stock.STOCK.STOCK_TAST:
                return "tast"
            elif self == stock.STOCK.STOCK_TAT:
                return "tat"
            elif self == stock.STOCK.STOCK_TATT:
                return "tatt"
            elif self == stock.STOCK.STOCK_TAX:
                return "tax"
            elif self == stock.STOCK.STOCK_TAXR:
                return "taxr"
            elif self == stock.STOCK.STOCK_TAYD:
                return "tayd"
            elif self == stock.STOCK.STOCK_TBB:
                return "tbb"
            elif self == stock.STOCK.STOCK_TBBK:
                return "tbbk"
            elif self == stock.STOCK.STOCK_TBI:
                return "tbi"
            elif self == stock.STOCK.STOCK_TBK:
                return "tbk"
            elif self == stock.STOCK.STOCK_TBLU:
                return "tblu"
            elif self == stock.STOCK.STOCK_TBNK:
                return "tbnk"
            elif self == stock.STOCK.STOCK_TBPH:
                return "tbph"
            elif self == stock.STOCK.STOCK_TCAP:
                return "tcap"
            elif self == stock.STOCK.STOCK_TCBI:
                return "tcbi"
            elif self == stock.STOCK.STOCK_TCBIL:
                return "tcbil"
            elif self == stock.STOCK.STOCK_TCBIP:
                return "tcbip"
            elif self == stock.STOCK.STOCK_TCBIW:
                return "tcbiw"
            elif self == stock.STOCK.STOCK_TCBK:
                return "tcbk"
            elif self == stock.STOCK.STOCK_TCCA:
                return "tcca"
            elif self == stock.STOCK.STOCK_TCCB:
                return "tccb"
            elif self == stock.STOCK.STOCK_TCCO:
                return "tcco"
            elif self == stock.STOCK.STOCK_TCF-WS:
                return "tcf-ws"
            elif self == stock.STOCK.STOCK_TCF:
                return "tcf"
            elif self == stock.STOCK.STOCK_TCFC:
                return "tcfc"
            elif self == stock.STOCK.STOCK_TCF_B-CL:
                return "tcf_b-cl"
            elif self == stock.STOCK.STOCK_TCF_C:
                return "tcf_c"
            elif self == stock.STOCK.STOCK_TCF_D:
                return "tcf_d"
            elif self == stock.STOCK.STOCK_TCGP:
                return "tcgp"
            elif self == stock.STOCK.STOCK_TCHF:
                return "tchf"
            elif self == stock.STOCK.STOCK_TCI:
                return "tci"
            elif self == stock.STOCK.STOCK_TCMD:
                return "tcmd"
            elif self == stock.STOCK.STOCK_TCO:
                return "tco"
            elif self == stock.STOCK.STOCK_TCON:
                return "tcon"
            elif self == stock.STOCK.STOCK_TCO_J:
                return "tco_j"
            elif self == stock.STOCK.STOCK_TCO_K:
                return "tco_k"
            elif self == stock.STOCK.STOCK_TCP:
                return "tcp"
            elif self == stock.STOCK.STOCK_TCPC:
                return "tcpc"
            elif self == stock.STOCK.STOCK_TCRD:
                return "tcrd"
            elif self == stock.STOCK.STOCK_TCRX:
                return "tcrx"
            elif self == stock.STOCK.STOCK_TCRZ:
                return "tcrz"
            elif self == stock.STOCK.STOCK_TCS:
                return "tcs"
            elif self == stock.STOCK.STOCK_TCTL:
                return "tctl"
            elif self == stock.STOCK.STOCK_TCX:
                return "tcx"
            elif self == stock.STOCK.STOCK_TD:
                return "td"
            elif self == stock.STOCK.STOCK_TDA:
                return "tda"
            elif self == stock.STOCK.STOCK_TDC:
                return "tdc"
            elif self == stock.STOCK.STOCK_TDE:
                return "tde"
            elif self == stock.STOCK.STOCK_TDF:
                return "tdf"
            elif self == stock.STOCK.STOCK_TDG:
                return "tdg"
            elif self == stock.STOCK.STOCK_TDI:
                return "tdi"
            elif self == stock.STOCK.STOCK_TDJ:
                return "tdj"
            elif self == stock.STOCK.STOCK_TDOC:
                return "tdoc"
            elif self == stock.STOCK.STOCK_TDS:
                return "tds"
            elif self == stock.STOCK.STOCK_TDW-WS-A:
                return "tdw-ws-a"
            elif self == stock.STOCK.STOCK_TDW-WS-B:
                return "tdw-ws-b"
            elif self == stock.STOCK.STOCK_TDW:
                return "tdw"
            elif self == stock.STOCK.STOCK_TDY:
                return "tdy"
            elif self == stock.STOCK.STOCK_TEAM:
                return "team"
            elif self == stock.STOCK.STOCK_TEAR:
                return "tear"
            elif self == stock.STOCK.STOCK_TECD:
                return "tecd"
            elif self == stock.STOCK.STOCK_TECH:
                return "tech"
            elif self == stock.STOCK.STOCK_TECK:
                return "teck"
            elif self == stock.STOCK.STOCK_TEDU:
                return "tedu"
            elif self == stock.STOCK.STOCK_TEF:
                return "tef"
            elif self == stock.STOCK.STOCK_TEGP:
                return "tegp"
            elif self == stock.STOCK.STOCK_TEI:
                return "tei"
            elif self == stock.STOCK.STOCK_TEL:
                return "tel"
            elif self == stock.STOCK.STOCK_TELL:
                return "tell"
            elif self == stock.STOCK.STOCK_TEN:
                return "ten"
            elif self == stock.STOCK.STOCK_TENX:
                return "tenx"
            elif self == stock.STOCK.STOCK_TEO:
                return "teo"
            elif self == stock.STOCK.STOCK_TEP:
                return "tep"
            elif self == stock.STOCK.STOCK_TER:
                return "ter"
            elif self == stock.STOCK.STOCK_TERM:
                return "term"
            elif self == stock.STOCK.STOCK_TERP:
                return "terp"
            elif self == stock.STOCK.STOCK_TESO:
                return "teso"
            elif self == stock.STOCK.STOCK_TESS:
                return "tess"
            elif self == stock.STOCK.STOCK_TETF:
                return "tetf"
            elif self == stock.STOCK.STOCK_TEUM:
                return "teum"
            elif self == stock.STOCK.STOCK_TEVA:
                return "teva"
            elif self == stock.STOCK.STOCK_TEX:
                return "tex"
            elif self == stock.STOCK.STOCK_TFSL:
                return "tfsl"
            elif self == stock.STOCK.STOCK_TFX:
                return "tfx"
            elif self == stock.STOCK.STOCK_TG:
                return "tg"
            elif self == stock.STOCK.STOCK_TGA:
                return "tga"
            elif self == stock.STOCK.STOCK_TGB:
                return "tgb"
            elif self == stock.STOCK.STOCK_TGC:
                return "tgc"
            elif self == stock.STOCK.STOCK_TGEN:
                return "tgen"
            elif self == stock.STOCK.STOCK_TGH:
                return "tgh"
            elif self == stock.STOCK.STOCK_TGI:
                return "tgi"
            elif self == stock.STOCK.STOCK_TGLS:
                return "tgls"
            elif self == stock.STOCK.STOCK_TGNA:
                return "tgna"
            elif self == stock.STOCK.STOCK_TGP:
                return "tgp"
            elif self == stock.STOCK.STOCK_TGP_A:
                return "tgp_a"
            elif self == stock.STOCK.STOCK_TGP_B:
                return "tgp_b"
            elif self == stock.STOCK.STOCK_TGS:
                return "tgs"
            elif self == stock.STOCK.STOCK_TGT:
                return "tgt"
            elif self == stock.STOCK.STOCK_TGTX:
                return "tgtx"
            elif self == stock.STOCK.STOCK_THC:
                return "thc"
            elif self == stock.STOCK.STOCK_THFF:
                return "thff"
            elif self == stock.STOCK.STOCK_THG:
                return "thg"
            elif self == stock.STOCK.STOCK_THGA:
                return "thga"
            elif self == stock.STOCK.STOCK_THM:
                return "thm"
            elif self == stock.STOCK.STOCK_THO:
                return "tho"
            elif self == stock.STOCK.STOCK_THQ:
                return "thq"
            elif self == stock.STOCK.STOCK_THR:
                return "thr"
            elif self == stock.STOCK.STOCK_THRM:
                return "thrm"
            elif self == stock.STOCK.STOCK_THS:
                return "ths"
            elif self == stock.STOCK.STOCK_THST:
                return "thst"
            elif self == stock.STOCK.STOCK_THW:
                return "thw"
            elif self == stock.STOCK.STOCK_TI-A:
                return "ti-a"
            elif self == stock.STOCK.STOCK_TI:
                return "ti"
            elif self == stock.STOCK.STOCK_TICC:
                return "ticc"
            elif self == stock.STOCK.STOCK_TICCL:
                return "ticcl"
            elif self == stock.STOCK.STOCK_TIER:
                return "tier"
            elif self == stock.STOCK.STOCK_TIF:
                return "tif"
            elif self == stock.STOCK.STOCK_TIG:
                return "tig"
            elif self == stock.STOCK.STOCK_TIK:
                return "tik"
            elif self == stock.STOCK.STOCK_TIL:
                return "til"
            elif self == stock.STOCK.STOCK_TILE:
                return "tile"
            elif self == stock.STOCK.STOCK_TIME:
                return "time"
            elif self == stock.STOCK.STOCK_TIPT:
                return "tipt"
            elif self == stock.STOCK.STOCK_TIS:
                return "tis"
            elif self == stock.STOCK.STOCK_TISA:
                return "tisa"
            elif self == stock.STOCK.STOCK_TISI:
                return "tisi"
            elif self == stock.STOCK.STOCK_TITN:
                return "titn"
            elif self == stock.STOCK.STOCK_TIVO:
                return "tivo"
            elif self == stock.STOCK.STOCK_TJX:
                return "tjx"
            elif self == stock.STOCK.STOCK_TK:
                return "tk"
            elif self == stock.STOCK.STOCK_TKAT:
                return "tkat"
            elif self == stock.STOCK.STOCK_TKC:
                return "tkc"
            elif self == stock.STOCK.STOCK_TKF:
                return "tkf"
            elif self == stock.STOCK.STOCK_TKR:
                return "tkr"
            elif self == stock.STOCK.STOCK_TLDH:
                return "tldh"
            elif self == stock.STOCK.STOCK_TLEH:
                return "tleh"
            elif self == stock.STOCK.STOCK_TLF:
                return "tlf"
            elif self == stock.STOCK.STOCK_TLGT:
                return "tlgt"
            elif self == stock.STOCK.STOCK_TLI:
                return "tli"
            elif self == stock.STOCK.STOCK_TLK:
                return "tlk"
            elif self == stock.STOCK.STOCK_TLND:
                return "tlnd"
            elif self == stock.STOCK.STOCK_TLP:
                return "tlp"
            elif self == stock.STOCK.STOCK_TLRA:
                return "tlra"
            elif self == stock.STOCK.STOCK_TLRD:
                return "tlrd"
            elif self == stock.STOCK.STOCK_TLYS:
                return "tlys"
            elif self == stock.STOCK.STOCK_TM:
                return "tm"
            elif self == stock.STOCK.STOCK_TMHC:
                return "tmhc"
            elif self == stock.STOCK.STOCK_TMK:
                return "tmk"
            elif self == stock.STOCK.STOCK_TMK_B:
                return "tmk_b"
            elif self == stock.STOCK.STOCK_TMK_C:
                return "tmk_c"
            elif self == stock.STOCK.STOCK_TMO:
                return "tmo"
            elif self == stock.STOCK.STOCK_TMP:
                return "tmp"
            elif self == stock.STOCK.STOCK_TMQ:
                return "tmq"
            elif self == stock.STOCK.STOCK_TMST:
                return "tmst"
            elif self == stock.STOCK.STOCK_TMUS:
                return "tmus"
            elif self == stock.STOCK.STOCK_TMUSP:
                return "tmusp"
            elif self == stock.STOCK.STOCK_TNAV:
                return "tnav"
            elif self == stock.STOCK.STOCK_TNC:
                return "tnc"
            elif self == stock.STOCK.STOCK_TNDM:
                return "tndm"
            elif self == stock.STOCK.STOCK_TNET:
                return "tnet"
            elif self == stock.STOCK.STOCK_TNH:
                return "tnh"
            elif self == stock.STOCK.STOCK_TNK:
                return "tnk"
            elif self == stock.STOCK.STOCK_TNP:
                return "tnp"
            elif self == stock.STOCK.STOCK_TNP_B:
                return "tnp_b"
            elif self == stock.STOCK.STOCK_TNP_C:
                return "tnp_c"
            elif self == stock.STOCK.STOCK_TNP_D:
                return "tnp_d"
            elif self == stock.STOCK.STOCK_TNP_E:
                return "tnp_e"
            elif self == stock.STOCK.STOCK_TNTR:
                return "tntr"
            elif self == stock.STOCK.STOCK_TNXP:
                return "tnxp"
            elif self == stock.STOCK.STOCK_TOCA:
                return "toca"
            elif self == stock.STOCK.STOCK_TOL:
                return "tol"
            elif self == stock.STOCK.STOCK_TOO:
                return "too"
            elif self == stock.STOCK.STOCK_TOO_A:
                return "too_a"
            elif self == stock.STOCK.STOCK_TOO_B:
                return "too_b"
            elif self == stock.STOCK.STOCK_TOPS:
                return "tops"
            elif self == stock.STOCK.STOCK_TORM:
                return "torm"
            elif self == stock.STOCK.STOCK_TOT:
                return "tot"
            elif self == stock.STOCK.STOCK_TOUR:
                return "tour"
            elif self == stock.STOCK.STOCK_TOWN:
                return "town"
            elif self == stock.STOCK.STOCK_TOWR:
                return "towr"
            elif self == stock.STOCK.STOCK_TPB:
                return "tpb"
            elif self == stock.STOCK.STOCK_TPC:
                return "tpc"
            elif self == stock.STOCK.STOCK_TPGE-U:
                return "tpge-u"
            elif self == stock.STOCK.STOCK_TPGE-WS:
                return "tpge-ws"
            elif self == stock.STOCK.STOCK_TPGE:
                return "tpge"
            elif self == stock.STOCK.STOCK_TPGH-U:
                return "tpgh-u"
            elif self == stock.STOCK.STOCK_TPGH-WS:
                return "tpgh-ws"
            elif self == stock.STOCK.STOCK_TPGH:
                return "tpgh"
            elif self == stock.STOCK.STOCK_TPH:
                return "tph"
            elif self == stock.STOCK.STOCK_TPHS:
                return "tphs"
            elif self == stock.STOCK.STOCK_TPIC:
                return "tpic"
            elif self == stock.STOCK.STOCK_TPIV:
                return "tpiv"
            elif self == stock.STOCK.STOCK_TPL:
                return "tpl"
            elif self == stock.STOCK.STOCK_TPOR:
                return "tpor"
            elif self == stock.STOCK.STOCK_TPR:
                return "tpr"
            elif self == stock.STOCK.STOCK_TPRE:
                return "tpre"
            elif self == stock.STOCK.STOCK_TPVG:
                return "tpvg"
            elif self == stock.STOCK.STOCK_TPVY:
                return "tpvy"
            elif self == stock.STOCK.STOCK_TPX:
                return "tpx"
            elif self == stock.STOCK.STOCK_TPYP:
                return "tpyp"
            elif self == stock.STOCK.STOCK_TPZ:
                return "tpz"
            elif self == stock.STOCK.STOCK_TR:
                return "tr"
            elif self == stock.STOCK.STOCK_TRC:
                return "trc"
            elif self == stock.STOCK.STOCK_TRCB:
                return "trcb"
            elif self == stock.STOCK.STOCK_TRCH:
                return "trch"
            elif self == stock.STOCK.STOCK_TRCO:
                return "trco"
            elif self == stock.STOCK.STOCK_TRCR:
                return "trcr"
            elif self == stock.STOCK.STOCK_TRCRW:
                return "trcrw"
            elif self == stock.STOCK.STOCK_TREC:
                return "trec"
            elif self == stock.STOCK.STOCK_TREE:
                return "tree"
            elif self == stock.STOCK.STOCK_TREX:
                return "trex"
            elif self == stock.STOCK.STOCK_TRGP:
                return "trgp"
            elif self == stock.STOCK.STOCK_TRHC:
                return "trhc"
            elif self == stock.STOCK.STOCK_TRI:
                return "tri"
            elif self == stock.STOCK.STOCK_TRIB:
                return "trib"
            elif self == stock.STOCK.STOCK_TRIL:
                return "tril"
            elif self == stock.STOCK.STOCK_TRIP:
                return "trip"
            elif self == stock.STOCK.STOCK_TRK:
                return "trk"
            elif self == stock.STOCK.STOCK_TRMB:
                return "trmb"
            elif self == stock.STOCK.STOCK_TRMK:
                return "trmk"
            elif self == stock.STOCK.STOCK_TRMT:
                return "trmt"
            elif self == stock.STOCK.STOCK_TRN:
                return "trn"
            elif self == stock.STOCK.STOCK_TRNC:
                return "trnc"
            elif self == stock.STOCK.STOCK_TRNO:
                return "trno"
            elif self == stock.STOCK.STOCK_TRNS:
                return "trns"
            elif self == stock.STOCK.STOCK_TROV:
                return "trov"
            elif self == stock.STOCK.STOCK_TROW:
                return "trow"
            elif self == stock.STOCK.STOCK_TROX:
                return "trox"
            elif self == stock.STOCK.STOCK_TRP:
                return "trp"
            elif self == stock.STOCK.STOCK_TRPX:
                return "trpx"
            elif self == stock.STOCK.STOCK_TRQ:
                return "trq"
            elif self == stock.STOCK.STOCK_TRS:
                return "trs"
            elif self == stock.STOCK.STOCK_TRST:
                return "trst"
            elif self == stock.STOCK.STOCK_TRT:
                return "trt"
            elif self == stock.STOCK.STOCK_TRTN:
                return "trtn"
            elif self == stock.STOCK.STOCK_TRTX:
                return "trtx"
            elif self == stock.STOCK.STOCK_TRU:
                return "tru"
            elif self == stock.STOCK.STOCK_TRUE:
                return "true"
            elif self == stock.STOCK.STOCK_TRUP:
                return "trup"
            elif self == stock.STOCK.STOCK_TRV:
                return "trv"
            elif self == stock.STOCK.STOCK_TRVG:
                return "trvg"
            elif self == stock.STOCK.STOCK_TRVN:
                return "trvn"
            elif self == stock.STOCK.STOCK_TRX:
                return "trx"
            elif self == stock.STOCK.STOCK_TRXC:
                return "trxc"
            elif self == stock.STOCK.STOCK_TS:
                return "ts"
            elif self == stock.STOCK.STOCK_TSBK:
                return "tsbk"
            elif self == stock.STOCK.STOCK_TSC:
                return "tsc"
            elif self == stock.STOCK.STOCK_TSCO:
                return "tsco"
            elif self == stock.STOCK.STOCK_TSE:
                return "tse"
            elif self == stock.STOCK.STOCK_TSEM:
                return "tsem"
            elif self == stock.STOCK.STOCK_TSG:
                return "tsg"
            elif self == stock.STOCK.STOCK_TSI:
                return "tsi"
            elif self == stock.STOCK.STOCK_TSLA:
                return "tsla"
            elif self == stock.STOCK.STOCK_TSLF:
                return "tslf"
            elif self == stock.STOCK.STOCK_TSLX:
                return "tslx"
            elif self == stock.STOCK.STOCK_TSM:
                return "tsm"
            elif self == stock.STOCK.STOCK_TSN:
                return "tsn"
            elif self == stock.STOCK.STOCK_TSQ:
                return "tsq"
            elif self == stock.STOCK.STOCK_TSRI:
                return "tsri"
            elif self == stock.STOCK.STOCK_TSRO:
                return "tsro"
            elif self == stock.STOCK.STOCK_TSS:
                return "tss"
            elif self == stock.STOCK.STOCK_TST:
                return "tst"
            elif self == stock.STOCK.STOCK_TSU:
                return "tsu"
            elif self == stock.STOCK.STOCK_TTAC:
                return "ttac"
            elif self == stock.STOCK.STOCK_TTAI:
                return "ttai"
            elif self == stock.STOCK.STOCK_TTC:
                return "ttc"
            elif self == stock.STOCK.STOCK_TTD:
                return "ttd"
            elif self == stock.STOCK.STOCK_TTEC:
                return "ttec"
            elif self == stock.STOCK.STOCK_TTEK:
                return "ttek"
            elif self == stock.STOCK.STOCK_TTF:
                return "ttf"
            elif self == stock.STOCK.STOCK_TTGT:
                return "ttgt"
            elif self == stock.STOCK.STOCK_TTI:
                return "tti"
            elif self == stock.STOCK.STOCK_TTM:
                return "ttm"
            elif self == stock.STOCK.STOCK_TTMI:
                return "ttmi"
            elif self == stock.STOCK.STOCK_TTNP:
                return "ttnp"
            elif self == stock.STOCK.STOCK_TTOO:
                return "ttoo"
            elif self == stock.STOCK.STOCK_TTP:
                return "ttp"
            elif self == stock.STOCK.STOCK_TTPH:
                return "ttph"
            elif self == stock.STOCK.STOCK_TTS:
                return "tts"
            elif self == stock.STOCK.STOCK_TTWO:
                return "ttwo"
            elif self == stock.STOCK.STOCK_TU:
                return "tu"
            elif self == stock.STOCK.STOCK_TUES:
                return "tues"
            elif self == stock.STOCK.STOCK_TUP:
                return "tup"
            elif self == stock.STOCK.STOCK_TURN:
                return "turn"
            elif self == stock.STOCK.STOCK_TUSK:
                return "tusk"
            elif self == stock.STOCK.STOCK_TV:
                return "tv"
            elif self == stock.STOCK.STOCK_TVC:
                return "tvc"
            elif self == stock.STOCK.STOCK_TVE:
                return "tve"
            elif self == stock.STOCK.STOCK_TVPT:
                return "tvpt"
            elif self == stock.STOCK.STOCK_TVTY:
                return "tvty"
            elif self == stock.STOCK.STOCK_TWI:
                return "twi"
            elif self == stock.STOCK.STOCK_TWIN:
                return "twin"
            elif self == stock.STOCK.STOCK_TWLO:
                return "twlo"
            elif self == stock.STOCK.STOCK_TWMC:
                return "twmc"
            elif self == stock.STOCK.STOCK_TWN:
                return "twn"
            elif self == stock.STOCK.STOCK_TWNK:
                return "twnk"
            elif self == stock.STOCK.STOCK_TWNKW:
                return "twnkw"
            elif self == stock.STOCK.STOCK_TWO:
                return "two"
            elif self == stock.STOCK.STOCK_TWOU:
                return "twou"
            elif self == stock.STOCK.STOCK_TWOW:
                return "twow"
            elif self == stock.STOCK.STOCK_TWO_A:
                return "two_a"
            elif self == stock.STOCK.STOCK_TWO_B:
                return "two_b"
            elif self == stock.STOCK.STOCK_TWTR:
                return "twtr"
            elif self == stock.STOCK.STOCK_TWX:
                return "twx"
            elif self == stock.STOCK.STOCK_TX:
                return "tx"
            elif self == stock.STOCK.STOCK_TXMD:
                return "txmd"
            elif self == stock.STOCK.STOCK_TXN:
                return "txn"
            elif self == stock.STOCK.STOCK_TXRH:
                return "txrh"
            elif self == stock.STOCK.STOCK_TXT:
                return "txt"
            elif self == stock.STOCK.STOCK_TY:
                return "ty"
            elif self == stock.STOCK.STOCK_TYG:
                return "tyg"
            elif self == stock.STOCK.STOCK_TYHT:
                return "tyht"
            elif self == stock.STOCK.STOCK_TYL:
                return "tyl"
            elif self == stock.STOCK.STOCK_TYME:
                return "tyme"
            elif self == stock.STOCK.STOCK_TYPE:
                return "type"
            elif self == stock.STOCK.STOCK_TY_:
                return "ty_"
            elif self == stock.STOCK.STOCK_TZOO:
                return "tzoo"
            elif self == stock.STOCK.STOCK_UA:
                return "ua"
            elif self == stock.STOCK.STOCK_UAA:
                return "uaa"
            elif self == stock.STOCK.STOCK_UAL:
                return "ual"
            elif self == stock.STOCK.STOCK_UAMY:
                return "uamy"
            elif self == stock.STOCK.STOCK_UAN:
                return "uan"
            elif self == stock.STOCK.STOCK_UBA:
                return "uba"
            elif self == stock.STOCK.STOCK_UBCP:
                return "ubcp"
            elif self == stock.STOCK.STOCK_UBFO:
                return "ubfo"
            elif self == stock.STOCK.STOCK_UBIO:
                return "ubio"
            elif self == stock.STOCK.STOCK_UBNK:
                return "ubnk"
            elif self == stock.STOCK.STOCK_UBNT:
                return "ubnt"
            elif self == stock.STOCK.STOCK_UBOH:
                return "uboh"
            elif self == stock.STOCK.STOCK_UBP:
                return "ubp"
            elif self == stock.STOCK.STOCK_UBP_F-CL:
                return "ubp_f-cl"
            elif self == stock.STOCK.STOCK_UBP_G:
                return "ubp_g"
            elif self == stock.STOCK.STOCK_UBP_H:
                return "ubp_h"
            elif self == stock.STOCK.STOCK_UBRT:
                return "ubrt"
            elif self == stock.STOCK.STOCK_UBS:
                return "ubs"
            elif self == stock.STOCK.STOCK_UBSH:
                return "ubsh"
            elif self == stock.STOCK.STOCK_UBSI:
                return "ubsi"
            elif self == stock.STOCK.STOCK_UCBA:
                return "ucba"
            elif self == stock.STOCK.STOCK_UCBI:
                return "ucbi"
            elif self == stock.STOCK.STOCK_UCFC:
                return "ucfc"
            elif self == stock.STOCK.STOCK_UCTT:
                return "uctt"
            elif self == stock.STOCK.STOCK_UDBI:
                return "udbi"
            elif self == stock.STOCK.STOCK_UDR:
                return "udr"
            elif self == stock.STOCK.STOCK_UE:
                return "ue"
            elif self == stock.STOCK.STOCK_UEC:
                return "uec"
            elif self == stock.STOCK.STOCK_UEIC:
                return "ueic"
            elif self == stock.STOCK.STOCK_UEPS:
                return "ueps"
            elif self == stock.STOCK.STOCK_UEVM:
                return "uevm"
            elif self == stock.STOCK.STOCK_UFAB:
                return "ufab"
            elif self == stock.STOCK.STOCK_UFCS:
                return "ufcs"
            elif self == stock.STOCK.STOCK_UFI:
                return "ufi"
            elif self == stock.STOCK.STOCK_UFPI:
                return "ufpi"
            elif self == stock.STOCK.STOCK_UFPT:
                return "ufpt"
            elif self == stock.STOCK.STOCK_UFS:
                return "ufs"
            elif self == stock.STOCK.STOCK_UG:
                return "ug"
            elif self == stock.STOCK.STOCK_UGI:
                return "ugi"
            elif self == stock.STOCK.STOCK_UGP:
                return "ugp"
            elif self == stock.STOCK.STOCK_UHAL:
                return "uhal"
            elif self == stock.STOCK.STOCK_UHS:
                return "uhs"
            elif self == stock.STOCK.STOCK_UHT:
                return "uht"
            elif self == stock.STOCK.STOCK_UIHC:
                return "uihc"
            elif self == stock.STOCK.STOCK_UIS:
                return "uis"
            elif self == stock.STOCK.STOCK_UITB:
                return "uitb"
            elif self == stock.STOCK.STOCK_UIVM:
                return "uivm"
            elif self == stock.STOCK.STOCK_UL:
                return "ul"
            elif self == stock.STOCK.STOCK_ULBI:
                return "ulbi"
            elif self == stock.STOCK.STOCK_ULH:
                return "ulh"
            elif self == stock.STOCK.STOCK_ULTA:
                return "ulta"
            elif self == stock.STOCK.STOCK_ULTI:
                return "ulti"
            elif self == stock.STOCK.STOCK_ULVM:
                return "ulvm"
            elif self == stock.STOCK.STOCK_UMBF:
                return "umbf"
            elif self == stock.STOCK.STOCK_UMC:
                return "umc"
            elif self == stock.STOCK.STOCK_UMH:
                return "umh"
            elif self == stock.STOCK.STOCK_UMH_B:
                return "umh_b"
            elif self == stock.STOCK.STOCK_UMH_C:
                return "umh_c"
            elif self == stock.STOCK.STOCK_UMPQ:
                return "umpq"
            elif self == stock.STOCK.STOCK_UN:
                return "un"
            elif self == stock.STOCK.STOCK_UNAM:
                return "unam"
            elif self == stock.STOCK.STOCK_UNB:
                return "unb"
            elif self == stock.STOCK.STOCK_UNF:
                return "unf"
            elif self == stock.STOCK.STOCK_UNFI:
                return "unfi"
            elif self == stock.STOCK.STOCK_UNH:
                return "unh"
            elif self == stock.STOCK.STOCK_UNIT:
                return "unit"
            elif self == stock.STOCK.STOCK_UNM:
                return "unm"
            elif self == stock.STOCK.STOCK_UNP:
                return "unp"
            elif self == stock.STOCK.STOCK_UNT:
                return "unt"
            elif self == stock.STOCK.STOCK_UNTY:
                return "unty"
            elif self == stock.STOCK.STOCK_UNVR:
                return "unvr"
            elif self == stock.STOCK.STOCK_UONE:
                return "uone"
            elif self == stock.STOCK.STOCK_UONEK:
                return "uonek"
            elif self == stock.STOCK.STOCK_UPL:
                return "upl"
            elif self == stock.STOCK.STOCK_UPLD:
                return "upld"
            elif self == stock.STOCK.STOCK_UPS:
                return "ups"
            elif self == stock.STOCK.STOCK_UQM:
                return "uqm"
            elif self == stock.STOCK.STOCK_URBN:
                return "urbn"
            elif self == stock.STOCK.STOCK_URG:
                return "urg"
            elif self == stock.STOCK.STOCK_URGN:
                return "urgn"
            elif self == stock.STOCK.STOCK_URI:
                return "uri"
            elif self == stock.STOCK.STOCK_USA:
                return "usa"
            elif self == stock.STOCK.STOCK_USAC:
                return "usac"
            elif self == stock.STOCK.STOCK_USAK:
                return "usak"
            elif self == stock.STOCK.STOCK_USAP:
                return "usap"
            elif self == stock.STOCK.STOCK_USAS:
                return "usas"
            elif self == stock.STOCK.STOCK_USAT:
                return "usat"
            elif self == stock.STOCK.STOCK_USATP:
                return "usatp"
            elif self == stock.STOCK.STOCK_USAU:
                return "usau"
            elif self == stock.STOCK.STOCK_USB:
                return "usb"
            elif self == stock.STOCK.STOCK_USB_A:
                return "usb_a"
            elif self == stock.STOCK.STOCK_USB_H:
                return "usb_h"
            elif self == stock.STOCK.STOCK_USB_M:
                return "usb_m"
            elif self == stock.STOCK.STOCK_USB_O:
                return "usb_o"
            elif self == stock.STOCK.STOCK_USCR:
                return "uscr"
            elif self == stock.STOCK.STOCK_USDP:
                return "usdp"
            elif self == stock.STOCK.STOCK_USEG:
                return "useg"
            elif self == stock.STOCK.STOCK_USEQ:
                return "useq"
            elif self == stock.STOCK.STOCK_USFD:
                return "usfd"
            elif self == stock.STOCK.STOCK_USG:
                return "usg"
            elif self == stock.STOCK.STOCK_USHY:
                return "ushy"
            elif self == stock.STOCK.STOCK_USLB:
                return "uslb"
            elif self == stock.STOCK.STOCK_USLM:
                return "uslm"
            elif self == stock.STOCK.STOCK_USM:
                return "usm"
            elif self == stock.STOCK.STOCK_USMC:
                return "usmc"
            elif self == stock.STOCK.STOCK_USMF:
                return "usmf"
            elif self == stock.STOCK.STOCK_USNA:
                return "usna"
            elif self == stock.STOCK.STOCK_USOD:
                return "usod"
            elif self == stock.STOCK.STOCK_USOI:
                return "usoi"
            elif self == stock.STOCK.STOCK_USOU:
                return "usou"
            elif self == stock.STOCK.STOCK_USPH:
                return "usph"
            elif self == stock.STOCK.STOCK_USRT:
                return "usrt"
            elif self == stock.STOCK.STOCK_USTB:
                return "ustb"
            elif self == stock.STOCK.STOCK_USVM:
                return "usvm"
            elif self == stock.STOCK.STOCK_UTES:
                return "utes"
            elif self == stock.STOCK.STOCK_UTF:
                return "utf"
            elif self == stock.STOCK.STOCK_UTG:
                return "utg"
            elif self == stock.STOCK.STOCK_UTHR:
                return "uthr"
            elif self == stock.STOCK.STOCK_UTI:
                return "uti"
            elif self == stock.STOCK.STOCK_UTL:
                return "utl"
            elif self == stock.STOCK.STOCK_UTLF:
                return "utlf"
            elif self == stock.STOCK.STOCK_UTMD:
                return "utmd"
            elif self == stock.STOCK.STOCK_UTSI:
                return "utsi"
            elif self == stock.STOCK.STOCK_UTSL:
                return "utsl"
            elif self == stock.STOCK.STOCK_UTX:
                return "utx"
            elif self == stock.STOCK.STOCK_UUU:
                return "uuu"
            elif self == stock.STOCK.STOCK_UUUU-WS:
                return "uuuu-ws"
            elif self == stock.STOCK.STOCK_UUUU:
                return "uuuu"
            elif self == stock.STOCK.STOCK_UVE:
                return "uve"
            elif self == stock.STOCK.STOCK_UVSP:
                return "uvsp"
            elif self == stock.STOCK.STOCK_UVV:
                return "uvv"
            elif self == stock.STOCK.STOCK_UWN:
                return "uwn"
            elif self == stock.STOCK.STOCK_UWT:
                return "uwt"
            elif self == stock.STOCK.STOCK_UZA:
                return "uza"
            elif self == stock.STOCK.STOCK_UZB:
                return "uzb"
            elif self == stock.STOCK.STOCK_UZC:
                return "uzc"
            elif self == stock.STOCK.STOCK_V:
                return "v"
            elif self == stock.STOCK.STOCK_VAC:
                return "vac"
            elif self == stock.STOCK.STOCK_VALE-P:
                return "vale-p"
            elif self == stock.STOCK.STOCK_VALE:
                return "vale"
            elif self == stock.STOCK.STOCK_VALU:
                return "valu"
            elif self == stock.STOCK.STOCK_VALX:
                return "valx"
            elif self == stock.STOCK.STOCK_VAMO:
                return "vamo"
            elif self == stock.STOCK.STOCK_VAR:
                return "var"
            elif self == stock.STOCK.STOCK_VBF:
                return "vbf"
            elif self == stock.STOCK.STOCK_VBFC:
                return "vbfc"
            elif self == stock.STOCK.STOCK_VBIV:
                return "vbiv"
            elif self == stock.STOCK.STOCK_VBLT:
                return "vblt"
            elif self == stock.STOCK.STOCK_VBND:
                return "vbnd"
            elif self == stock.STOCK.STOCK_VBTX:
                return "vbtx"
            elif self == stock.STOCK.STOCK_VC:
                return "vc"
            elif self == stock.STOCK.STOCK_VCEL:
                return "vcel"
            elif self == stock.STOCK.STOCK_VCF:
                return "vcf"
            elif self == stock.STOCK.STOCK_VCO:
                return "vco"
            elif self == stock.STOCK.STOCK_VCRA:
                return "vcra"
            elif self == stock.STOCK.STOCK_VCV:
                return "vcv"
            elif self == stock.STOCK.STOCK_VCYT:
                return "vcyt"
            elif self == stock.STOCK.STOCK_VDSI:
                return "vdsi"
            elif self == stock.STOCK.STOCK_VDTH:
                return "vdth"
            elif self == stock.STOCK.STOCK_VEAC:
                return "veac"
            elif self == stock.STOCK.STOCK_VEACU:
                return "veacu"
            elif self == stock.STOCK.STOCK_VEACW:
                return "veacw"
            elif self == stock.STOCK.STOCK_VEC:
                return "vec"
            elif self == stock.STOCK.STOCK_VECO:
                return "veco"
            elif self == stock.STOCK.STOCK_VEDL:
                return "vedl"
            elif self == stock.STOCK.STOCK_VEEV:
                return "veev"
            elif self == stock.STOCK.STOCK_VEON:
                return "veon"
            elif self == stock.STOCK.STOCK_VER:
                return "ver"
            elif self == stock.STOCK.STOCK_VERI:
                return "veri"
            elif self == stock.STOCK.STOCK_VERU:
                return "veru"
            elif self == stock.STOCK.STOCK_VER_F:
                return "ver_f"
            elif self == stock.STOCK.STOCK_VESH:
                return "vesh"
            elif self == stock.STOCK.STOCK_VET:
                return "vet"
            elif self == stock.STOCK.STOCK_VFC:
                return "vfc"
            elif self == stock.STOCK.STOCK_VFL:
                return "vfl"
            elif self == stock.STOCK.STOCK_VG:
                return "vg"
            elif self == stock.STOCK.STOCK_VGFO:
                return "vgfo"
            elif self == stock.STOCK.STOCK_VGI:
                return "vgi"
            elif self == stock.STOCK.STOCK_VGM:
                return "vgm"
            elif self == stock.STOCK.STOCK_VGR:
                return "vgr"
            elif self == stock.STOCK.STOCK_VGZ:
                return "vgz"
            elif self == stock.STOCK.STOCK_VHC:
                return "vhc"
            elif self == stock.STOCK.STOCK_VHI:
                return "vhi"
            elif self == stock.STOCK.STOCK_VIA:
                return "via"
            elif self == stock.STOCK.STOCK_VIAB:
                return "viab"
            elif self == stock.STOCK.STOCK_VIAV:
                return "viav"
            elif self == stock.STOCK.STOCK_VICL:
                return "vicl"
            elif self == stock.STOCK.STOCK_VICR:
                return "vicr"
            elif self == stock.STOCK.STOCK_VIGI:
                return "vigi"
            elif self == stock.STOCK.STOCK_VII:
                return "vii"
            elif self == stock.STOCK.STOCK_VIPS:
                return "vips"
            elif self == stock.STOCK.STOCK_VIRC:
                return "virc"
            elif self == stock.STOCK.STOCK_VIRT:
                return "virt"
            elif self == stock.STOCK.STOCK_VISI:
                return "visi"
            elif self == stock.STOCK.STOCK_VIST:
                return "vist"
            elif self == stock.STOCK.STOCK_VIV:
                return "viv"
            elif self == stock.STOCK.STOCK_VIVE:
                return "vive"
            elif self == stock.STOCK.STOCK_VIVO:
                return "vivo"
            elif self == stock.STOCK.STOCK_VJET:
                return "vjet"
            elif self == stock.STOCK.STOCK_VKI:
                return "vki"
            elif self == stock.STOCK.STOCK_VKQ:
                return "vkq"
            elif self == stock.STOCK.STOCK_VKTX:
                return "vktx"
            elif self == stock.STOCK.STOCK_VKTXW:
                return "vktxw"
            elif self == stock.STOCK.STOCK_VLGEA:
                return "vlgea"
            elif self == stock.STOCK.STOCK_VLO:
                return "vlo"
            elif self == stock.STOCK.STOCK_VLP:
                return "vlp"
            elif self == stock.STOCK.STOCK_VLRS:
                return "vlrs"
            elif self == stock.STOCK.STOCK_VLRX:
                return "vlrx"
            elif self == stock.STOCK.STOCK_VLT:
                return "vlt"
            elif self == stock.STOCK.STOCK_VLY-WS:
                return "vly-ws"
            elif self == stock.STOCK.STOCK_VLY:
                return "vly"
            elif self == stock.STOCK.STOCK_VLY_A:
                return "vly_a"
            elif self == stock.STOCK.STOCK_VLY_B:
                return "vly_b"
            elif self == stock.STOCK.STOCK_VMAX:
                return "vmax"
            elif self == stock.STOCK.STOCK_VMC:
                return "vmc"
            elif self == stock.STOCK.STOCK_VMET:
                return "vmet"
            elif self == stock.STOCK.STOCK_VMI:
                return "vmi"
            elif self == stock.STOCK.STOCK_VMIN:
                return "vmin"
            elif self == stock.STOCK.STOCK_VMM:
                return "vmm"
            elif self == stock.STOCK.STOCK_VMO:
                return "vmo"
            elif self == stock.STOCK.STOCK_VMOT:
                return "vmot"
            elif self == stock.STOCK.STOCK_VMW:
                return "vmw"
            elif self == stock.STOCK.STOCK_VNCE:
                return "vnce"
            elif self == stock.STOCK.STOCK_VNDA:
                return "vnda"
            elif self == stock.STOCK.STOCK_VNET:
                return "vnet"
            elif self == stock.STOCK.STOCK_VNLA:
                return "vnla"
            elif self == stock.STOCK.STOCK_VNO:
                return "vno"
            elif self == stock.STOCK.STOCK_VNOM:
                return "vnom"
            elif self == stock.STOCK.STOCK_VNO_G:
                return "vno_g"
            elif self == stock.STOCK.STOCK_VNO_I:
                return "vno_i"
            elif self == stock.STOCK.STOCK_VNO_K:
                return "vno_k"
            elif self == stock.STOCK.STOCK_VNO_L:
                return "vno_l"
            elif self == stock.STOCK.STOCK_VNRX:
                return "vnrx"
            elif self == stock.STOCK.STOCK_VNTR:
                return "vntr"
            elif self == stock.STOCK.STOCK_VNTV:
                return "vntv"
            elif self == stock.STOCK.STOCK_VOC:
                return "voc"
            elif self == stock.STOCK.STOCK_VOD:
                return "vod"
            elif self == stock.STOCK.STOCK_VOXX:
                return "voxx"
            elif self == stock.STOCK.STOCK_VOYA:
                return "voya"
            elif self == stock.STOCK.STOCK_VPG:
                return "vpg"
            elif self == stock.STOCK.STOCK_VPV:
                return "vpv"
            elif self == stock.STOCK.STOCK_VR:
                return "vr"
            elif self == stock.STOCK.STOCK_VRA:
                return "vra"
            elif self == stock.STOCK.STOCK_VRAY:
                return "vray"
            elif self == stock.STOCK.STOCK_VREX:
                return "vrex"
            elif self == stock.STOCK.STOCK_VRIG:
                return "vrig"
            elif self == stock.STOCK.STOCK_VRML:
                return "vrml"
            elif self == stock.STOCK.STOCK_VRNA:
                return "vrna"
            elif self == stock.STOCK.STOCK_VRNS:
                return "vrns"
            elif self == stock.STOCK.STOCK_VRNT:
                return "vrnt"
            elif self == stock.STOCK.STOCK_VRS:
                return "vrs"
            elif self == stock.STOCK.STOCK_VRSK:
                return "vrsk"
            elif self == stock.STOCK.STOCK_VRSN:
                return "vrsn"
            elif self == stock.STOCK.STOCK_VRTS:
                return "vrts"
            elif self == stock.STOCK.STOCK_VRTSP:
                return "vrtsp"
            elif self == stock.STOCK.STOCK_VRTU:
                return "vrtu"
            elif self == stock.STOCK.STOCK_VRTV:
                return "vrtv"
            elif self == stock.STOCK.STOCK_VRTX:
                return "vrtx"
            elif self == stock.STOCK.STOCK_VRX:
                return "vrx"
            elif self == stock.STOCK.STOCK_VR_A:
                return "vr_a"
            elif self == stock.STOCK.STOCK_VR_B:
                return "vr_b"
            elif self == stock.STOCK.STOCK_VSAR:
                return "vsar"
            elif self == stock.STOCK.STOCK_VSAT:
                return "vsat"
            elif self == stock.STOCK.STOCK_VSDA:
                return "vsda"
            elif self == stock.STOCK.STOCK_VSEC:
                return "vsec"
            elif self == stock.STOCK.STOCK_VSH:
                return "vsh"
            elif self == stock.STOCK.STOCK_VSI:
                return "vsi"
            elif self == stock.STOCK.STOCK_VSLR:
                return "vslr"
            elif self == stock.STOCK.STOCK_VSM:
                return "vsm"
            elif self == stock.STOCK.STOCK_VSMV:
                return "vsmv"
            elif self == stock.STOCK.STOCK_VST:
                return "vst"
            elif self == stock.STOCK.STOCK_VSTM:
                return "vstm"
            elif self == stock.STOCK.STOCK_VSTO:
                return "vsto"
            elif self == stock.STOCK.STOCK_VTA:
                return "vta"
            elif self == stock.STOCK.STOCK_VTC:
                return "vtc"
            elif self == stock.STOCK.STOCK_VTEB:
                return "vteb"
            elif self == stock.STOCK.STOCK_VTGN:
                return "vtgn"
            elif self == stock.STOCK.STOCK_VTL:
                return "vtl"
            elif self == stock.STOCK.STOCK_VTN:
                return "vtn"
            elif self == stock.STOCK.STOCK_VTNR:
                return "vtnr"
            elif self == stock.STOCK.STOCK_VTR:
                return "vtr"
            elif self == stock.STOCK.STOCK_VTRB:
                return "vtrb"
            elif self == stock.STOCK.STOCK_VTVT:
                return "vtvt"
            elif self == stock.STOCK.STOCK_VUZI:
                return "vuzi"
            elif self == stock.STOCK.STOCK_VVC:
                return "vvc"
            elif self == stock.STOCK.STOCK_VVI:
                return "vvi"
            elif self == stock.STOCK.STOCK_VVPR:
                return "vvpr"
            elif self == stock.STOCK.STOCK_VVR:
                return "vvr"
            elif self == stock.STOCK.STOCK_VVUS:
                return "vvus"
            elif self == stock.STOCK.STOCK_VVV:
                return "vvv"
            elif self == stock.STOCK.STOCK_VWR:
                return "vwr"
            elif self == stock.STOCK.STOCK_VYGR:
                return "vygr"
            elif self == stock.STOCK.STOCK_VYMI:
                return "vymi"
            elif self == stock.STOCK.STOCK_VZ:
                return "vz"
            elif self == stock.STOCK.STOCK_VZA:
                return "vza"
            elif self == stock.STOCK.STOCK_W:
                return "w"
            elif self == stock.STOCK.STOCK_WAAS:
                return "waas"
            elif self == stock.STOCK.STOCK_WAB:
                return "wab"
            elif self == stock.STOCK.STOCK_WABC:
                return "wabc"
            elif self == stock.STOCK.STOCK_WAC:
                return "wac"
            elif self == stock.STOCK.STOCK_WAFD:
                return "wafd"
            elif self == stock.STOCK.STOCK_WAFDW:
                return "wafdw"
            elif self == stock.STOCK.STOCK_WAGE:
                return "wage"
            elif self == stock.STOCK.STOCK_WAIR:
                return "wair"
            elif self == stock.STOCK.STOCK_WAL:
                return "wal"
            elif self == stock.STOCK.STOCK_WALA:
                return "wala"
            elif self == stock.STOCK.STOCK_WASH:
                return "wash"
            elif self == stock.STOCK.STOCK_WAT:
                return "wat"
            elif self == stock.STOCK.STOCK_WATT:
                return "watt"
            elif self == stock.STOCK.STOCK_WAYN:
                return "wayn"
            elif self == stock.STOCK.STOCK_WB:
                return "wb"
            elif self == stock.STOCK.STOCK_WBA:
                return "wba"
            elif self == stock.STOCK.STOCK_WBAI:
                return "wbai"
            elif self == stock.STOCK.STOCK_WBBW:
                return "wbbw"
            elif self == stock.STOCK.STOCK_WBC:
                return "wbc"
            elif self == stock.STOCK.STOCK_WBIA:
                return "wbia"
            elif self == stock.STOCK.STOCK_WBIB:
                return "wbib"
            elif self == stock.STOCK.STOCK_WBIC:
                return "wbic"
            elif self == stock.STOCK.STOCK_WBID:
                return "wbid"
            elif self == stock.STOCK.STOCK_WBIE:
                return "wbie"
            elif self == stock.STOCK.STOCK_WBIF:
                return "wbif"
            elif self == stock.STOCK.STOCK_WBIG:
                return "wbig"
            elif self == stock.STOCK.STOCK_WBIH:
                return "wbih"
            elif self == stock.STOCK.STOCK_WBII:
                return "wbii"
            elif self == stock.STOCK.STOCK_WBIL:
                return "wbil"
            elif self == stock.STOCK.STOCK_WBIR:
                return "wbir"
            elif self == stock.STOCK.STOCK_WBIY:
                return "wbiy"
            elif self == stock.STOCK.STOCK_WBK:
                return "wbk"
            elif self == stock.STOCK.STOCK_WBKC:
                return "wbkc"
            elif self == stock.STOCK.STOCK_WBS:
                return "wbs"
            elif self == stock.STOCK.STOCK_WBS_E:
                return "wbs_e"
            elif self == stock.STOCK.STOCK_WBT:
                return "wbt"
            elif self == stock.STOCK.STOCK_WCC:
                return "wcc"
            elif self == stock.STOCK.STOCK_WCFB:
                return "wcfb"
            elif self == stock.STOCK.STOCK_WCG:
                return "wcg"
            elif self == stock.STOCK.STOCK_WCN:
                return "wcn"
            elif self == stock.STOCK.STOCK_WD:
                return "wd"
            elif self == stock.STOCK.STOCK_WDAY:
                return "wday"
            elif self == stock.STOCK.STOCK_WDC:
                return "wdc"
            elif self == stock.STOCK.STOCK_WDFC:
                return "wdfc"
            elif self == stock.STOCK.STOCK_WDR:
                return "wdr"
            elif self == stock.STOCK.STOCK_WDRW:
                return "wdrw"
            elif self == stock.STOCK.STOCK_WEA:
                return "wea"
            elif self == stock.STOCK.STOCK_WEAR:
                return "wear"
            elif self == stock.STOCK.STOCK_WEB:
                return "web"
            elif self == stock.STOCK.STOCK_WEBK:
                return "webk"
            elif self == stock.STOCK.STOCK_WEC:
                return "wec"
            elif self == stock.STOCK.STOCK_WEN:
                return "wen"
            elif self == stock.STOCK.STOCK_WERN:
                return "wern"
            elif self == stock.STOCK.STOCK_WES:
                return "wes"
            elif self == stock.STOCK.STOCK_WETF:
                return "wetf"
            elif self == stock.STOCK.STOCK_WEX:
                return "wex"
            elif self == stock.STOCK.STOCK_WEXP:
                return "wexp"
            elif self == stock.STOCK.STOCK_WEYS:
                return "weys"
            elif self == stock.STOCK.STOCK_WF:
                return "wf"
            elif self == stock.STOCK.STOCK_WFBI:
                return "wfbi"
            elif self == stock.STOCK.STOCK_WFC-WS:
                return "wfc-ws"
            elif self == stock.STOCK.STOCK_WFC:
                return "wfc"
            elif self == stock.STOCK.STOCK_WFC_J:
                return "wfc_j"
            elif self == stock.STOCK.STOCK_WFC_L:
                return "wfc_l"
            elif self == stock.STOCK.STOCK_WFC_N:
                return "wfc_n"
            elif self == stock.STOCK.STOCK_WFC_O:
                return "wfc_o"
            elif self == stock.STOCK.STOCK_WFC_P:
                return "wfc_p"
            elif self == stock.STOCK.STOCK_WFC_Q:
                return "wfc_q"
            elif self == stock.STOCK.STOCK_WFC_R:
                return "wfc_r"
            elif self == stock.STOCK.STOCK_WFC_T:
                return "wfc_t"
            elif self == stock.STOCK.STOCK_WFC_V:
                return "wfc_v"
            elif self == stock.STOCK.STOCK_WFC_W:
                return "wfc_w"
            elif self == stock.STOCK.STOCK_WFC_X:
                return "wfc_x"
            elif self == stock.STOCK.STOCK_WFC_Y:
                return "wfc_y"
            elif self == stock.STOCK.STOCK_WFE_A:
                return "wfe_a"
            elif self == stock.STOCK.STOCK_WFHY:
                return "wfhy"
            elif self == stock.STOCK.STOCK_WFIG:
                return "wfig"
            elif self == stock.STOCK.STOCK_WFT:
                return "wft"
            elif self == stock.STOCK.STOCK_WG:
                return "wg"
            elif self == stock.STOCK.STOCK_WGL:
                return "wgl"
            elif self == stock.STOCK.STOCK_WGO:
                return "wgo"
            elif self == stock.STOCK.STOCK_WGP:
                return "wgp"
            elif self == stock.STOCK.STOCK_WHF:
                return "whf"
            elif self == stock.STOCK.STOCK_WHFBL:
                return "whfbl"
            elif self == stock.STOCK.STOCK_WHG:
                return "whg"
            elif self == stock.STOCK.STOCK_WHLM:
                return "whlm"
            elif self == stock.STOCK.STOCK_WHLR:
                return "whlr"
            elif self == stock.STOCK.STOCK_WHLRD:
                return "whlrd"
            elif self == stock.STOCK.STOCK_WHLRP:
                return "whlrp"
            elif self == stock.STOCK.STOCK_WHLRW:
                return "whlrw"
            elif self == stock.STOCK.STOCK_WHR:
                return "whr"
            elif self == stock.STOCK.STOCK_WIA:
                return "wia"
            elif self == stock.STOCK.STOCK_WIFI:
                return "wifi"
            elif self == stock.STOCK.STOCK_WILC:
                return "wilc"
            elif self == stock.STOCK.STOCK_WIN:
                return "win"
            elif self == stock.STOCK.STOCK_WINA:
                return "wina"
            elif self == stock.STOCK.STOCK_WING:
                return "wing"
            elif self == stock.STOCK.STOCK_WINS:
                return "wins"
            elif self == stock.STOCK.STOCK_WIRE:
                return "wire"
            elif self == stock.STOCK.STOCK_WIT:
                return "wit"
            elif self == stock.STOCK.STOCK_WIW:
                return "wiw"
            elif self == stock.STOCK.STOCK_WIX:
                return "wix"
            elif self == stock.STOCK.STOCK_WK:
                return "wk"
            elif self == stock.STOCK.STOCK_WKHS:
                return "wkhs"
            elif self == stock.STOCK.STOCK_WLB:
                return "wlb"
            elif self == stock.STOCK.STOCK_WLDN:
                return "wldn"
            elif self == stock.STOCK.STOCK_WLFC:
                return "wlfc"
            elif self == stock.STOCK.STOCK_WLH:
                return "wlh"
            elif self == stock.STOCK.STOCK_WLK:
                return "wlk"
            elif self == stock.STOCK.STOCK_WLKP:
                return "wlkp"
            elif self == stock.STOCK.STOCK_WLL:
                return "wll"
            elif self == stock.STOCK.STOCK_WLTW:
                return "wltw"
            elif self == stock.STOCK.STOCK_WM:
                return "wm"
            elif self == stock.STOCK.STOCK_WMB:
                return "wmb"
            elif self == stock.STOCK.STOCK_WMC:
                return "wmc"
            elif self == stock.STOCK.STOCK_WMGI:
                return "wmgi"
            elif self == stock.STOCK.STOCK_WMGIZ:
                return "wmgiz"
            elif self == stock.STOCK.STOCK_WMIH:
                return "wmih"
            elif self == stock.STOCK.STOCK_WMK:
                return "wmk"
            elif self == stock.STOCK.STOCK_WMLP:
                return "wmlp"
            elif self == stock.STOCK.STOCK_WMS:
                return "wms"
            elif self == stock.STOCK.STOCK_WMT:
                return "wmt"
            elif self == stock.STOCK.STOCK_WNC:
                return "wnc"
            elif self == stock.STOCK.STOCK_WNEB:
                return "wneb"
            elif self == stock.STOCK.STOCK_WNFM:
                return "wnfm"
            elif self == stock.STOCK.STOCK_WNRL:
                return "wnrl"
            elif self == stock.STOCK.STOCK_WNS:
                return "wns"
            elif self == stock.STOCK.STOCK_WOR:
                return "wor"
            elif self == stock.STOCK.STOCK_WOW:
                return "wow"
            elif self == stock.STOCK.STOCK_WPC:
                return "wpc"
            elif self == stock.STOCK.STOCK_WPCS:
                return "wpcs"
            elif self == stock.STOCK.STOCK_WPG:
                return "wpg"
            elif self == stock.STOCK.STOCK_WPG_H:
                return "wpg_h"
            elif self == stock.STOCK.STOCK_WPG_I:
                return "wpg_i"
            elif self == stock.STOCK.STOCK_WPM:
                return "wpm"
            elif self == stock.STOCK.STOCK_WPPGY:
                return "wppgy"
            elif self == stock.STOCK.STOCK_WPRT:
                return "wprt"
            elif self == stock.STOCK.STOCK_WPX:
                return "wpx"
            elif self == stock.STOCK.STOCK_WPXP:
                return "wpxp"
            elif self == stock.STOCK.STOCK_WPZ:
                return "wpz"
            elif self == stock.STOCK.STOCK_WR:
                return "wr"
            elif self == stock.STOCK.STOCK_WRB:
                return "wrb"
            elif self == stock.STOCK.STOCK_WRB_B:
                return "wrb_b"
            elif self == stock.STOCK.STOCK_WRB_C:
                return "wrb_c"
            elif self == stock.STOCK.STOCK_WRB_D:
                return "wrb_d"
            elif self == stock.STOCK.STOCK_WRD:
                return "wrd"
            elif self == stock.STOCK.STOCK_WRE:
                return "wre"
            elif self == stock.STOCK.STOCK_WRI:
                return "wri"
            elif self == stock.STOCK.STOCK_WRK:
                return "wrk"
            elif self == stock.STOCK.STOCK_WRLD:
                return "wrld"
            elif self == stock.STOCK.STOCK_WRLS:
                return "wrls"
            elif self == stock.STOCK.STOCK_WRLSR:
                return "wrlsr"
            elif self == stock.STOCK.STOCK_WRLSU:
                return "wrlsu"
            elif self == stock.STOCK.STOCK_WRLSW:
                return "wrlsw"
            elif self == stock.STOCK.STOCK_WRN:
                return "wrn"
            elif self == stock.STOCK.STOCK_WSBC:
                return "wsbc"
            elif self == stock.STOCK.STOCK_WSBF:
                return "wsbf"
            elif self == stock.STOCK.STOCK_WSCI:
                return "wsci"
            elif self == stock.STOCK.STOCK_WSFS:
                return "wsfs"
            elif self == stock.STOCK.STOCK_WSKY:
                return "wsky"
            elif self == stock.STOCK.STOCK_WSM:
                return "wsm"
            elif self == stock.STOCK.STOCK_WSO-B:
                return "wso-b"
            elif self == stock.STOCK.STOCK_WSO:
                return "wso"
            elif self == stock.STOCK.STOCK_WSPT:
                return "wspt"
            elif self == stock.STOCK.STOCK_WSR:
                return "wsr"
            elif self == stock.STOCK.STOCK_WST:
                return "wst"
            elif self == stock.STOCK.STOCK_WSTG:
                return "wstg"
            elif self == stock.STOCK.STOCK_WSTL:
                return "wstl"
            elif self == stock.STOCK.STOCK_WTBA:
                return "wtba"
            elif self == stock.STOCK.STOCK_WTFC:
                return "wtfc"
            elif self == stock.STOCK.STOCK_WTFCM:
                return "wtfcm"
            elif self == stock.STOCK.STOCK_WTFCW:
                return "wtfcw"
            elif self == stock.STOCK.STOCK_WTI:
                return "wti"
            elif self == stock.STOCK.STOCK_WTID:
                return "wtid"
            elif self == stock.STOCK.STOCK_WTIU:
                return "wtiu"
            elif self == stock.STOCK.STOCK_WTM:
                return "wtm"
            elif self == stock.STOCK.STOCK_WTR:
                return "wtr"
            elif self == stock.STOCK.STOCK_WTRX:
                return "wtrx"
            elif self == stock.STOCK.STOCK_WTS:
                return "wts"
            elif self == stock.STOCK.STOCK_WTT:
                return "wtt"
            elif self == stock.STOCK.STOCK_WTTR:
                return "wttr"
            elif self == stock.STOCK.STOCK_WTW:
                return "wtw"
            elif self == stock.STOCK.STOCK_WU:
                return "wu"
            elif self == stock.STOCK.STOCK_WUBA:
                return "wuba"
            elif self == stock.STOCK.STOCK_WUSA:
                return "wusa"
            elif self == stock.STOCK.STOCK_WVE:
                return "wve"
            elif self == stock.STOCK.STOCK_WVFC:
                return "wvfc"
            elif self == stock.STOCK.STOCK_WVVI:
                return "wvvi"
            elif self == stock.STOCK.STOCK_WVVIP:
                return "wvvip"
            elif self == stock.STOCK.STOCK_WWD:
                return "wwd"
            elif self == stock.STOCK.STOCK_WWE:
                return "wwe"
            elif self == stock.STOCK.STOCK_WWR:
                return "wwr"
            elif self == stock.STOCK.STOCK_WWW:
                return "www"
            elif self == stock.STOCK.STOCK_WY:
                return "wy"
            elif self == stock.STOCK.STOCK_WYDE:
                return "wyde"
            elif self == stock.STOCK.STOCK_WYIG:
                return "wyig"
            elif self == stock.STOCK.STOCK_WYIGU:
                return "wyigu"
            elif self == stock.STOCK.STOCK_WYIGW:
                return "wyigw"
            elif self == stock.STOCK.STOCK_WYN:
                return "wyn"
            elif self == stock.STOCK.STOCK_WYNN:
                return "wynn"
            elif self == stock.STOCK.STOCK_WYY:
                return "wyy"
            elif self == stock.STOCK.STOCK_X:
                return "x"
            elif self == stock.STOCK.STOCK_XBIO:
                return "xbio"
            elif self == stock.STOCK.STOCK_XBIT:
                return "xbit"
            elif self == stock.STOCK.STOCK_XBKS:
                return "xbks"
            elif self == stock.STOCK.STOCK_XCEM:
                return "xcem"
            elif self == stock.STOCK.STOCK_XCO:
                return "xco"
            elif self == stock.STOCK.STOCK_XCRA:
                return "xcra"
            elif self == stock.STOCK.STOCK_XEC:
                return "xec"
            elif self == stock.STOCK.STOCK_XEL:
                return "xel"
            elif self == stock.STOCK.STOCK_XELA:
                return "xela"
            elif self == stock.STOCK.STOCK_XELB:
                return "xelb"
            elif self == stock.STOCK.STOCK_XENE:
                return "xene"
            elif self == stock.STOCK.STOCK_XENT:
                return "xent"
            elif self == stock.STOCK.STOCK_XFLT:
                return "xflt"
            elif self == stock.STOCK.STOCK_XGTI:
                return "xgti"
            elif self == stock.STOCK.STOCK_XGTIW:
                return "xgtiw"
            elif self == stock.STOCK.STOCK_XHR:
                return "xhr"
            elif self == stock.STOCK.STOCK_XIN:
                return "xin"
            elif self == stock.STOCK.STOCK_XINA:
                return "xina"
            elif self == stock.STOCK.STOCK_XITK:
                return "xitk"
            elif self == stock.STOCK.STOCK_XIVH:
                return "xivh"
            elif self == stock.STOCK.STOCK_XL:
                return "xl"
            elif self == stock.STOCK.STOCK_XLNX:
                return "xlnx"
            elif self == stock.STOCK.STOCK_XLRE:
                return "xlre"
            elif self == stock.STOCK.STOCK_XLRN:
                return "xlrn"
            elif self == stock.STOCK.STOCK_XMX:
                return "xmx"
            elif self == stock.STOCK.STOCK_XNCR:
                return "xncr"
            elif self == stock.STOCK.STOCK_XNET:
                return "xnet"
            elif self == stock.STOCK.STOCK_XNTK:
                return "xntk"
            elif self == stock.STOCK.STOCK_XNY:
                return "xny"
            elif self == stock.STOCK.STOCK_XOG:
                return "xog"
            elif self == stock.STOCK.STOCK_XOM:
                return "xom"
            elif self == stock.STOCK.STOCK_XOMA:
                return "xoma"
            elif self == stock.STOCK.STOCK_XON:
                return "xon"
            elif self == stock.STOCK.STOCK_XONE:
                return "xone"
            elif self == stock.STOCK.STOCK_XOXO:
                return "xoxo"
            elif self == stock.STOCK.STOCK_XPER:
                return "xper"
            elif self == stock.STOCK.STOCK_XPL:
                return "xpl"
            elif self == stock.STOCK.STOCK_XPLR:
                return "xplr"
            elif self == stock.STOCK.STOCK_XPO:
                return "xpo"
            elif self == stock.STOCK.STOCK_XRAY:
                return "xray"
            elif self == stock.STOCK.STOCK_XRF:
                return "xrf"
            elif self == stock.STOCK.STOCK_XRM:
                return "xrm"
            elif self == stock.STOCK.STOCK_XRX:
                return "xrx"
            elif self == stock.STOCK.STOCK_XSHD:
                return "xshd"
            elif self == stock.STOCK.STOCK_XSHQ:
                return "xshq"
            elif self == stock.STOCK.STOCK_XTH:
                return "xth"
            elif self == stock.STOCK.STOCK_XTLB:
                return "xtlb"
            elif self == stock.STOCK.STOCK_XTNT:
                return "xtnt"
            elif self == stock.STOCK.STOCK_XUSA:
                return "xusa"
            elif self == stock.STOCK.STOCK_XWEB:
                return "xweb"
            elif self == stock.STOCK.STOCK_XXII:
                return "xxii"
            elif self == stock.STOCK.STOCK_XYL:
                return "xyl"
            elif self == stock.STOCK.STOCK_Y:
                return "y"
            elif self == stock.STOCK.STOCK_YECO:
                return "yeco"
            elif self == stock.STOCK.STOCK_YELP:
                return "yelp"
            elif self == stock.STOCK.STOCK_YERR:
                return "yerr"
            elif self == stock.STOCK.STOCK_YESR:
                return "yesr"
            elif self == stock.STOCK.STOCK_YEXT:
                return "yext"
            elif self == stock.STOCK.STOCK_YGE:
                return "yge"
            elif self == stock.STOCK.STOCK_YGYI:
                return "ygyi"
            elif self == stock.STOCK.STOCK_YIN:
                return "yin"
            elif self == stock.STOCK.STOCK_YLD:
                return "yld"
            elif self == stock.STOCK.STOCK_YLDE:
                return "ylde"
            elif self == stock.STOCK.STOCK_YNDX:
                return "yndx"
            elif self == stock.STOCK.STOCK_YOGA:
                return "yoga"
            elif self == stock.STOCK.STOCK_YORW:
                return "yorw"
            elif self == stock.STOCK.STOCK_YPF:
                return "ypf"
            elif self == stock.STOCK.STOCK_YRCW:
                return "yrcw"
            elif self == stock.STOCK.STOCK_YRD:
                return "yrd"
            elif self == stock.STOCK.STOCK_YTEN:
                return "yten"
            elif self == stock.STOCK.STOCK_YTRA:
                return "ytra"
            elif self == stock.STOCK.STOCK_YUM:
                return "yum"
            elif self == stock.STOCK.STOCK_YUMA:
                return "yuma"
            elif self == stock.STOCK.STOCK_YUMC:
                return "yumc"
            elif self == stock.STOCK.STOCK_YUME:
                return "yume"
            elif self == stock.STOCK.STOCK_YY:
                return "yy"
            elif self == stock.STOCK.STOCK_Z:
                return "z"
            elif self == stock.STOCK.STOCK_ZAGG:
                return "zagg"
            elif self == stock.STOCK.STOCK_ZAIS:
                return "zais"
            elif self == stock.STOCK.STOCK_ZAYO:
                return "zayo"
            elif self == stock.STOCK.STOCK_ZBH:
                return "zbh"
            elif self == stock.STOCK.STOCK_ZBIO:
                return "zbio"
            elif self == stock.STOCK.STOCK_ZBK:
                return "zbk"
            elif self == stock.STOCK.STOCK_ZBRA:
                return "zbra"
            elif self == stock.STOCK.STOCK_ZBZX:
                return "zbzx"
            elif self == stock.STOCK.STOCK_ZB_A:
                return "zb_a"
            elif self == stock.STOCK.STOCK_ZB_G:
                return "zb_g"
            elif self == stock.STOCK.STOCK_ZB_H:
                return "zb_h"
            elif self == stock.STOCK.STOCK_ZDGE:
                return "zdge"
            elif self == stock.STOCK.STOCK_ZEAL:
                return "zeal"
            elif self == stock.STOCK.STOCK_ZEN:
                return "zen"
            elif self == stock.STOCK.STOCK_ZEUS:
                return "zeus"
            elif self == stock.STOCK.STOCK_ZF:
                return "zf"
            elif self == stock.STOCK.STOCK_ZFGN:
                return "zfgn"
            elif self == stock.STOCK.STOCK_ZG:
                return "zg"
            elif self == stock.STOCK.STOCK_ZGNX:
                return "zgnx"
            elif self == stock.STOCK.STOCK_ZION:
                return "zion"
            elif self == stock.STOCK.STOCK_ZIONW:
                return "zionw"
            elif self == stock.STOCK.STOCK_ZIONZ:
                return "zionz"
            elif self == stock.STOCK.STOCK_ZIOP:
                return "ziop"
            elif self == stock.STOCK.STOCK_ZIXI:
                return "zixi"
            elif self == stock.STOCK.STOCK_ZJZZT:
                return "zjzzt"
            elif self == stock.STOCK.STOCK_ZKIN:
                return "zkin"
            elif self == stock.STOCK.STOCK_ZLAB:
                return "zlab"
            elif self == stock.STOCK.STOCK_ZN:
                return "zn"
            elif self == stock.STOCK.STOCK_ZNGA:
                return "znga"
            elif self == stock.STOCK.STOCK_ZNH:
                return "znh"
            elif self == stock.STOCK.STOCK_ZNWAA:
                return "znwaa"
            elif self == stock.STOCK.STOCK_ZOES:
                return "zoes"
            elif self == stock.STOCK.STOCK_ZSAN:
                return "zsan"
            elif self == stock.STOCK.STOCK_ZTO:
                return "zto"
            elif self == stock.STOCK.STOCK_ZTR:
                return "ztr"
            elif self == stock.STOCK.STOCK_ZTS:
                return "zts"
            elif self == stock.STOCK.STOCK_ZUMZ:
                return "zumz"
            elif self == stock.STOCK.STOCK_ZVV:
                return "zvv"
            elif self == stock.STOCK.STOCK_ZX:
                return "zx"
            elif self == stock.STOCK.STOCK_ZYME:
                return "zyme"
            elif self == stock.STOCK.STOCK_ZYNE:
                return "zyne"
"""
