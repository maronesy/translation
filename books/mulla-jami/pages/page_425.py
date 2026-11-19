# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 425 (printed ٤٢٤)."""

PAGE_NUMBER = 425
PRINTED_PAGE = "٤٢٤"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «فالأشياء هي المعدودات، وآحادها كل واحد واحد منها، وكمية الآحاد ما» at the foot of PDF p. 424.
    {"type": "matn",
     "ar": "يجاب به إذا سئل عن واحد واحد أو عن أكثر من واحد من تلك المعدودات بـ«كم» والألفاظ الموضوعة بإزاء تلك الكميات، بأن يكون كل واحد منها موضوعا لكمية واحدة منها أسماء العدد،",
     "en": "…is given in answer when one asks with “kam” about each single one, or about more than one, of those counted things; and the expressions imposed for those quantities, each of them being imposed for one of those quantities, are the number nouns."},
    {"type": "matn",
     "ar": "فالواحد موضوع لكمية آحاد الأشياء إذا أخذت منفردة، فإذا سئل عن معدود معدود منها بـ«كم» هو يجاب بالواحد",
     "en": "So “one” is imposed for the quantity of the units of things when they are taken singly; when one asks with “kam” about each single counted thing among them, the answer is given with “one”."},
    {"type": "matn",
     "ar": "والاثنان موضوع لكميتها إذا أخذت مجتمعة متكررة مرة واحدة، فإذا سئل عن معدودين معدودين بـ«كم» يجاب بالاثنين، وهكذا إلى ما لا نهاية له.",
     "en": "“Two” is imposed for their quantity when they are taken combined, repeated once; when one asks with “kam” about each pair of counted things, the answer is given with “two”; and so on without end."},
    {"type": "matn",
     "ar": "فظهر من هذا التقرير أن لفظ الواحد والاثنين داخلان في هذا التعريف؛ لأنهما من أسماء العدد في عرف النحاة، وإن لم يكونا عند بعض أهل الحساب من العدد[[١]]،",
     "en": "From this exposition it is clear that the words “one” and “two” are included in this definition, because they are number nouns in the usage of the grammarians, even if, for some arithmeticians, they are not numbers."},
    {"type": "matn",
     "ar": "ولما كان المتبادر من هذه العبارة أن نفس الكمية هي الموضوع له من غير اعتبار معنى آخر، لا ينتقض التعريف بمثل: «رجل ورجلين، وذراع وذراعين، ومن ومنين» حيث لا يفهم منها الوحدة والاثنينية فقط.",
     "en": "Since what first comes to mind from this wording is that quantity itself is what [the word] is imposed for, without regard to any other meaning, the definition is not undermined by examples such as “rajul” and “rajulayn” (a man, two men), “dhirāʿ” and “dhirāʿayn” (a cubit, two cubits), “mann” and “mannayn” (a mann, two manns), since oneness and twoness alone are not understood from them."},
    {"type": "matn",
     "ar": "(أصولها) أي: أصول أسماء العدد التي يتفرع منها باقيها:",
     "en": "(Their roots), that is, the roots of the number nouns from which the rest branch off:"},
    {"type": "matn",
     "ar": "إما بإلحاق تاء التأنيث كـ«واحدة» و«اثنتان» أو بإسقاطها[[٢]] كـ«ثلاث» إلى «تسع»، أو بالتثنية كـ«مائتين وألفين»،",
     "en": "either by adding the feminine tāʾ, as in “wāḥida” and “ithnatān”, or by dropping it, as in “thalāth” to “tisʿ”; or by the dual, as in “miʾatayn” and “alfayn”;"},
    {"type": "matn",
     "ar": "أو بالجمع كـ«مئات وألوف وعشرين»، أو بالتركيب إضافيا كان كـ«ثلاثمائة»، وامتزاجيا كـ«خمسة عشر»[[٣]]، أو بالعطف كـ«خمسة وعشرين»",
     "en": "or by the plural, as in “miʾāt”, “ulūf” and “ʿishrīn”; or by compounding, whether genitival, as in “thalāthumiʾa”, or blended (imtizājī), as in “khamsata ʿashara”; or by coordination, as in “khamsa wa-ʿishrīn”:"},
    {"type": "matn",
     "ar": "(اثنتا عشرة كلمة: واحد إلى عشرة، ومائة، وألف).",
     "en": "(twelve words: one to ten, hundred, and thousand)."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "أي: وإن لم يكن شيء منهما عند بعض الحساب من العدد.",
     "en": "That is, even if neither of them is a number for some arithmeticians."},
    {"type": "pair",
     "ar": "أما الواحد فليس بعدد عند أحد من الحساب؛ لأن العدد نصف مجموع حاشيتيه عند بعض.",
     "en": "As for “one”, it is not a number for any of the arithmeticians, because number, according to some, is half the sum of its two flanking [numbers]."},
    {"type": "pair",
     "ar": "وبعضهم استثنى من التعريف الزوج الأول فقال: إذا لم يكن الفرد الأول عددا، ينبغي ألا يكون الزوج الأول عددا أيضا.",
     "en": "Some of them excepted the first even number from the definition and said: if the first odd number is not a number, the first even number should not be a number either."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "فإن الأصل في الثلاثة وأخواتها ثبوت التاء.",
     "en": "For the original state in thalātha and its sisters is the presence of the tāʾ."},
    {"type": "pair",
     "ar": "في شرح التسهيل للفاضل المصري: الثلاثة وأخواتها أسماء جماعات كعزة وزمرة وأمة وفرقة وعصبة وصحبة وسرية وفئة وعشيرة وقبيلة وفصيلة،",
     "en": "In the commentary on al-Tashīl by the learned Egyptian: thalātha and its sisters are names of groups, like ʿizza, zumra, umma, firqa, ʿuṣba, ṣuḥba, sariyya, fiʾa, ʿashīra, qabīla and faṣīla;"},
    {"type": "pair",
     "ar": "فالأصل أن تكون بالتاء لتوافق الأسماء التي هي بمنزلتها، فاستصحب الأصل مع المعدود المذكر لتقدم رتبته، وحذفت التاء مع المعدود المؤنث لتأخر رتبته،",
     "en": "so the default is that they have the tāʾ, to agree with the nouns that are of their standing; the default was retained with a masculine counted noun because its rank is prior, and the tāʾ was dropped with a feminine counted noun because its rank is posterior."},
    {"type": "pair",
     "ar": "ويدل على أن أصلها التاء أن العرب إذا قصدت مجرد العدد تقول: ثلاثة نصف ستة.",
     "en": "What shows that their original form has the tāʾ is that the Arabs, when they intend bare number, say: “thalātha is half of sitta”."},
    {"type": "pair",
     "ar": "وفي الرضي: إنما وضعت على التأنيث في الأصل؛ لأن كل جمع إنما يصير مؤنثا في كلامهم بسبب كونه على عدد فوق الاثنين،",
     "en": "In al-Raḍī: they were imposed originally in the feminine only because every plural becomes feminine in their speech by virtue of its being of a number above two;"},
    {"type": "pair",
     "ar": "فإذا صار المذكر في نحو: رجال مؤنثا بسبب عروض هذا العارض، فتأنيث العارض في نفسه أولى.",
     "en": "so if the masculine, as in rijāl, becomes feminine because this accident befalls it, then the feminine status of the accident itself is all the more fitting."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "جعله الرضي من العطف؛ لأنه في الأصل بالعطف، والشارح آثر رعاية الحال على رعاية الأصل،",
     "en": "Al-Raḍī counted it under coordination, because it is originally by coordination; the Commentator preferred regard for the present state over regard for the origin."},
    {"type": "pair",
     "ar": "لكن الصواب أو تضمنيا لكان امتزاجيا.",
     "en": "But the correct [wording] is “or implicative (taḍammunī)” in place of “blended (imtizājī)”."},
    # REVIEW: «لكن الصواب أو تضمنيا لكان امتزاجيا» is printed so; «لكان» is presumably a misprint for «مكان» ("in place of"). Transcribed as printed; translated on that reading.
]
