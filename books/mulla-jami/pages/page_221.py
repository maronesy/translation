# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 221 (printed ٢٢٠)."""

PAGE_NUMBER = 221
PRINTED_PAGE = "٢٢٠"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues from p.220: «… (على) الاستعمال (الأكثر …)».
    {"type": "matn",
     "ar": "(الأكثر فيقال) في «يا حارث» (يا حار) بكسر الراء على ما كان عليه قبل الترخيم،",
     "en": "…(most frequent) usage, (so one says), for “yā Ḥārithu,” (“yā Ḥāri”) with a kasra on the rāʾ, as it was before the truncation (tarkhīm);"},
    {"type": "matn",
     "ar": "(و) في «يا ثمود» (يا ثمو) بواو متطرفة بعد ضمة، (و) في «يا كروان» (يا كرو) بواو متحركة بعد فتحة.",
     "en": "(and) for “yā Thamūdu,” (“yā Thamu”), with a final wāw after a ḍamma; (and) for “yā Karawānu,” (“yā Karaw”), with a vowelled wāw after a fatḥa."},
    {"type": "matn",
     "ar": "(وقد يجعل) «قد» للتقليل، أي: ويجعل المنادى المرخم على الاستعمال الأقل (اسما برأسه) كأنه لم يحذف منه شيء،",
     "en": "(And it is sometimes made)—“qad” denotes infrequency—that is, the truncated vocative is made, in the less frequent usage, (a noun in its own right), as if nothing had been elided from it,"},
    {"type": "matn",
     "ar": "فيكون له في بنائه وإعلاله وتصحيحه حكم نفسه لا حكم الأصل.",
     "en": "so that in its indeclinable ending, its weak-letter change (iʿlāl) and its retention of the sound form (taṣḥīḥ) it has its own rule, not the rule of the original."},
    {"type": "matn",
     "ar": "(فيقال[[١]]: «يا حار») بالضم كأنه اسم مفرد معرفة برأسه،",
     "en": "(So one says: “yā Ḥāru”) with a ḍamma, as if it were a single, definite noun in its own right;"},
    {"type": "matn",
     "ar": "فيضم (ويا ثمي)؛ لأنه لما جعل «ثمو» اسما برأسه، صارت الواو طرفا بعد ضمة،",
     "en": "so it takes the ḍamma. (And “yā Thamī”), because when “Thamu” was made a noun in its own right, the wāw became final after a ḍamma;"},
    {"type": "matn",
     "ar": "فلا جرم قلبت ياء[[٢]] وكسر ما قبلها كـ«أدل» في «أدلو»[[٣]]",
     "en": "it was therefore necessarily changed to a yāʾ and the letter before it given a kasra, like “adlin” for “adluw.”"},
    {"type": "matn",
     "ar": "(ويا كرا[[٤]])؛ لأنه لما جعل «كرو» اسما برأسه ارتفع مانع الإعلال، وهو وقوع الساكن بعد الواو،",
     "en": "(And “yā Karā”), because when “Karaw” was made a noun in its own right, the impediment to iʿlāl—namely the occurrence of an unvowelled letter after the wāw—was removed,"},
    {"type": "matn",
     "ar": "فانقلبت الواو ألفا لتحركها وانفتاح ما قبلها.",
     "en": "so the wāw changed into an alif, because it is vowelled and the letter before it has a fatḥa."},

    {"type": "section", "ar": "[المندوب]",
     "en": "The Lamented Noun (al-Mandūb)"},

    {"type": "matn",
     "ar": "(وقد استعملوا[[٥]]) يعني: العرب (صيغة النداء) يعني «يا»[[٦]] خاصة (في المندوب)؛",
     "en": "(They have used)—he means the Arabs—(the form of the vocative)—he means “yā” specifically—(for the lamented noun—al-mandūb),"},
    {"type": "matn",
     "ar": "لأنه لا يدخل عليه سواها[[٧]]، لكونها أشهر صيغها[[٨]]، فكانت أولى بأن يتوسع فيها باستعمالها في غير المنادى.",
     "en": "since no other [vocative particle] enters upon it; because it is the best known of its forms, it was the more fitting to be extended by being used for what is not a vocative."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "الفاء فصيحة، أي: إذا كان كذلك فيقال،",
     "en": "The fāʾ is the “disclosing” fāʾ (faṣīḥa), that is: if that is so, then one says;"},
    {"type": "pair",
     "ar": "أو عاطفة عطف الفعلية على الاسمية المؤولة بالفعلية، كأنه قيل: يجعل المنادى ثابتا بجميع أجزائه، أو المحذوف ثابتا فيقال.",
     "en": "or it is conjunctive, coordinating the verbal sentence with the nominal sentence interpreted as verbal, as if it were said: “the vocative is treated as present with all its parts,” or “the elided part is treated as present, so one says.”"},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "لأنه لم يأت في كلام العرب اسم متمكن آخره واو، قبلها ضمة، إلا وتقلب الواو ياء، والضمة كسرة، نحو: التغازي والأدلي،",
     "en": "Because no fully declinable (mutamakkin) noun ending in a wāw preceded by a ḍamma occurs in the speech of the Arabs without the wāw changing into a yāʾ and the ḍamma into a kasra, as in al-taghāzī and al-adlī;"},
    {"type": "pair",
     "ar": "والمنادى في حكم المتمكن لعروض بنائه.",
     "en": "and the vocative counts as fully declinable, because its indeclinability is accidental."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "لأن المنادى في حكم المعرب لعروض بنائه، فأعل بما يعل به الاسم المعرب.",
     "en": "Because the vocative counts as declinable (muʿrab), its indeclinability being accidental; so it undergoes the iʿlāl that the declinable noun undergoes."},
    {"type": "pair",
     "ar": "ولم يجعل في حكم هو مع أنه مبني.",
     "en": "And it was not treated like “huwa,” although it is indeclinable."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "مثل بثلاثة أمثلة؛ لأن التغير في الاستعمال الأقل: إما بالحركة فقط، أو بالحرف، أو بكليهما.",
     "en": "He gave three examples because the change in the less frequent usage is either in the vowel only, or in the letter, or in both."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "لا وجه لإيراد المندوب في أثناء مباحث المنادى والفصل به بين مباحثه، فالأولى أن يؤخر عن بحث المنادى برمته.",
     "en": "There is no reason to bring in the lamented noun in the midst of the discussions of the vocative and to separate those discussions with it; it would have been better to defer it until the whole discussion of the vocative was complete."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "إشعار بأن «يا» أصل في حروف النداء حتى يعبر عنه بصيغة النداء.",
     "en": "This indicates that “yā” is the basic vocative particle, so that it is referred to as “the form of the vocative.”"},
    {"type": "pair",
     "ar": "ويجوز أن يراد بصيغة النداء مجموع المنادى مع الياء للتنبيه على أن صيغة النداء استعيرت للمندوب.",
     "en": "“The form of the vocative” may also mean the vocative together with the yāʾ, to point out that the form of the vocative has been borrowed for the lamented noun."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "علة لذكر قوله: خاصة.",
     "en": "[This is] the reason for his mentioning “specifically.”"},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "ولهذا أطلق صيغة النداء، وأريد «يا» خاصة لانصراف المطلق إليه،",
     "en": "For this reason he spoke of “the form of the vocative” without qualification while meaning “yā” specifically, since the unqualified term is taken to refer to it;"},
    {"type": "pair",
     "ar": "ولم يقل: وقد استعملوا «يا» في المندوب مع أنها أخصر وأظهر للتنبيه على أن الصيغة أعيرت للمندوب.",
     "en": "and he did not say “they have used ‘yā’ for the lamented noun,” though that is shorter and clearer, to point out that the form has been lent to the lamented noun."},
]
