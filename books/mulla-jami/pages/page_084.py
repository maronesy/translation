# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 84 (printed ٨٣)."""

PAGE_NUMBER = 84
PRINTED_PAGE = "٨٣"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- Main text (matn) ----------------
    {"type": "matn",
     "ar": "عرف غير المنصرف، واكتفى بتعريفه، فقال: (غير المنصرف[[١]]: ما) أي: اسم معرب[[٢]]",
     "en": "He defined the diptote (ghayr al-munṣarif) and contented himself with defining it, saying: (The diptote is “mā” — that which), that is: a declinable noun,"},
    {"type": "matn",
     "ar": "(فيه علتان[[٣]] تؤثران باجتماعهما[[٤]]، واستجماع شرائطهما[[٥]] فيه أثرا) أي: (من[[٦]]) علل (تسع أو علة واحدة منها تقوم) أي: من تلك التسع تقوم هذه العلة الواحدة (مقامهما) أي: مقام هاتين العلتين، تؤثر وحدها تأثيرهما.",
     "en": "(in which are two causes that exert, by their coming together and the completing of their conditions in it, an effect), that is: (from) causes (nine, or a single cause among them that stands) — that is: from those nine, this single cause stands (in their place — maqāmahumā), that is: in the place of these two causes, exerting by itself their effect."},
    {"type": "matn",
     "ar": "(وهي) أي: العلل التسع مجموع ما في هذين البيتين من الأمور التسعة، لا كل واحد منها،",
     "en": "(And they — wa-hiya) that is: the nine causes are the totality of what these two verses contain of the nine matters, not each one of them singly,"},
    {"type": "matn",
     "ar": "حتى يقال: لا يصح الحكم على العلل التسع بكل واحد من هذه الأمور، وذلك المجموع[[٧]]:",
     "en": "such that one might say: it is not valid to predicate of the nine causes each one of these matters. And that totality is:"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "المنصرف مأخوذ من الصرف، وهو الفضل والزيادة، وإنما سمي المنصرف به لاشتماله على زيادة على الإعراب، أعني: التنوين، وهي علامته، أو لاتصافه بزيادة تمكن.",
     "en": "Al-munṣarif is derived from al-ṣarf, which is superiority and increase; it is called munṣarif only because it thereby comprises an increase over iʿrāb — namely, tanwīn, which is its mark — or because of its being characterized by an increase of firm establishment (tamakkun)."},
    {"type": "pair",
     "ar": "ولذا يقال له: الأمكن. ولما عري مقابله عن تلك الزيادة سمي بغير المنصرف.",
     "en": "For this reason it is called “the most firmly established” (al-amkan); and since its counterpart is stripped of that increase, it is named ghayr al-munṣarif (the diptote)."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "جعل «ما» موصولة لا موصوفة؛ لأن حق الخبر أن يكون نكرة، ولئلا يلزم تعريف الخبر وتنكير المبتدأ؛ لأن «غير» لا يكتسب التعريف من المضاف إليه.",
     "en": "He made “mā” a relative pronoun, not a qualified [indefinite] noun, because the due status of the predicate is that it be indefinite, and lest it entail a definite predicate and an indefinite subject, since “ghayr” does not acquire definiteness from the noun to which it is annexed."},
    {"type": "pair",
     "ar": "وفيه أن المراد بغير المنصرف معناه العرفي، وهو مفهوم محصل لم يلاحظ فيه معنى المغايرة.",
     "en": "Yet [it may be objected] that what is meant by “ghayr al-munṣarif” is its conventional sense, which is a determinate concept in which the meaning of “otherness” is not regarded."},
    {"type": "pair",
     "ar": "وله أن يقول: إنه بهذا المعنى أيضا نكرة؛ لأن الظاهر أنه اسم جنس لا علم جنس؛ لأنه علم ضروري ولا ضرورة هنا. والقول بأنه خبر قدم يخالف الأسلوب الشائع من تقديم المعروف، وجعله موضوعا، والقاعدة المحفوظة أيضا من أن سبق العلم بشيء يستدعي جعله موضوعا، وقد سبق العلم بغير المنصرف.",
     "en": "He may reply: even in this sense it is indefinite, since it is apparently a generic noun (ism jins), not a proper generic name (ʿalam jins) — for a proper generic name is a necessity, and there is no necessity here. And to say that it is a fronted predicate contradicts the common style of placing the [more] familiar term first and making it the subject (mawḍūʿ), as well as the established rule that prior knowledge of a thing calls for making it the subject — and knowledge of “ghayr al-munṣarif” has indeed preceded."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "فاعل الظرف، أو مبتدأ قدم خبره، والجملة صفة «ما». العلة في اللغة: عارض غير طبيعي يستدعي حالة غير طبيعية.",
     "en": "[It is] the subject of the adverbial phrase, or a subject whose predicate is advanced, the sentence being a description of “mā.” “ʿIlla” (cause) in the [ordinary] language is: a non-natural accident that calls for a non-natural state."},
    {"type": "pair",
     "ar": "وفي اصطلاح النحاة ليست بمعنى الموجب، بل بمعنى ما ينبغي أن يختار المتكلم عند حصوله أمرا يناسبه، وذلك الأمر المناسب يسمى بالحكم.",
     "en": "In the terminology of the grammarians it is not in the sense of that which necessitates, but in the sense of that upon whose occurrence the speaker should choose a matter befitting it — and that befitting matter is called the ruling (al-ḥukm)."},
    {"type": "pair",
     "ar": "فعلى هذا يكون إطلاق العلة على كل واحد مجازا، لكن صريح كلام المصنف في الإيضاح يدل على أن إطلاق السبب على كل من التسع حقيقة.",
     "en": "Accordingly, applying “cause” to each one individually would be figurative; yet the plain wording of the author in al-Īḍāḥ indicates that applying “sabab” (occasioning cause) to each of the nine is literal."},
    {"type": "pair",
     "ar": "وبنى ذلك على أن صاحب المفصل ثنى السبب في تعريف غير المنصرف حيث قال: ما فيه سببان، ولم يقل: ما فيه سبب. ولا يخفى أن هذا الوجه جار في العلتين أيضا، فيكون إطلاق العلة على كل واحد حقيقة عنده. فاعل الظرف، أو مبتدأ قدم خبره، والجملة صفة «ما».",
     "en": "He built this on the fact that the author of al-Mufaṣṣal dualized “sabab” in defining the diptote, saying: “that which contains two occasioning causes,” and did not say: “that which contains an occasioning cause.” It is not hidden that this line of reasoning applies to the two causes (ʿillatān) as well, so that applying “ʿilla” to each one individually is, for him, literal. [It is] the subject of the adverbial phrase, or a subject whose predicate is advanced, the sentence being a description of “mā.”"},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "هذا القيد إشارة إلى أن مثل «حبلى» و«مصابيح» علمين خارج عن هذا الجزء من التعريف، داخل في الجزء الآخر منه، وهو قوله: «أو واحدة منها تقوم مقامهما»؛",
     "en": "This restriction points to [the fact] that the likes of “ḥublā” and “maṣābīḥ,” when [treated as] proper names, fall outside this part of the definition and inside its other part — namely his words: “or a single cause among them that stands in their place”;"},
    {"type": "pair",
     "ar": "لأنهما وإن كان فيهما علتان، لكن المؤثر العلة الواحدة، وهي التأنيث في الأول، والجمعية في الثاني لا العلمية، ولهذا لو نكرا لم ينصرفا أيضا.",
     "en": "for although each of them contains two causes, yet what exerts the effect is [only] the single cause — namely femininity in the first and pluralness in the second, not proper-namehood (ʿalamiyya) — and for this reason, even if they were made indefinite they still would not be triptote."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "قيد بذلك لئلا يتوهم أن مجرد اجتماع العلتين كاف في التأثير، حتى يلزم أن يكون مثل «نوح» غير منصرف مع أنه منصرف.",
     "en": "He restricted it thereby lest one imagine that the mere coming-together of the two causes suffices for the effect — which would entail that a word like “Nūḥ” be a diptote, even though it is [in fact] a triptote."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "لم يقل: من تسع علل؛ حتى يكون المحذوف المضاف إليه لا الموصوف؛ لأن شرط حذف المضاف إليه لم يتحقق فيه.",
     "en": "He did not say “from nine causes” [min tisʿi ʿilalin], so that the elided element would be the noun of annexation (muḍāf ilayhi) and not the described noun (mawṣūf); because the condition for eliding the muḍāf ilayhi was not fulfilled here."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "عدل: لقد بلغ تنكير الأسباب في هاتين البيتين نهاية الحسن؛ إذ السبب عدل ما، لا كل عدل، وهو عدل لا يكون علة للبناء، وكذا السبب وصف ما، وهو الوصف الأصلي وهكذا.",
     "en": "“ʿAdl” (deviation): The rendering of the occasioning causes indefinite in these two verses has indeed reached the utmost of excellence; for an occasioning cause is a certain [kind of] deviation, not every deviation — a deviation that is not itself a cause of indeclinability (bināʾ); and likewise the occasioning cause [in the case of description] is a certain [kind of] description, namely the original description; and so on."},
    {"type": "pair",
     "ar": "وحينئذ كان المناسب تنكير النون أيضا، إلا أنه لم يساعده النظم، فأحسن ما قال بعض الشارحين: إن الألف واللام فيه زائدة.",
     "en": "In that case it would have been fitting to render “the nūn” indefinite as well, except that the metre did not permit it; so the best of what some commentators have said is that the alif and lām in it are extra (zāʾida)."},
]
