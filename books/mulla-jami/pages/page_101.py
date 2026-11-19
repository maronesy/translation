# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 101 (printed ١٠٠)."""

PAGE_NUMBER = 101
PRINTED_PAGE = "١٠٠"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The base text (matn) ----------------
    {"type": "matn",
     "ar": "أوصاف، ولم يهجر استعمالها في معانيها الأصلية أيضا بالكلية، فالمانع من الصرف في هذه الأسماء: الصفة الأصلية، ووزن الفعل.",
     "en": "[They are] adjectives, and their use in their original meanings has not been wholly abandoned either; so what prevents these nouns from full declension (al-ṣarf) is the original adjectival quality and the verbal pattern (wazn al-fiʿl)."},
    {"type": "matn",
     "ar": "وأما عند استعمالها في معانيها الأصلية، فلا إشكال في منع صرفها، لوزن الفعل، والوصف في الأصل والحال.",
     "en": "As for when they are used in their original meanings, there is no difficulty in their being prevented from declension — on account of the verbal pattern and of the adjectival quality, both originally and in [the present] state."},
    {"type": "matn",
     "ar": "(وضعف منع «أفعى»[[١]]) اسما (للحية) على زعم وصفيته، لتوهم اشتقاقه من «الفعوة» التي هي الخبث.",
     "en": "(And the prevention of full declension of “afʿā”[[١]] is weak,) it being a noun (for a snake), upon the supposition of its being adjectival — because of the [false] imagining that it is derived from “al-faʿwa,” which is [the sense of] foulness."},
    {"type": "matn",
     "ar": "(و) كذلك منع (أجدل للصقر) على زعم وصفيته لتوهم اشتقاقه من الجدل بمعنى القوة.",
     "en": "(And) likewise the prevention of the full declension of (“ajdal,” for the falcon), upon the supposition of its being adjectival — because of imagining it derived from al-jadl in the sense of strength."},
    {"type": "matn",
     "ar": "(وأخيل للطائر) أي: لطائر ذي خيلان[[٢]] على زعم وصفيته، لتوهم اشتقاقه من الخال.",
     "en": "(And of “akhyal,” for the bird) — that is: for a bird possessing khīlān (moles)[[٢]] — upon the supposition of its being adjectival, because of imagining it derived from al-khāl (the mole)."},
    {"type": "matn",
     "ar": "ووجه ضعف منع الصرف في هذه الأسماء عدم الجزم بكونها أوصافا أصلية،",
     "en": "The aspect of the weakness of preventing declension in these nouns is the lack of certainty that they are original adjectives,"},
    {"type": "matn",
     "ar": "فإنها لم يقصد بها المعاني الوصفية مطلقا[[٣]]، لا في الأصل، ولا في الحال[[٤]]، مع أن الأصل في الاسم الصرف[[٥]].",
     "en": "for the adjectival meanings were not intended by them at all[[٣]] — neither originally nor in [the present] state[[٤]] — given that the default (al-aṣl) for a noun is full declension (al-ṣarf)[[٥]]."},

    {"type": "section", "ar": "[ التأنيث بالتاء ]",
     "en": "Feminization by the Tāʾ"},

    {"type": "matn",
     "ar": "(التأنيث) اللفظي الحاصل (بالتاء[[٦]]) لا بالألف، فإنه لا شرط له[[٧]]. (شرطه) في",
     "en": "(The feminization —) the morphological [feminization] effected (by the tāʾ[[٦]]), not by the alif, for the latter has no condition[[٧]]. (Its condition [lies]) in ..."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "فإن قلت: لو أوجب تقدير الوصفية من غير تحقق ضعف منع الصرف لأوجب تقدير العدل أيضا من غير تحقق ضعف منع الصرف في «عمر» فلم لم يحكم بالضعف فيه؟",
     "en": "If you say: were the [mere] positing of the adjectival quality, without its [actual] realization, to necessitate a weakening of the prevention of declension, then the positing of deflection (al-ʿadl), without its realization, ought likewise to have necessitated a weakening of the prevention of declension in “ʿUmar” — so why has weakness not been judged in it?"},
    {"type": "pair",
     "ar": "قلت: تقدير السبب بعد تحقق منع صرف «عمر» لا يوجب ضعفه. وإنما يوجب ضعفه لتقديره، ولم يتحقق منع الصرف في «أفعى» كما في «عمر».",
     "en": "I say: positing the cause (al-sabab) after the prevention of the declension of “ʿUmar” has [already] been realized does not necessitate its weakening. Rather, [the case] necessitates its weakening [only] because [the cause] is [merely] posited — and the prevention of declension has not been realized in “afʿā” as it has in “ʿUmar.”"},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "جمع خال، وهو المعروف.",
     "en": "[Khīlān is] the plural of khāl (mole), and it is the well-known [term]."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "قيد لم يقصد.",
     "en": "[The word “at all” (muṭlaqan)] is a qualification of “were not intended.”"},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "أما الأول فظاهر أنه لم يثبت. وأما الثاني فلأن المستعمل لم يقصد بتلك الألفاظ إلا أنواعا مخصوصة من غير ملاحظة خبث وقوة وخال وإن كانت في نفسها متصفة بتلك الأوصاف.",
     "en": "As for the first [“not originally”], it is evident that it was never established. As for the second [“nor in the present state”], it is because the user intended by those words only specific species [of creature], without regard to foulness, strength, and mole — even if [those creatures] are in themselves characterized by those attributes."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "أي: لعدم احتياجه إلى الشرط، وليكون إعرابه بأتم وجه.",
     "en": "That is: because it (the noun) has no need of any condition [to be declinable], and so that its iʿrāb (inflection) may be in the most complete manner."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "قال العصام: قيده باللفظي ليقابل المعنوي، ولا يقابله بالتاء لاشتراكها بينهما.",
     "en": "Al-ʿIṣām said: he restricted it with “morphological” (lafẓī) in order to contrast it with “semantic” (maʿnawī), and he did not contrast it with “by the tāʾ,” because the tāʾ is shared between them."},
    {"type": "pair",
     "ar": "وأنا أظن أن مراد المصنف التأنيث الذي يعرف بالتاء، والمعنوي لم يعرف بالتاء، بل بأمارات تدل على اعتبار العرب تأنيثه فاعرفه فإنه دقيق، وبالاعتبار حقيق.",
     "en": "But I hold that the author's intent is the feminization that is recognized by the tāʾ, whereas the semantic [feminization] is not recognized by the tāʾ but by indications pointing to the Arabs' regarding it as feminine — so grasp it, for it is subtle and worthy of consideration."},
    {"type": "pair",
     "ar": "يقال: المراد تاء تنقلب هاء، فتاء أخت ليست للتأنيث، ولو سمي به مذكر لا يمتنع، ولو سمي به مؤنث فحاله كحال عرفات.",
     "en": "It is said: what is meant is a tāʾ that turns into a hāʾ [in pause]; thus the tāʾ of “ukht” (sister) is not for feminization, so that, were a male named with it, it would not be prevented from declension, and were a female named with it, its case would be like the case of “ʿArafāt.”"},
    {"type": "pair",
     "ar": "فقال الزمخشري: عرفات تنصرف. ولذا يجري عليه الكسر والتنوين؛ لأن هذه التاء ليست للتأنيث، ويمنع من تقدير تاء التأنيث إذا لم يعهد في كلامهم اجتماعها مع تاء التأنيث.",
     "en": "Al-Zamakhsharī said: “ʿArafāt” is fully declinable, and for that reason the kasra and tanwīn apply to it, because this tāʾ is not for feminization; and one is barred from positing the feminine tāʾ [in it], since its combining with the feminine tāʾ is not attested in their speech."},
    {"type": "pair",
     "ar": "وقال غيره: يمنع من الصرف، ولا يمنع من غير المنصرف كثرة جمع المؤنث وتنوين المقابلة.",
     "en": "Another said: it is prevented from full declension, and the frequency of [its being treated as] a feminine plural, together with the tanwīn of counterbalancing (tanwīn al-muqābala), does not remove it from [the category of] the non-declinable (ghayr al-munṣarif)."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "للزوم الألف.",
     "en": "Because of the permanence of the alif."},
]
